import random
import logging
from typing import Dict, Any, Optional, TYPE_CHECKING
from ..models import BusinessProfile
from .serpapi_service import SerpAPIService
from .scoring_service import ScoringService

if TYPE_CHECKING:
    pass

logger = logging.getLogger(__name__)


class BusinessService:
    """Core service for business profile management"""

    def __init__(self):
        self.serpapi_service = SerpAPIService()
        self.scoring_service = ScoringService()

    def get_or_create_business(
        self, business_name: str, website: Optional[str] = None
    ) -> BusinessProfile:
        """Get existing business or create with real SerpAPI data"""
        business = BusinessProfile.objects.create(name=business_name)

        self._update_business_data(business, website)

        return business

    def format_business_data(self, business: BusinessProfile) -> Dict[str, Any]:
        """Format business data for API response"""
        return {
            # Basic Information
            "name": business.name,
            "website": business.website,
            "description": business.description,
            "category": business.category,
            "established_year": business.established_year,
            # Contact Information
            "phone": business.phone,
            "email": business.email,
            # Location Details
            "address": business.address,
            "city": business.city,
            "state": business.state,
            "postal_code": business.postal_code,
            "country": business.country,
            "full_address": business.full_address,
            # Business Operations
            "business_hours": business.business_hours,
            "is_open": business.is_open,
            "temporarily_closed": business.temporarily_closed,
            # Business Characteristics
            "price_range": business.price_range,
            "cuisine_type": business.cuisine_type,
            # Service Options
            "offers_delivery": business.offers_delivery,
            "offers_takeout": business.offers_takeout,
            "offers_dine_in": business.offers_dine_in,
            "accepts_reservations": business.accepts_reservations,
            "service_options": (
                business.service_options_summary
                if hasattr(business, "service_options_summary")
                else None
            ),
            # Online Presence
            "facebook_url": business.facebook_url,
            "instagram_url": business.instagram_url,
            "twitter_url": business.twitter_url,
            # Review Metrics
            "review_count": business.review_count,
            "average_rating": float(business.rating) if business.rating else 0.0,
            "rating": float(business.rating) if business.rating else 0.0,
            "google_reviews": (
                business.google_reviews
                if hasattr(business, "google_reviews")
                else business.review_count
            ),
            "yelp_reviews": (
                business.yelp_reviews if hasattr(business, "yelp_reviews") else 0
            ),
            "total_reviews": business.review_count,
            "reviews": business.reviews if hasattr(business, "reviews") else [],
            # Content Metrics
            "image_count": business.image_count,
            "images": business.images if hasattr(business, "images") else [],
            "has_hours": business.has_hours,
            "has_description": business.has_description,
            "has_menu": business.has_menu,
            "menu_url": business.menu_url,
            # Features & Amenities
            "has_parking": business.has_parking,
            "wheelchair_accessible": business.wheelchair_accessible,
            "has_wifi": business.has_wifi,
            "accepts_credit_cards": business.accepts_credit_cards,
            "outdoor_seating": business.outdoor_seating,
            "special_features": (
                business.special_features
                if hasattr(business, "special_features")
                else []
            ),
            "popular_dishes": (
                business.popular_dishes if hasattr(business, "popular_dishes") else []
            ),
            # Additional SerpAPI fields
            "data_id": business.data_id if hasattr(business, "data_id") else "",
            "place_id": getattr(business, "place_id", ""),
        }

    def _update_business_data(
        self, business: BusinessProfile, website: Optional[str] = None
    ):
        """Update business with data from SerpAPI or fallback"""
        serpapi_data = self.serpapi_service.search_business(business.name)

        if serpapi_data:
            self._update_from_serpapi_data(business, serpapi_data)
        # else:
        #     self._set_fallback_data(business, website)

        business.save()
        logger.info(f"Updated business {business.name}")

    def _update_from_serpapi_data(
        self, business: BusinessProfile, serpapi_data: Dict[str, Any]
    ):
        """Update business model with SerpAPI data"""
        try:
            # Basic location and contact info
            business.address = serpapi_data.get("address", "")
            business.phone = serpapi_data.get("phone", "")
            business.website = serpapi_data.get("website", "")
            business.description = serpapi_data.get("description", "")

            # Store data_id for fetching additional data
            business.data_id = serpapi_data.get("data_id", "")

            # Ratings and reviews
            business.rating = serpapi_data.get("rating", 0.0)
            business.review_count = serpapi_data.get("reviews", 0)

            # Images
            images = serpapi_data.get("images", [])
            business.image_count = len(images)

            # Store actual image URLs (limit to first 10 for performance)
            business.images = []
            for img in images[:10]:
                if isinstance(img, dict) and img.get("thumbnail"):
                    business.images.append(
                        {
                            "url": img["thumbnail"],
                            "title": img.get("title", ""),
                            "source": "Google",
                        }
                    )

            # If we have a data_id, fetch additional reviews and photos
            if business.data_id:
                # Fetch reviews from SerpAPI Reviews endpoint
                reviews_data = self.serpapi_service.get_reviews(business.data_id, 5)
                business.reviews = []

                for review in reviews_data:
                    if isinstance(review, dict):
                        business.reviews.append(
                            {
                                "rating": review.get("rating", 0),
                                "text": review.get("snippet", review.get("text", "")),
                                "author": review.get("user", {}).get(
                                    "name", review.get("author_name", "Anonymous")
                                ),
                                "date": review.get(
                                    "date", review.get("relative_time_description", "")
                                ),
                                "source": "Google",
                            }
                        )

                # Fetch photos from SerpAPI Photos endpoint
                photos_data = self.serpapi_service.get_photos(business.data_id)
                if (
                    photos_data and not business.images
                ):  # Only if we don't already have images
                    business.images = []
                    for photo in photos_data[:10]:  # Limit to 10 photos
                        if isinstance(photo, dict):
                            business.images.append(
                                {
                                    "url": photo.get("thumbnail", photo.get("url", "")),
                                    "title": photo.get("title", ""),
                                    "source": "Google Photos",
                                }
                            )

            # Extract reviews from user_reviews section if available
            if not business.reviews:
                user_reviews = serpapi_data.get("user_reviews", {})
                most_relevant = user_reviews.get("most_relevant", [])
                business.reviews = []

                for review in most_relevant[:5]:  # Limit to first 5 reviews
                    if isinstance(review, dict):
                        business.reviews.append(
                            {
                                "rating": review.get("rating", 0),
                                "text": review.get("description", ""),
                                "author": review.get("username", "Anonymous"),
                                "date": review.get("date", ""),
                                "source": "Google",
                            }
                        )

            # Business hours
            hours = serpapi_data.get("hours", [])
            business.has_hours = len(hours) > 0
            if business.has_hours:
                business.business_hours = hours

            # Category/type
            types = serpapi_data.get("type", [])
            if types:
                business.category = types[0] if isinstance(types, list) else str(types)
            else:
                business.category = "Business"

            # Description
            business.description = self._extract_description(serpapi_data)
            business.has_description = bool(business.description)

            # Check for menu
            business.has_menu = self._has_menu_info(serpapi_data)
            if business.has_menu:
                # Look for menu URL in order_online_link or website
                business.menu_url = serpapi_data.get(
                    "order_online_link", business.website
                )

            # Extract service options from extensions
            service_options = serpapi_data.get("service_options", {})
            business.offers_delivery = service_options.get("delivery", False)
            business.offers_takeout = service_options.get("takeout", False)
            business.offers_dine_in = service_options.get("dine_in", False)

            # Extract additional business characteristics from extensions
            extensions = serpapi_data.get("extensions", [])
            business.accepts_reservations = False
            business.has_parking = False
            business.wheelchair_accessible = False
            business.has_wifi = False
            business.outdoor_seating = False
            business.accepts_credit_cards = False
            business.special_features = []
            business.popular_dishes = []

            for ext in extensions:
                if isinstance(ext, dict):
                    # Service options
                    if "service_options" in ext:
                        service_opts = ext["service_options"]
                        if "Takeout" in service_opts:
                            business.offers_takeout = True
                        if "Dine-in" in service_opts:
                            business.offers_dine_in = True
                        if "Delivery" in service_opts:
                            business.offers_delivery = True

                    # Accessibility
                    if "accessibility" in ext:
                        accessibility = ext["accessibility"]
                        if any("wheelchair" in item.lower() for item in accessibility):
                            business.wheelchair_accessible = True

                    # Amenities
                    if "amenities" in ext:
                        amenities = ext["amenities"]
                        if any("wi-fi" in item.lower() for item in amenities):
                            business.has_wifi = True
                        if any("parking" in item.lower() for item in amenities):
                            business.has_parking = True

                    # Payments
                    if "payments" in ext:
                        payments = ext["payments"]
                        if any("credit" in item.lower() for item in payments):
                            business.accepts_credit_cards = True

                    # Highlights as special features
                    if "highlights" in ext:
                        business.special_features = ext["highlights"]

                    # Offerings as popular dishes/items
                    if "offerings" in ext:
                        business.popular_dishes = ext["offerings"]

            # Price range
            price = serpapi_data.get("price", "")
            business.price_range = price if price else "$$"

            # Set default values for missing fields
            business.established_year = random.randint(2010, 2022)
            business.cuisine_type = ""

            # Determine cuisine type from category and offerings
            if business.category and "cafe" in business.category.lower():
                business.cuisine_type = "Coffee & Cafe"
            elif any(
                "restaurant" in cat.lower() for cat in types if isinstance(cat, str)
            ):
                business.cuisine_type = "Restaurant"

            # Set operational status
            open_state = serpapi_data.get("open_state", "")
            business.is_open = "open" in open_state.lower() if open_state else True
            business.temporarily_closed = (
                "closed" in open_state.lower() if open_state else False
            )

            # GPS coordinates for full address
            gps = serpapi_data.get("gps_coordinates", {})
            if gps:
                # Extract city, state, country from address
                address_parts = business.address.split(", ") if business.address else []
                if len(address_parts) >= 3:
                    business.city = address_parts[-2].split()[0]  # City
                    business.country = address_parts[-1]  # Country
                    business.postal_code = (
                        address_parts[-2].split()[-1]
                        if len(address_parts[-2].split()) > 1
                        else ""
                    )

        except Exception as e:
            logger.error(f"Error updating business from SerpAPI data: {str(e)}")
            # Log the specific data that caused the error for debugging
            logger.error(
                f"SerpAPI data keys: {list(serpapi_data.keys()) if isinstance(serpapi_data, dict) else 'Not a dict'}"
            )

    def _extract_description(self, serpapi_data: Dict[str, Any]) -> str:
        """Extract or generate description from SerpAPI data"""
        # First check if there's a direct description
        if serpapi_data.get("description"):
            return serpapi_data["description"]

        # Try to get description from popular highlights and offerings
        extensions = serpapi_data.get("extensions", [])
        highlights = []
        offerings = []
        popular_for = []

        for ext in extensions:
            if isinstance(ext, dict):
                if "highlights" in ext:
                    highlights.extend(ext["highlights"])
                if "offerings" in ext:
                    offerings.extend(ext["offerings"])
                if "popular_for" in ext:
                    popular_for.extend(ext["popular_for"])

        # Build description from available data
        description_parts = []

        if highlights:
            description_parts.append(f"Known for: {', '.join(highlights[:3])}")

        if popular_for:
            description_parts.append(f"Popular for: {', '.join(popular_for[:3])}")

        if offerings:
            description_parts.append(f"Offers: {', '.join(offerings[:3])}")

        if description_parts:
            return ". ".join(description_parts) + "."
        else:
            # Fallback description
            category = (
                serpapi_data.get("type", ["business"])[0]
                if serpapi_data.get("type")
                else "business"
            )
            return f"A {category.lower()} serving customers in the local area."

    def _has_menu_info(self, serpapi_data: Dict[str, Any]) -> bool:
        """Check if business has menu information"""
        images = serpapi_data.get("images", [])

        # Check if any image is labeled as menu
        for image in images:
            if image.get("title", "").lower() in ["menu", "food & drink"]:
                return True

        # Check extensions for menu-related info
        extensions = serpapi_data.get("extensions", [])
        for ext in extensions:
            if "offerings" in ext:
                offerings = ext["offerings"]
                menu_keywords = [
                    "menu",
                    "food",
                    "drinks",
                    "coffee",
                    "breakfast",
                    "lunch",
                    "dinner",
                ]
                if any(
                    keyword in " ".join(offerings).lower() for keyword in menu_keywords
                ):
                    return True

        return False

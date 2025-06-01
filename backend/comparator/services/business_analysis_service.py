import logging
from typing import Dict, Any
from .business_service import BusinessService
from .ai_service import AIService
from .scoring_service import ScoringService
from .comparison_service import ComparisonService


logger = logging.getLogger(__name__)


class BusinessAnalysisService:
    """Main orchestrator service for business analysis operations"""

    def __init__(self):
        self.business_service = BusinessService()
        self.ai_service = AIService()
        self.scoring_service = ScoringService()
        self.comparison_service = ComparisonService()

    def analyze_business(
        self, business_name: str, website: str = None
    ) -> Dict[str, Any]:
        """
        Analyze a single business and provide insights
        Returns: Business profile data with AI-generated suggestions
        """
        # Get or create business profile with real data
        business = self.business_service.get_or_create_business(business_name, website)

        # Calculate business score
        score = self.scoring_service.calculate_business_score(business)

        # Prepare business data for AI analysis
        business_data = self._prepare_business_data(business, score)

        # Generate analysis insights
        insights = self.ai_service.generate_business_insights(business_data)

        return {
            "business": self.business_service.format_business_data(business),
            "analysis": insights,
            "score": score,
        }

    def compare_businesses(
        self,
        your_business: str,
        your_website: str,
        competitor_business: str,
        competitor_website: str = None,
    ):
        """Compare two businesses and provide detailed analysis"""
        return self.comparison_service.compare_businesses(
            your_business, your_website, competitor_business, competitor_website
        )

    def find_competitors(
        self, business_name: str, location: str = None, limit: int = 5
    ) -> Dict[str, Any]:
        """
        Find potential competitors for a given business
        This is a placeholder implementation for future development
        """
        # TODO: Implement competitor finding using SerpAPI local search
        # This could search for similar businesses in the same area/category
        return {
            "business_name": business_name,
            "location": location,
            "competitors": [],
            "message": "Competitor finding functionality not yet implemented. Please specify competitors manually.",
            "suggestions": [
                "Use Google Maps to search for similar businesses in your area",
                "Look for businesses with similar categories or services",
                "Check local business directories for competitors",
            ],
        }

    def _prepare_business_data(self, business, score: float) -> Dict[str, Any]:
        """Prepare business data for AI analysis"""
        return {
            # Basic Information
            "name": business.name,
            "category": business.category,
            "cuisine_type": business.cuisine_type,
            "price_range": business.price_range,
            "established_year": business.established_year,
            # Contact & Location
            "has_phone": bool(business.phone),
            "has_email": bool(business.email),
            "has_address": bool(business.address),
            "city": business.city,
            "state": business.state,
            "website": business.website,
            # Business Operations
            "is_open": business.is_open,
            "temporarily_closed": business.temporarily_closed,
            "has_hours": business.has_hours,
            "has_business_hours": bool(business.business_hours),
            # Service Options
            "offers_delivery": business.offers_delivery,
            "offers_takeout": business.offers_takeout,
            "offers_dine_in": business.offers_dine_in,
            "accepts_reservations": business.accepts_reservations,
            "service_options_count": len(business.service_options_summary),
            # Review Metrics
            "review_count": business.review_count,
            "google_reviews": business.google_reviews,
            "yelp_reviews": business.yelp_reviews,
            "total_reviews": business.total_reviews,
            "average_rating": float(business.average_rating),
            # Content Metrics
            "image_count": business.image_count,
            "has_description": business.has_description,
            "has_menu": business.has_menu,
            "has_menu_url": bool(business.menu_url),
            # Features & Amenities
            "has_parking": business.has_parking,
            "wheelchair_accessible": business.wheelchair_accessible,
            "has_wifi": business.has_wifi,
            "accepts_credit_cards": business.accepts_credit_cards,
            "outdoor_seating": business.outdoor_seating,
            "special_features_count": len(business.special_features),
            "popular_dishes_count": len(business.popular_dishes),
            # Online Presence
            "has_social_media": any(
                [business.facebook_url, business.instagram_url, business.twitter_url]
            ),
            "social_media_count": sum(
                [
                    bool(business.facebook_url),
                    bool(business.instagram_url),
                    bool(business.twitter_url),
                ]
            ),
            # Overall Score
            "score": score,
        }

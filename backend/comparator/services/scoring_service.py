from typing import TYPE_CHECKING
from .config import SCORE_WEIGHTS

if TYPE_CHECKING:
    from ..models import BusinessProfile


class ScoringService:
    """Service for calculating business scores and metrics"""

    def calculate_business_score(self, business: "BusinessProfile") -> float:
        """Calculate a 0-100 score for the business based on completeness and performance"""
        score = 0.0

        # Review metrics (40% of score)
        score += self._calculate_review_score(business)

        # Content completeness (40% of score)
        score += self._calculate_content_score(business)

        # Image count (20% of score)
        score += self._calculate_image_score(business)

        return round(min(100, max(0, score)), 1)

    def _calculate_review_score(self, business: "BusinessProfile") -> float:
        """Calculate score based on reviews and ratings"""
        max_review_score = SCORE_WEIGHTS["reviews"] * 100

        total_reviews = business.total_reviews
        if total_reviews <= 0:
            return 0.0

        # Review count component (half of review score)
        review_count_score = min(
            max_review_score / 2, (total_reviews / 100) * (max_review_score / 2)
        )

        # Rating component (half of review score)
        rating_score = (float(business.average_rating) / 5.0) * (max_review_score / 2)

        return review_count_score + rating_score

    def _calculate_content_score(self, business: "BusinessProfile") -> float:
        """Calculate score based on content completeness"""
        max_content_score = SCORE_WEIGHTS["content"] * 100

        # Basic information completeness
        basic_info_items = [
            bool(business.phone),
            bool(business.email),
            bool(business.address),
            bool(business.city),
            bool(business.state),
            bool(business.website),
            bool(business.description),
            bool(business.category),
        ]

        # Business operations completeness
        operations_items = [
            business.has_hours,
            business.is_open,
            bool(business.business_hours),
            bool(business.established_year),
        ]

        # Content and menu completeness
        content_items = [
            business.has_description,
            business.has_menu,
            business.image_count > 10,
            (
                bool(business.menu_url) if business.has_menu else True
            ),  # Bonus for menu URL
        ]

        # Service options completeness
        service_items = [
            business.offers_dine_in
            or business.offers_takeout
            or business.offers_delivery,
            bool(business.price_range),
            bool(business.cuisine_type),
        ]

        # Features and amenities (bonus points)
        feature_items = [
            business.has_parking,
            business.wheelchair_accessible,
            business.has_wifi,
            business.accepts_credit_cards,
            len(business.special_features) > 0,
            len(business.popular_dishes) > 0,
        ]

        # Online presence (bonus points)
        online_presence_items = [
            bool(business.facebook_url),
            bool(business.instagram_url),
            bool(business.twitter_url),
        ]

        # Calculate weighted completeness
        basic_score = (sum(basic_info_items) / len(basic_info_items)) * 0.4
        operations_score = (sum(operations_items) / len(operations_items)) * 0.3
        content_score = (sum(content_items) / len(content_items)) * 0.2
        service_score = (sum(service_items) / len(service_items)) * 0.1

        # Bonus points for features and online presence (up to 10% extra)
        feature_bonus = (sum(feature_items) / len(feature_items)) * 0.05
        online_bonus = (sum(online_presence_items) / len(online_presence_items)) * 0.05

        total_completeness = (
            basic_score
            + operations_score
            + content_score
            + service_score
            + feature_bonus
            + online_bonus
        )

        return min(total_completeness, 1.0) * max_content_score

    def _calculate_image_score(self, business: "BusinessProfile") -> float:
        """Calculate score based on image count"""
        max_image_score = SCORE_WEIGHTS["images"] * 100
        return min(max_image_score, (business.image_count / 30) * max_image_score)

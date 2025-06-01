from django.db import models
from django.utils import timezone


class BusinessProfile(models.Model):
    """Enhanced business profile model with comprehensive business data"""

    # Basic Information
    name = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, default="Restaurant")
    established_year = models.IntegerField(
        blank=True, null=True, help_text="Year the business was established"
    )

    # Contact Information
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    # Location Details
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=50, default="United States")

    # Business Operations
    business_hours = models.JSONField(
        blank=True, default=dict, help_text="Operating hours for each day"
    )
    is_open = models.BooleanField(
        default=True, help_text="Whether the business is currently operating"
    )
    temporarily_closed = models.BooleanField(default=False)

    # Business Characteristics
    PRICE_RANGE_CHOICES = [
        ("$", "Budget-friendly"),
        ("$$", "Moderate"),
        ("$$$", "Upscale"),
        ("$$$$", "High-end"),
    ]
    price_range = models.CharField(
        max_length=4, choices=PRICE_RANGE_CHOICES, blank=True, null=True
    )
    cuisine_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Type of cuisine or service offered",
    )

    # Service Options
    offers_delivery = models.BooleanField(default=False)
    offers_takeout = models.BooleanField(default=False)
    offers_dine_in = models.BooleanField(default=False)
    accepts_reservations = models.BooleanField(default=False)

    # Online Presence
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)

    # Review Metrics
    review_count = models.IntegerField(default=0)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    google_reviews = models.IntegerField(default=0)
    yelp_reviews = models.IntegerField(default=0)

    # Content Metrics
    image_count = models.IntegerField(default=0)
    has_hours = models.BooleanField(default=False)
    has_description = models.BooleanField(default=False)
    has_menu = models.BooleanField(default=False)
    menu_url = models.URLField(blank=True, null=True)

    # Images & Reviews Data
    images = models.JSONField(
        blank=True, default=list, help_text="List of image URLs from SerpAPI"
    )
    reviews = models.JSONField(
        blank=True, default=list, help_text="List of reviews from SerpAPI"
    )

    # SerpAPI Data
    data_id = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="SerpAPI data ID for fetching additional data",
    )

    # Business Features & Amenities
    has_parking = models.BooleanField(default=False)
    wheelchair_accessible = models.BooleanField(default=False)
    has_wifi = models.BooleanField(default=False)
    accepts_credit_cards = models.BooleanField(default=True)
    outdoor_seating = models.BooleanField(default=False)

    # Additional Features
    special_features = models.JSONField(
        blank=True, default=list, help_text="List of special features or amenities"
    )
    popular_dishes = models.JSONField(
        blank=True, default=list, help_text="List of popular dishes or services"
    )

    # Timestamps
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def full_address(self):
        """Return formatted full address"""
        parts = [self.address, self.city, self.state, self.postal_code]
        return ", ".join(filter(None, parts))

    @property
    def total_reviews(self):
        """Return total reviews across all platforms"""
        return self.google_reviews + self.yelp_reviews + self.review_count

    @property
    def service_options_summary(self):
        """Return a summary of available service options"""
        options = []
        if self.offers_dine_in:
            options.append("Dine-in")
        if self.offers_takeout:
            options.append("Takeout")
        if self.offers_delivery:
            options.append("Delivery")
        return options

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Business Profile"
        verbose_name_plural = "Business Profiles"

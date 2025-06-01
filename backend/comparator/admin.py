from django.contrib import admin
from .models import BusinessProfile


@admin.register(BusinessProfile)
class BusinessProfileAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "category",
        "city",
        "state",
        "price_range",
        "total_reviews",
        "average_rating",
        "is_open",
        "created_at",
    ]
    list_filter = [
        "category",
        "price_range",
        "is_open",
        "temporarily_closed",
        "offers_delivery",
        "offers_takeout",
        "offers_dine_in",
        "has_parking",
        "wheelchair_accessible",
        "state",
        "created_at",
    ]
    search_fields = ["name", "address", "city", "website", "phone", "email"]
    readonly_fields = ["created_at", "updated_at", "total_reviews", "full_address"]

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "name",
                    "category",
                    "description",
                    "established_year",
                    "cuisine_type",
                    "price_range",
                )
            },
        ),
        (
            "Contact Information",
            {
                "fields": (
                    "phone",
                    "email",
                    "website",
                )
            },
        ),
        (
            "Location",
            {
                "fields": (
                    "address",
                    "city",
                    "state",
                    "postal_code",
                    "country",
                    "full_address",
                )
            },
        ),
        (
            "Business Operations",
            {
                "fields": (
                    "is_open",
                    "temporarily_closed",
                    "business_hours",
                    "has_hours",
                )
            },
        ),
        (
            "Service Options",
            {
                "fields": (
                    "offers_dine_in",
                    "offers_takeout",
                    "offers_delivery",
                    "accepts_reservations",
                )
            },
        ),
        (
            "Review Metrics",
            {
                "fields": (
                    "review_count",
                    "google_reviews",
                    "yelp_reviews",
                    "total_reviews",
                    "average_rating",
                )
            },
        ),
        (
            "Content & Menu",
            {
                "fields": (
                    "image_count",
                    "has_description",
                    "has_menu",
                    "menu_url",
                )
            },
        ),
        (
            "Features & Amenities",
            {
                "fields": (
                    "has_parking",
                    "wheelchair_accessible",
                    "has_wifi",
                    "accepts_credit_cards",
                    "outdoor_seating",
                    "special_features",
                    "popular_dishes",
                )
            },
        ),
        (
            "Social Media",
            {
                "fields": (
                    "facebook_url",
                    "instagram_url",
                    "twitter_url",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Timestamps",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )

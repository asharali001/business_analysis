from django.urls import path
from . import views

app_name = "comparator"

urlpatterns = [
    # Core business analysis APIs
    path("analyze/", views.analyze_business, name="analyze_business"),
    path("compare/", views.compare_businesses, name="compare_businesses"),
]

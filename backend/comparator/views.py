from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .services import BusinessAnalysisService


@api_view(["POST"])
def analyze_business(request):
    """
    Analyze a business profile and provide insights

    POST /api/analyze/
    {
        "business_name": "My Restaurant",
    }
    """
    business_name = request.data.get("business_name")
    website = request.data.get("website")

    if not business_name:
        return Response(
            {"error": "business_name is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        service = BusinessAnalysisService()
        analysis = service.analyze_business(business_name, website)
        return Response(analysis, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"error": f"Analysis failed: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["POST"])
def compare_businesses(request):
    """
    Compare your business with a competitor

    POST /api/compare/
    {
        "your_business": "My Restaurant",
        "competitor_business": "Competitor Restaurant",
    }
    """
    your_business = request.data.get("your_business")
    your_website = request.data.get("your_website")
    competitor_business = request.data.get("competitor_business")
    competitor_website = request.data.get("competitor_website")

    if not your_business or not competitor_business:
        return Response(
            {"error": "your_business and competitor_business are required"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        service = BusinessAnalysisService()
        comparison = service.compare_businesses(
            your_business, your_website, competitor_business, competitor_website
        )
        return Response(comparison, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {"error": f"Comparison failed: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

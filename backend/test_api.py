#!/usr/bin/env python
"""
Simple test script for the 3 core business analysis APIs
"""
import os
import sys
import django
import json

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "competitor_insights.settings")
django.setup()

from comparator.services import BusinessAnalysisService


def test_analyze_business():
    """Test the business analysis API"""
    print("Testing Business Analysis API...")
    service = BusinessAnalysisService()

    result = service.analyze_business("Mario's Pizza", "https://mariospizza.com")

    print("✓ Business Analysis Result:")
    print(f"  Business: {result['business']['name']}")
    print(f"  Score: {result['score']}/100")
    print(f"  Suggestions: {len(result['analysis']['suggestions'])}")
    print()


def test_compare_businesses():
    """Test the business comparison API"""
    print("Testing Business Comparison API...")
    service = BusinessAnalysisService()

    result = service.compare_businesses(
        "Mario's Pizza",
        "https://mariospizza.com",
        "Luigi's Italian Kitchen",
        "https://luigis.com",
    )

    print("✓ Business Comparison Result:")
    print(
        f"  Your Business: {result['your_business']['name']} (Score: {result['your_score']})"
    )
    print(
        f"  Competitor: {result['competitor']['name']} (Score: {result['competitor_score']})"
    )
    print(f"  Suggestions: {len(result['comparison']['suggestions'])}")
    print(f"  Strengths: {len(result['comparison']['strengths'])}")
    print()


if __name__ == "__main__":
    print("🚀 Testing Simplified Business Analysis APIs\n")

    try:
        test_analyze_business()
        test_compare_businesses()

        print("✅ All tests passed! The simplified APIs are working correctly.")

    except Exception as e:
        print(f"❌ Test failed: {e}")
        sys.exit(1)

import requests
import logging
from typing import Optional, Dict, Any, List
from .config import SERPAPI_API_KEY, SERPAPI_BASE_URL, REQUEST_TIMEOUT

logger = logging.getLogger(__name__)


class SerpAPIService:
    """Service for handling SerpAPI interactions"""

    def __init__(self):
        self.api_key = SERPAPI_API_KEY
        self.base_url = SERPAPI_BASE_URL

    def search_business(self, business_name: str) -> Optional[Dict[str, Any]]:
        """Search for a business using Google Maps"""
        try:
            params = {
                "engine": "google_maps",
                "q": business_name,
                "api_key": self.api_key,
                "type": "search",
            }

            response = requests.get(
                self.base_url, params=params, timeout=REQUEST_TIMEOUT
            )
            response.raise_for_status()

            data = response.json()

            # Get the first place result if available

            if "place_results" in data:
                return data["place_results"]
            elif "local_results" in data:
                # If no place_results, try the first local result
                first_place = data["local_results"][0]
                return self.get_place_details(first_place.get("place_id"))

            return None

        except Exception as e:
            logger.error(f"Error searching business {business_name}: {str(e)}")
            return None

    def get_place_details(self, place_id: str) -> Optional[Dict[str, Any]]:
        """Get detailed place information using place_id"""
        if not place_id:
            return None

        try:
            params = {
                "engine": "google_maps",
                "place_id": place_id,
                "api_key": self.api_key,
            }

            response = requests.get(
                self.base_url, params=params, timeout=REQUEST_TIMEOUT
            )
            response.raise_for_status()

            data = response.json()
            return data.get("place_results")

        except Exception as e:
            logger.error(f"Error fetching place details for {place_id}: {str(e)}")
            return None

    def get_reviews(self, data_id: str, num_reviews: int = 5) -> list:
        """Get reviews for a place using data_id"""
        if not data_id:
            return []

        try:
            params = {
                "engine": "google_maps_reviews",
                "data_id": data_id,
                "api_key": self.api_key,
                "num": min(num_reviews, 5),  # Limit to 5 reviews max
            }

            response = requests.get(
                self.base_url, params=params, timeout=REQUEST_TIMEOUT
            )
            response.raise_for_status()

            data = response.json()
            return data.get("reviews", [])

        except Exception as e:
            logger.error(f"Error fetching reviews for data_id {data_id}: {str(e)}")
            return []

    def get_photos(self, data_id: str) -> list:
        """Get photos for a place using data_id"""
        if not data_id:
            return []

        try:
            params = {
                "engine": "google_maps_photos",
                "data_id": data_id,
                "api_key": self.api_key,
            }

            response = requests.get(
                self.base_url, params=params, timeout=REQUEST_TIMEOUT
            )
            response.raise_for_status()

            data = response.json()
            return data.get("photos", [])

        except Exception as e:
            logger.error(f"Error fetching photos for data_id {data_id}: {str(e)}")
            return []

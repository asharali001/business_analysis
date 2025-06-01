import logging
from django.conf import settings

# Initialize logger
logger = logging.getLogger(__name__)

# OpenAI Configuration
OPENAI_API_KEY = getattr(settings, "OPENAI_API_KEY", None)
OPENAI_MODEL = getattr(settings, "OPENAI_MODEL", "gpt-4o-mini")

# SerpAPI Configuration
SERPAPI_API_KEY = getattr(
    settings,
    "SERPAPI_KEY",
    "6bf299ca887c6e81ce088e384fb1de8fcf4c2a961e3a0d990b427ad64b0b7d8b",
)
SERPAPI_BASE_URL = "https://serpapi.com/search"

# Business Analysis Configuration
DEFAULT_COMPETITOR_COUNT = 3
REQUEST_TIMEOUT = 10
MAX_SUGGESTIONS = 5
MAX_STRENGTHS = 5

# Scoring weights
SCORE_WEIGHTS = {
    "reviews": 0.4,  # 40% of score
    "content": 0.4,  # 40% of score
    "images": 0.2,  # 20% of score
}

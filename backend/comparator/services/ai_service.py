import json
import logging
from typing import Dict, Any, Optional
from openai import OpenAI
from .config import OPENAI_API_KEY, OPENAI_MODEL, MAX_SUGGESTIONS

logger = logging.getLogger(__name__)


class AIService:
    """Service for AI-powered insights and analysis"""

    def __init__(self):
        self.client = self._initialize_client()

    def _initialize_client(self) -> Optional[OpenAI]:
        """Initialize OpenAI client with error handling"""
        try:
            if OPENAI_API_KEY:
                return OpenAI(api_key=OPENAI_API_KEY)
            else:
                logger.warning(
                    "OpenAI API key not configured. Using fallback analysis methods."
                )
                return None
        except Exception as e:
            logger.error(f"Failed to initialize OpenAI client: {str(e)}")
            return None

    def generate_business_insights(
        self, business_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Generate AI-powered insights for a single business"""
        if not self.client:
            return self._generate_fallback_insights(business_data)

        try:
            prompt = self._build_business_analysis_prompt(business_data)

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a business consultant expert in online presence optimization and customer acquisition.",
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
                max_tokens=500,
            )

            # Parse AI response
            json_content = self._extract_json_from_response(
                response.choices[0].message.content
            )
            ai_response = json.loads(json_content)

            return {
                "summary": ai_response.get(
                    "summary", f"{business_data['name']} analysis completed."
                ),
                "suggestions": ai_response.get("suggestions", [])[:MAX_SUGGESTIONS],
            }

        except Exception as e:
            logger.error(f"Error generating AI insights: {str(e)}")
            return self._generate_fallback_insights(business_data)

    def generate_comparison_insights(
        self, your_business: Dict[str, Any], competitor: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Generate AI-powered comparison insights between two businesses"""
        if not self.client:
            return self._generate_fallback_comparison(your_business, competitor)

        try:
            prompt = self._build_comparison_prompt(your_business, competitor)

            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a competitive business analyst expert in market positioning and competitive strategy.",
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
                max_tokens=600,
            )

            # Parse AI response
            json_content = self._extract_json_from_response(
                response.choices[0].message.content
            )
            ai_response = json.loads(json_content)

            return {
                "summary": ai_response.get(
                    "summary",
                    f"Comparison between {your_business['name']} and {competitor['name']}.",
                ),
                "suggestions": ai_response.get("suggestions", [])[:MAX_SUGGESTIONS],
                "strengths": ai_response.get("strengths", []),
            }

        except Exception as e:
            logger.error(f"Error generating comparison insights: {str(e)}")
            return self._generate_fallback_comparison(your_business, competitor)

    def _build_business_analysis_prompt(self, business_data: Dict[str, Any]) -> str:
        """Build prompt for business analysis"""
        return f"""
        You are a business consultant analyzing an online business profile. Provide actionable insights and suggestions.
        
        Business Data:
        - Name: {business_data['name']}
        - Category: {business_data['category']}
        - Reviews: {business_data['review_count']} reviews
        - Rating: {business_data['average_rating']}/5 stars
        - Photos: {business_data['image_count']} images
        - Has business hours: {business_data['has_hours']}
        - Has description: {business_data['has_description']}
        - Has menu: {business_data['has_menu']}
        - Has phone number: {business_data['has_phone']}
        - Has address: {business_data['has_address']}
        - Website: {business_data['website']}
        - Current Profile Score: {business_data['score']}/100
        
        Please provide:
        1. A brief 1-2 sentence summary of the business's online presence
        2. 3-5 specific, actionable suggestions to improve their online presence and attract more customers
        
        Focus on practical improvements that would have the most impact on customer acquisition and retention.
        Be specific and avoid generic advice.
        
        Respond in JSON format:
        {{
            "summary": "Brief summary here",
            "suggestions": ["Suggestion 1", "Suggestion 2", "Suggestion 3"]
        }}
        """

    def _build_comparison_prompt(
        self, your_business: Dict[str, Any], competitor: Dict[str, Any]
    ) -> str:
        """Build prompt for business comparison"""
        return f"""
        You are a competitive business analyst. Compare these two businesses and provide strategic insights.
        
        Your Business:
        - Name: {your_business['name']}
        - Reviews: {your_business['review_count']} ({your_business['average_rating']}/5 stars)
        - Photos: {your_business['image_count']}
        - Complete info (hours/description/menu): {your_business['has_hours']}/{your_business['has_description']}/{your_business['has_menu']}
        - Profile Score: {your_business['score']}/100
        
        Competitor:
        - Name: {competitor['name']}
        - Reviews: {competitor['review_count']} ({competitor['average_rating']}/5 stars)
        - Photos: {competitor['image_count']}
        - Complete info (hours/description/menu): {competitor['has_hours']}/{competitor['has_description']}/{competitor['has_menu']}
        - Profile Score: {competitor['score']}/100
        
        Provide:
        1. A summary comparing the two businesses
        2. Specific areas where your business is stronger than the competitor
        3. 3-5 actionable suggestions to gain competitive advantage
        
        Focus on data-driven insights and specific recommendations.
        
        Respond in JSON format:
        {{
            "summary": "Competitive analysis summary",
            "strengths": ["Strength 1", "Strength 2"],
            "suggestions": ["Suggestion 1", "Suggestion 2", "Suggestion 3"]
        }}
        """

    def _extract_json_from_response(self, content: str) -> str:
        """Extract JSON content from markdown code blocks"""
        try:
            if content.strip().startswith("```"):
                lines = content.strip().split("\n")
                start_idx = 0
                end_idx = len(lines)

                # Find JSON content boundaries
                for i, line in enumerate(lines):
                    if line.strip().startswith("```"):
                        start_idx = i + 1
                        break

                for i in range(len(lines) - 1, -1, -1):
                    if lines[i].strip() == "```":
                        end_idx = i
                        break

                json_content = "\n".join(lines[start_idx:end_idx])
                return json_content.strip()
            else:
                return content.strip()
        except Exception:
            return content.strip()

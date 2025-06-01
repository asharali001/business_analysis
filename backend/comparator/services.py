# Legacy import for backward compatibility
# The main business logic has been refactored into modular services
from .services.business_analysis_service import BusinessAnalysisService

# Export for backward compatibility
__all__ = ["BusinessAnalysisService"]

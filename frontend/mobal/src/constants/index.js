/**
 * Application Constants
 * Centralized configuration and magic values
 */

// API Configuration
export const API_CONFIG = {
  BASE_URL: 'http://localhost:8000/api/',
  TIMEOUT: 30000,
  ENDPOINTS: {
    ANALYZE: 'analyze/',
    COMPETITORS: 'competitors/',
    COMPARE: 'compare/'
  }
}

// Business Analysis Constants
export const BUSINESS_ANALYSIS = {
  DEFAULT_COMPETITOR_COUNT: 3,
  MIN_RATING: 0,
  MAX_RATING: 5,
  SCORE_RANGES: {
    EXCELLENT: 90,
    GOOD: 70,
    AVERAGE: 50,
    POOR: 30
  }
}

// Review Analysis Thresholds
export const REVIEW_THRESHOLDS = {
  EXCELLENT_VOLUME: 100,
  GOOD_VOLUME: 50,
  MODERATE_VOLUME: 20,
  LOW_VOLUME: 10,
  EXCELLENT_RATING: 4.5,
  GOOD_RATING: 4.0,
  AVERAGE_RATING: 3.5,
  POOR_RATING: 3.0
}

// UI Constants
export const UI_CONSTANTS = {
  MAX_IMAGES_DISPLAY: 12,
  MAX_REVIEWS_DISPLAY: 10
}

// Error Messages
export const ERROR_MESSAGES = {
  NETWORK_ERROR: 'Unable to connect to the server. Please check your internet connection.',
  INVALID_REQUEST: 'Invalid request. Please check your input.',
  SERVER_ERROR: 'Server error occurred. Please try again.',
  GENERIC_ERROR: 'An unexpected error occurred.',
  NO_DATA: 'No analysis data available. Please try again.',
  COMPARISON_FAILED: 'Failed to compare with this business. Please try again.'
}

// Business Profile Fields (for completion calculation)
export const BUSINESS_FIELDS = [
  'phone',
  'email', 
  'website',
  'has_hours',
  'has_description',
  'has_menu',
  'address'
] 
/**
 * Utility Functions
 * Common helper functions used throughout the application
 */

import { BUSINESS_FIELDS, REVIEW_THRESHOLDS } from '../constants'

/**
 * Calculate business profile completion percentage
 * @param {Object} business - Business object
 * @returns {number} Completion percentage (0-100)
 */
export function calculateCompletionPercentage(business) {
  if (!business) return 0
  
  const completedFields = BUSINESS_FIELDS.filter(field => business[field]).length
  return Math.round((completedFields / BUSINESS_FIELDS.length) * 100)
}

/**
 * Get review volume analysis text
 * @param {number} reviewCount - Number of reviews
 * @returns {string} Analysis text
 */
export function getReviewVolumeAnalysis(reviewCount) {
  if (reviewCount >= REVIEW_THRESHOLDS.EXCELLENT_VOLUME) return 'Excellent volume'
  if (reviewCount >= REVIEW_THRESHOLDS.GOOD_VOLUME) return 'Good volume'
  if (reviewCount >= REVIEW_THRESHOLDS.MODERATE_VOLUME) return 'Moderate volume'
  if (reviewCount >= REVIEW_THRESHOLDS.LOW_VOLUME) return 'Low volume'
  return 'Very few reviews'
}

/**
 * Get rating quality text
 * @param {number} rating - Average rating
 * @returns {string} Quality description
 */
export function getRatingQualityText(rating) {
  if (rating >= REVIEW_THRESHOLDS.EXCELLENT_RATING) return 'Excellent (4.5+)'
  if (rating >= REVIEW_THRESHOLDS.GOOD_RATING) return 'Very Good (4.0+)'
  if (rating >= REVIEW_THRESHOLDS.AVERAGE_RATING) return 'Good (3.5+)'
  if (rating >= REVIEW_THRESHOLDS.POOR_RATING) return 'Average (3.0+)'
  return 'Below Average'
}

/**
 * Get rating quality CSS class
 * @param {number} rating - Average rating
 * @returns {string} CSS class
 */
export function getRatingQualityClass(rating) {
  if (rating >= REVIEW_THRESHOLDS.EXCELLENT_RATING) return 'text-green-600 font-medium'
  if (rating >= REVIEW_THRESHOLDS.GOOD_RATING) return 'text-green-500 font-medium'
  if (rating >= REVIEW_THRESHOLDS.AVERAGE_RATING) return 'text-yellow-600 font-medium'
  if (rating >= REVIEW_THRESHOLDS.POOR_RATING) return 'text-orange-600 font-medium'
  return 'text-red-600 font-medium'
}

/**
 * Get review volume CSS class
 * @param {number} count - Review count
 * @returns {string} CSS class
 */
export function getReviewVolumeClass(count) {
  if (count >= REVIEW_THRESHOLDS.EXCELLENT_VOLUME) return 'text-green-600 font-medium'
  if (count >= REVIEW_THRESHOLDS.GOOD_VOLUME) return 'text-green-500 font-medium'
  if (count >= REVIEW_THRESHOLDS.MODERATE_VOLUME) return 'text-yellow-600 font-medium'
  if (count >= REVIEW_THRESHOLDS.LOW_VOLUME) return 'text-orange-600 font-medium'
  return 'text-red-600 font-medium'
}

/**
 * Format review date to readable string
 * @param {string} dateString - Date string
 * @returns {string} Formatted date
 */
export function formatReviewDate(dateString) {
  if (!dateString) return ''
  
  try {
    const date = new Date(dateString)
    if (isNaN(date.getTime())) return dateString
    
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    })
  } catch {
    return dateString
  }
}

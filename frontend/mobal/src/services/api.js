import axios from 'axios'
import { API_CONFIG, ERROR_MESSAGES, BUSINESS_ANALYSIS } from '../constants'

// Create axios instance with default config
const api = axios.create({
  baseURL: API_CONFIG.BASE_URL,
  timeout: API_CONFIG.TIMEOUT,
  headers: {
    'Content-Type': 'application/json',
  }
})

// Enhanced error handling function
function handleApiError(error) {
  console.error('❌ API Error:', error)
  
  if (error.response) {
    const status = error.response.status
    const data = error.response.data
    
    switch (status) {
      case 400:
        throw new Error(data.error || ERROR_MESSAGES.INVALID_REQUEST)
      case 500:
        throw new Error(data.error || ERROR_MESSAGES.SERVER_ERROR)
      default:
        throw new Error(data.error || `Server returned error ${status}`)
    }
  } else if (error.request) {
    throw new Error(ERROR_MESSAGES.NETWORK_ERROR)
  } else {
    throw new Error(error.message || ERROR_MESSAGES.GENERIC_ERROR)
  }
}

/**
 * Main workflow function - performs complete competitor analysis
 * @param {string} businessName - Name of the business to analyze
 * @returns {Promise<Object>} Analysis results
 */
export const performBusinessAnalysis = async (
  businessName
) => {
  try {
    console.log('🔍 Starting business analysis for:', businessName)
    
    // Step 1: Analyze the target business
    const analyzePayload = {
      business_name: businessName
    }
    
    
    const businessAnalysis = await api.post(API_CONFIG.ENDPOINTS.ANALYZE, analyzePayload)
    console.log('✅ Business analysis completed:', businessAnalysis.data)
    
   
    
    // Prepare the result in the format expected by the frontend
    return {
      target_business: businessAnalysis.data.business,
      competitors: [],
      analysis: businessAnalysis.data.analysis,
      score: businessAnalysis.data.score,
      summary: businessAnalysis.data.analysis.summary,
      suggestions: businessAnalysis.data.analysis.suggestions
    }
    
  } catch (error) {
    handleApiError(error)
  }
}

/**
 * Perform detailed comparison between two specific businesses
 * @param {string} yourBusiness - Your business name
 * @param {string} competitorBusiness - Competitor business name
 * @returns {Promise<Object>} Comparison results
 */
export const performBusinessComparison = async (
  yourBusiness,
  competitorBusiness, 
) => {
  try {
    console.log('🔍 Starting detailed comparison between:', yourBusiness, 'vs', competitorBusiness)
    
    const payload = {
      your_business: yourBusiness,
      competitor_business: competitorBusiness
    }
    
    const comparison = await api.post(API_CONFIG.ENDPOINTS.COMPARE, payload)
    console.log('✅ Business comparison completed:', comparison.data)
    
    return {
      your_business: comparison.data.your_business,
      competitor: comparison.data.competitor,
      comparison: comparison.data.comparison,
      your_score: comparison.data.your_score,
      competitor_score: comparison.data.competitor_score
    }
    
  } catch (error) {
    handleApiError(error)
  }
}

export default api 
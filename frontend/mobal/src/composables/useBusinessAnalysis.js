/**
 * Business Analysis Composable
 * Handles business analysis workflow and state management
 */

import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useBusinessStore } from '../stores/business'
import { performBusinessAnalysis, performBusinessComparison } from '../services/api'
import { ERROR_MESSAGES } from '../constants'

export function useBusinessAnalysis() {
  const router = useRouter()
  const store = useBusinessStore()
  const isProcessing = ref(false)

  /**
   * Handle competitor analysis workflow
   * @param {Object} searchData - Search form data
   */
  async function handleAnalysis(searchData) {
    try {
      store.clearError()
      isProcessing.value = true
      store.setLoading(true)
      
      // Store search query for reference
      store.setSearchQuery(searchData)
      
      console.log('🚀 Starting analysis workflow...', searchData)
      
      
      // Check if user provided competitors
      const hasCompetitors = searchData.competitors && searchData.competitors.length > 0
      
      if (hasCompetitors) {
        await handleCompetitorComparison(searchData.business, searchData.competitors)
      } else {
        await handleBusinessAnalysis(searchData.business)
      }
      
      // Navigate to results page
      router.push('/results')
      
    } catch (err) {
      console.error('❌ Analysis failed:', err)
      handleAnalysisError(err)
    } finally {
      isProcessing.value = false
      store.setLoading(false)
    }
  }

  /**
   * Handle business analysis only (no competitors)
   * @param {string} businessName - Business name
   * @param {string} website - Business website
   */
  async function handleBusinessAnalysis(businessName) {
    console.log('📈 Running business analysis only')
    
    const result = await performBusinessAnalysis(
      businessName
    )
    
    console.log('✅ Business analysis completed:', result)
    
    // Store analysis results
    store.setComparison({
      type: 'analysis',
      target_business: result.target_business,
      competitors: result.competitors,
      analysis: result.analysis,
      summary: result.summary,
      score: result.score
    })
  }

  /**
   * Handle competitor comparison workflow
   * @param {string} businessName - Business name
   * @param {string} website - Business website
   * @param {Array} competitors - List of competitors
   */
  async function handleCompetitorComparison(businessName, competitors) {
    console.log('📊 Running competitor comparison analysis')
    
    // For now, compare with the first competitor provided
    const competitorName = competitors[0]
    
    const comparison = await performBusinessComparison(
      businessName,
      competitorName,
    )
    
    console.log('✅ Competitor comparison completed:', comparison)
    
    // Store comparison results
    store.setComparison({
      type: 'comparison',
      your_business: comparison.your_business,
      competitor: comparison.competitor,
      comparison: comparison.comparison,
      your_score: comparison.your_score,
      competitor_score: comparison.competitor_score,
      selectedCompetitors: competitors
    })
  }

  /**
   * Handle analysis errors with proper messaging
   * @param {Error} err - Error object
   */
  function handleAnalysisError(err) {
    let errorMessage = ERROR_MESSAGES.GENERIC_ERROR
    
    if (err.message) {
      errorMessage = err.message
    } else if (err.response) {
      const status = err.response.status
      switch (status) {
        case 400:
          errorMessage = ERROR_MESSAGES.INVALID_REQUEST
          break
        case 500:
          errorMessage = ERROR_MESSAGES.SERVER_ERROR
          break
        default:
          errorMessage = ERROR_MESSAGES.GENERIC_ERROR
      }
    } else if (err.request) {
      errorMessage = ERROR_MESSAGES.NETWORK_ERROR
    }
    
    store.setError(errorMessage)
  }

  /**
   * Clear analysis error
   */
  function clearError() {
    store.clearError()
  }

  /**
   * Retry analysis with same parameters
   */
  async function retryAnalysis() {
    if (store.searchQuery) {
      await handleAnalysis(store.searchQuery)
    }
  }

  // Computed properties
  const error = computed(() => store.error)
  const hasError = computed(() => store.hasError)
  const canRetry = computed(() => store.canRetry)

  return {
    // State
    error,
    isProcessing,
    hasError,
    canRetry,
    
    // Methods
    handleAnalysis,
    clearError,
    retryAnalysis
  }
} 
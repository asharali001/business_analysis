import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useBusinessStore = defineStore('business', () => {
  // State
  const comparison = ref(null)
  const searchQuery = ref(null)
  const loading = ref(false)
  const error = ref(null)

  // Getters
  const hasComparison = computed(() => !!comparison.value)
  const isAnalysisType = computed(() => comparison.value?.type === 'analysis')
  const isComparisonType = computed(() => comparison.value?.type === 'comparison')
  const hasError = computed(() => !!error.value)
  const canRetry = computed(() => !!searchQuery.value && hasError.value)

  const targetBusiness = computed(() => {
    if (!comparison.value) return null
    return comparison.value.target_business || comparison.value.your_business
  })

  const competitorBusiness = computed(() => {
    if (!comparison.value || comparison.value.type !== 'comparison') return null
    return comparison.value.competitor
  })

  // Actions
  function setComparison(data) {
    comparison.value = data
    error.value = null
  }

  function setSearchQuery(query) {
    searchQuery.value = query
  }

  function setLoading(state) {
    loading.value = state
  }

  function setError(errorMessage) {
    error.value = errorMessage
  }

  function clearError() {
    error.value = null
  }

  function clear() {
    comparison.value = null
    searchQuery.value = null
    loading.value = false
    error.value = null
  }

  function reset() {
    clear()
  }

  return {
    // State
    comparison,
    searchQuery,
    loading,
    error,

    // Getters
    hasComparison,
    isAnalysisType,
    isComparisonType,
    hasError,
    canRetry,
    targetBusiness,
    competitorBusiness,

    // Actions
    setComparison,
    setSearchQuery,
    setLoading,
    setError,
    clearError,
    clear,
    reset
  }
}) 
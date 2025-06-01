<template>
  <AppLayout>
    <div class="container mx-auto px-4 py-8 max-w-6xl">
      <!-- Loading state -->
      <LoadingState v-if="store.loading" />

      <!-- Results content -->
      <div v-else-if="store.hasComparison">
        <!-- Page header -->
        <div class="mb-8">
          <h1 class="text-3xl font-bold text-gray-900">
            {{ store.isAnalysisType ? 'Business Analysis' : 'Business Comparison' }}
          </h1>
          <p class="text-gray-600 mt-2">
            {{ store.isAnalysisType 
                ? `Analysis results for ${store.targetBusiness?.name || 'your business'}` 
                : `Comparison between ${store.targetBusiness?.name || 'your business'} and ${store.competitorBusiness?.name || 'competitor'}` }}
          </p>
        </div>

        <!-- Business Analysis View -->
        <BusinessAnalysisView 
          v-if="store.isAnalysisType"
          :loading-new-comparison="loadingNewComparison"
          @compare-business="compareWithBusiness"
        />

        <!-- Business Comparison View -->
        <BusinessComparisonView v-else-if="store.isComparisonType" />

       
      </div>

      <!-- No results state -->
      <div v-else class="text-center py-16">
        <div class="text-gray-400 text-6xl mb-4">📊</div>
        <h2 class="text-2xl font-bold text-gray-900 mb-2">No Analysis Data</h2>
        <p class="text-gray-600 mb-8">Start by analyzing your business from the home page.</p>
        <BaseButton @click="$router.push('/')">
          Start Analysis
        </BaseButton>
      </div>
    </div>
  </AppLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import AppLayout from '../components/layout/AppLayout.vue'
import { useBusinessStore } from '../stores/business'
import { performBusinessComparison } from '../services/api'
import LoadingState from '../components/comparison/LoadingState.vue'
import BusinessAnalysisView from '../components/analysis/BusinessAnalysisView.vue'
import BusinessComparisonView from '../components/analysis/BusinessComparisonView.vue'
import BaseButton from '../components/ui/BaseButton.vue'

const router = useRouter()
const store = useBusinessStore()
const newCompetitorName = ref('')
const loadingNewComparison = ref(false)

// Redirect to home if no comparison data
onMounted(() => {
  if (!store.hasComparison && !store.loading) {
    router.push('/')
  }
})

async function compareWithBusiness(businessName) {
  if (!businessName || !businessName.trim()) return
  
  try {
    loadingNewComparison.value = true
    
    const targetBusiness = store.targetBusiness
    
    const comparison = await performBusinessComparison(
      targetBusiness.name,
      targetBusiness.website,
      businessName.trim(),
      null
    )
    
    // Update the store with new comparison data
    store.setComparison({
      type: 'comparison',
      your_business: comparison.your_business,
      competitor: comparison.competitor,
      comparison: comparison.comparison,
      your_score: comparison.your_score,
      competitor_score: comparison.competitor_score
    })
    
    // Clear the input
    newCompetitorName.value = ''
    
  } catch (error) {
    console.error('Comparison failed:', error)
    store.setError('Failed to compare with this business. Please try again.')
  } finally {
    loadingNewComparison.value = false
  }
}
</script>

<style scoped>
.animation-delay-300 {
  animation-delay: 300ms;
}
.animation-delay-600 {
  animation-delay: 600ms;
}
</style> 
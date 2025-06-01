<template>
  <AppLayout>
    <div class="container mx-auto px-4 py-8 max-w-6xl">
      <!-- Hero Section -->
      <div class="text-center mb-12">
        <h1 class="text-5xl font-bold mb-4 text-gray-900">
          🍔 Business Profile Comparator
        </h1>
        <p class="text-xl text-gray-600 mb-8 max-w-3xl mx-auto">
          Compare your business with competitors and get AI-powered insights to improve your online presence and attract more customers.
        </p>        
      </div>
      
      <!-- Business Input Form -->
      <BusinessInputForm @compare="handleAnalysis" :isLoading="isProcessing" />
    
      <!-- Error display -->
      <div v-if="hasError" class="mt-6 max-w-2xl mx-auto">
        <BaseAlert 
          type="error" 
          title="Analysis Error"
          :message="error"
          dismissible
          @dismiss="clearError"
        >
          <template #actions>
            <div class="mt-2">
              <BaseButton 
                v-if="canRetry"
                variant="outline" 
                size="sm" 
                @click="retryAnalysis"
                :loading="isProcessing"
              >
                Try Again
              </BaseButton>
            </div>
          </template>
        </BaseAlert>
      </div>
    </div>
  </AppLayout>
</template>

<script setup>
import AppLayout from '../components/layout/AppLayout.vue'
import BusinessInputForm from '../components/forms/BusinessInputForm.vue'
import BaseAlert from '../components/ui/BaseAlert.vue'
import BaseButton from '../components/ui/BaseButton.vue'
import { useBusinessAnalysis } from '../composables/useBusinessAnalysis'

const { 
  error, 
  isProcessing, 
  hasError, 
  canRetry, 
  handleAnalysis, 
  clearError, 
  retryAnalysis 
} = useBusinessAnalysis()
</script> 
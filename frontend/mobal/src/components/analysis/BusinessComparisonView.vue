<template>
  <div class="space-y-8">
    <!-- Business Comparison Cards -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <BusinessComparisonCard 
        v-if="store.targetBusiness"
        :business="store.targetBusiness"
        :score="store.comparison.your_score || 0"
        title="Your Business"
        icon="🏢"
      />
      
      <BusinessComparisonCard 
        v-if="store.competitorBusiness"
        :business="store.competitorBusiness"
        :score="store.comparison.competitor_score || 0"
        title="Competitor"
        icon="🏪"
      />
    </div>

    <!-- Detailed Metrics Comparison -->
    <BusinessMetricsComparison 
      v-if="store.targetBusiness && store.competitorBusiness"
      :your-business="store.targetBusiness"
      :competitor="store.competitorBusiness"
    />

    <!-- Comparison Analysis -->
    <BaseCard v-if="store.comparison.comparison" variant="default">
      <template #header>
        <h2 class="text-xl font-bold text-gray-900 flex items-center">
          📊 Detailed Comparison Analysis
        </h2>
      </template>

      <div v-if="store.comparison.comparison.summary" class="mb-6">
        <div class="p-6 bg-gradient-to-r from-blue-50 to-indigo-50 border border-blue-200 rounded-lg">
          <h3 class="font-semibold text-blue-900 mb-3 flex items-center">
            📋 Executive Summary
          </h3>
          <p class="text-blue-900 leading-relaxed">{{ store.comparison.comparison.summary }}</p>
        </div>
      </div>

      <!-- Strategic Recommendations -->
      <div v-if="store.comparison.comparison.suggestions && store.comparison.comparison.suggestions.length > 0" class="mb-6">
        <h3 class="font-semibold text-gray-900 mb-4 flex items-center text-lg">
          💡 Strategic Recommendations
        </h3>
        <div class="space-y-4">
          <div v-for="(suggestion, index) in store.comparison.comparison.suggestions" :key="index" 
               class="p-5 bg-gradient-to-r from-green-50 to-emerald-50 border border-green-200 rounded-lg hover:shadow-md transition-shadow">
            <div class="flex items-start">
              <span class="text-green-600 font-bold mr-4 mt-1 text-lg">{{ index + 1 }}.</span>
              <span class="text-green-900 leading-relaxed font-medium">{{ suggestion }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Competitive Strengths -->
      <div v-if="store.comparison.comparison.strengths && store.comparison.comparison.strengths.length > 0" class="mb-6">
        <h3 class="font-semibold text-gray-900 mb-4 flex items-center text-lg text-emerald-600">
          🏆 Your Competitive Advantages
        </h3>
        <div class="space-y-3">
          <div v-for="(strength, index) in store.comparison.comparison.strengths" :key="index" 
               class="p-4 bg-gradient-to-r from-emerald-50 to-green-50 border border-emerald-200 rounded-lg">
            <div class="flex items-start">
              <span class="text-emerald-500 mr-3 mt-0.5 text-lg">✓</span>
              <span class="text-emerald-900 leading-relaxed">{{ strength }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Legacy Strengths and Weaknesses (fallback) -->
      <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div v-if="store.comparison.comparison.your_strengths">
          <h3 class="font-semibold text-gray-900 mb-3 text-green-600">✅ Your Strengths</h3>
          <ul class="space-y-2">
            <li v-for="(strength, index) in store.comparison.comparison.your_strengths" :key="index" 
                class="flex items-start">
              <span class="text-green-500 mr-2 mt-0.5">✓</span>
              <span>{{ strength }}</span>
            </li>
          </ul>
        </div>

        <div v-if="store.comparison.comparison.areas_for_improvement">
          <h3 class="font-semibold text-gray-900 mb-3 text-orange-600">🔧 Areas for Improvement</h3>
          <ul class="space-y-2">
            <li v-for="(improvement, index) in store.comparison.comparison.areas_for_improvement" :key="index" 
                class="flex items-start">
              <span class="text-orange-500 mr-2 mt-0.5">•</span>
              <span>{{ improvement }}</span>
            </li>
          </ul>
        </div>
      </div>

      <!-- Score Comparison Visualization -->
      <div class="mt-8 p-6 bg-gray-50 rounded-lg">
        <h3 class="font-semibold text-gray-900 mb-4 flex items-center text-lg">
          📈 Performance Comparison
        </h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="text-center">
            <div class="mb-2">
              <span class="text-2xl font-bold text-blue-600">{{ store.comparison.your_score || 0 }}</span>
              <span class="text-gray-500">/100</span>
            </div>
            <div class="w-full bg-gray-200 rounded-full h-3 mb-2">
              <div class="bg-blue-600 h-3 rounded-full transition-all duration-500" 
                   :style="`width: ${store.comparison.your_score || 0}%`"></div>
            </div>
            <p class="text-sm font-medium text-gray-700">{{ store.targetBusiness?.name || 'Your Business' }}</p>
          </div>
          <div class="text-center">
            <div class="mb-2">
              <span class="text-2xl font-bold text-orange-600">{{ store.comparison.competitor_score || 0 }}</span>
              <span class="text-gray-500">/100</span>
            </div>
            <div class="w-full bg-gray-200 rounded-full h-3 mb-2">
              <div class="bg-orange-600 h-3 rounded-full transition-all duration-500" 
                   :style="`width: ${store.comparison.competitor_score || 0}%`"></div>
            </div>
            <p class="text-sm font-medium text-gray-700">{{ store.competitorBusiness?.name || 'Competitor' }}</p>
          </div>
        </div>
        
        <!-- Score Difference -->
        <div class="mt-4 text-center">
          <div v-if="(store.comparison.your_score || 0) > (store.comparison.competitor_score || 0)" 
               class="inline-flex items-center px-4 py-2 bg-green-100 text-green-800 rounded-full">
            <span class="mr-2">🎉</span>
            You're ahead by {{ Math.abs((store.comparison.your_score || 0) - (store.comparison.competitor_score || 0)).toFixed(2) }} points!
          </div>
          <div v-else-if="(store.comparison.your_score || 0) < (store.comparison.competitor_score || 0)" 
               class="inline-flex items-center px-4 py-2 bg-orange-100 text-orange-800 rounded-full">
            <span class="mr-2">⚡</span>
            {{ Math.abs((store.comparison.your_score || 0) - (store.comparison.competitor_score || 0)).toFixed(2) }} points to catch up
          </div>
          <div v-else class="inline-flex items-center px-4 py-2 bg-gray-100 text-gray-800 rounded-full">
            <span class="mr-2">🤝</span>
            It's a tie!
          </div>
        </div>
      </div>
    </BaseCard>
  </div>
</template>

<script setup>
import { useBusinessStore } from '../../stores/business'
import BusinessComparisonCard from '../comparison/BusinessComparisonCard.vue'
import BusinessMetricsComparison from '../comparison/BusinessMetricsComparison.vue'
import BaseCard from '../ui/BaseCard.vue'

const store = useBusinessStore()
</script> 
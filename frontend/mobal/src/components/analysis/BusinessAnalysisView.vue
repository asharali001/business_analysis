<template>
  <div class="space-y-8">
    <!-- Business Profile Card -->
    <BusinessProfileCard 
      v-if="store.targetBusiness"
      :business="store.targetBusiness" 
      :score="store.comparison.score || 0" 
    />

    <!-- Business Description Section -->
    <BusinessDescription 
      v-if="store.targetBusiness"
      :business="store.targetBusiness" 
    />

    <!-- Business Hours & Operations -->
    <BusinessHours 
      v-if="store.targetBusiness"
      :business="store.targetBusiness" 
    />

    <!-- Photos & Visual Content Section -->
    <BusinessPhotos 
      v-if="store.targetBusiness"
      :business="store.targetBusiness" 
    />

    <!-- Analysis Summary -->
    <BaseCard v-if="store.comparison.analysis" variant="default">
      <template #header>
        <h2 class="text-xl font-bold text-gray-900 flex items-center">
          📊 AI Analysis Summary
        </h2>
      </template>

      <div v-if="store.comparison.analysis.summary" class="mb-6">
        <div class="p-4 bg-blue-50 border border-blue-200 rounded-lg">
          <p class="text-blue-900 leading-relaxed font-medium">{{ store.comparison.analysis.summary }}</p>
        </div>
      </div>

      <!-- Suggestions -->
      <div v-if="store.comparison.analysis.suggestions && store.comparison.analysis.suggestions.length > 0">
        <h3 class="font-semibold text-gray-900 mb-4 flex items-center">
          💡 Strategic Recommendations
        </h3>
        <div class="space-y-3">
          <div v-for="(suggestion, index) in store.comparison.analysis.suggestions" :key="index" 
               class="p-4 bg-gradient-to-r from-green-50 to-emerald-50 border border-green-200 rounded-lg">
            <div class="flex items-start">
              <span class="text-green-600 font-bold mr-3 mt-1">{{ index + 1 }}.</span>
              <span class="text-green-900 leading-relaxed">{{ suggestion }}</span>
            </div>
          </div>
        </div>
      </div>
    </BaseCard>

    <!-- Competitors Section -->
    <BaseCard v-if="store.comparison.competitors && store.comparison.competitors.length > 0" variant="default">
      <template #header>
        <h2 class="text-xl font-bold text-gray-900 flex items-center">
          🏢 Competitors Found
        </h2>
      </template>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div v-for="(competitor, index) in store.comparison.competitors" :key="index" 
             class="p-4 border border-gray-200 rounded-lg hover:shadow-md transition-shadow">
          <h3 class="font-medium text-gray-900 mb-2">{{ competitor.name }}</h3>
          <div class="text-sm text-gray-600 space-y-1">
            <div class="flex justify-between">
              <span>Rating:</span>
              <span>{{ competitor.average_rating || 'N/A' }}/5</span>
            </div>
            <div class="flex justify-between">
              <span>Reviews:</span>
              <span>{{ competitor.review_count || 0 }}</span>
            </div>
          </div>
          <BaseButton 
            variant="outline" 
            size="sm" 
            class="mt-3 w-full"
            @click="$emit('compare-business', competitor.name)"
            :loading="loadingNewComparison"
          >
            Compare
          </BaseButton>
        </div>
      </div>
    </BaseCard>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue'
import { useBusinessStore } from '../../stores/business'
import BusinessProfileCard from '../business/BusinessProfileCard.vue'
import BusinessDescription from '../business/BusinessDescription.vue'
import BusinessPhotos from '../business/BusinessPhotos.vue'
import BusinessHours from '../business/BusinessHours.vue'
import BaseCard from '../ui/BaseCard.vue'
import BaseButton from '../ui/BaseButton.vue'

const props = defineProps({
  loadingNewComparison: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['compare-business'])

const store = useBusinessStore()
</script> 
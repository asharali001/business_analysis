<template>
  <BaseCard variant="default">
    <template #header>
      <div class="flex items-start justify-between">
        <div class="flex-1">
          <div class="flex items-center mb-2">
            <h2 class="text-2xl font-bold text-gray-900 mr-3">{{ business.name }}</h2>
            <div v-if="business.is_open !== undefined" :class="[
              'px-2 py-1 rounded-full text-xs font-medium',
              business.is_open ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
            ]">
              {{ business.is_open ? 'Open' : 'Closed' }}
            </div>
          </div>
          <div class="space-y-1">
            <p class="text-gray-600 font-medium">{{ business.category || 'Business' }}</p>
            <p class="text-sm text-gray-500">{{ business.full_address || business.address || 'Location not available' }}</p>
            
            <div v-if="business.established_year" class="text-sm text-gray-500">
              Established {{ business.established_year }} • {{ getYearsInBusiness() }} years in business
            </div>
                        <div v-if="business.website" class="text-sm text-gray-500">
              <a :href="business.website" target="_blank" class="text-blue-600 hover:text-blue-800">
                {{ business.website }}
              </a>
            </div>

          </div>
        </div>
        <div class="text-right ml-6">
          <div class="text-3xl font-bold text-blue-600">{{ score }}/100</div>
          <div class="text-sm text-gray-500">Overall Score</div>
          <div class="text-xs text-gray-400 mt-1">{{ getScoreCategory(score) }}</div>
        </div>
      </div>
    </template>

    <!-- Enhanced Key Metrics -->
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
      <div class="text-center p-4 bg-gradient-to-r from-yellow-50 to-orange-50 rounded-lg border border-yellow-200">
        <div class="text-2xl font-bold text-yellow-600">{{ business.average_rating || 0 }}/5</div>
        <div class="text-sm text-yellow-700">Rating</div>
        <div class="flex justify-center mt-1">
          <span v-for="i in 5" :key="i" class="text-sm">
            {{ i <= Math.floor(business.average_rating || 0) ? '⭐' : '☆' }}
          </span>
        </div>
      </div>
      <div class="text-center p-4 bg-gradient-to-r from-green-50 to-emerald-50 rounded-lg border border-green-200">
        <div class="text-2xl font-bold text-green-600">{{ business.review_count || 0 }}</div>
        <div class="text-sm text-green-700">Reviews</div>
        <div class="text-xs text-green-600 mt-1">{{ getReviewVolumeText(business.review_count) }}</div>
      </div>
      <div class="text-center p-4 bg-gradient-to-r from-blue-50 to-indigo-50 rounded-lg border border-blue-200">
        <div class="text-2xl font-bold text-blue-600">{{ business.image_count || 0 }}</div>
        <div class="text-sm text-blue-700">Photos</div>
        <div class="text-xs text-blue-600 mt-1">{{ getPhotoStatus(business.image_count) }}</div>
      </div>
      <div class="text-center p-4 bg-gradient-to-r from-purple-50 to-pink-50 rounded-lg border border-purple-200">
        <div class="text-2xl font-bold text-purple-600">{{ completionPercentage }}%</div>
        <div class="text-sm text-purple-700">Profile Complete</div>
        <div class="text-xs text-purple-600 mt-1">{{ getCompletionStatus(completionPercentage) }}</div>
      </div>
    </div>

    <!-- Special Features and Popular Items -->
    <div v-if="hasSpecialFeaturesOrDishes" class="mt-8 pt-6 border-t border-gray-200">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <!-- Special Features -->
        <div v-if="business.special_features && business.special_features.length > 0">
          <h4 class="font-medium text-gray-900 mb-3">✨ Special Features</h4>
          <div class="flex flex-wrap gap-2">
            <span v-for="feature in business.special_features" :key="feature"
                  class="px-3 py-1 bg-indigo-100 text-indigo-800 rounded-full text-sm font-medium">
              {{ feature }}
            </span>
          </div>
        </div>

        <!-- Popular Dishes -->
        <div v-if="business.popular_dishes && business.popular_dishes.length > 0">
          <h4 class="font-medium text-gray-900 mb-3">🍽️ Popular Items</h4>
          <div class="flex flex-wrap gap-2">
            <span v-for="dish in business.popular_dishes" :key="dish"
                  class="px-3 py-1 bg-orange-100 text-orange-800 rounded-full text-sm font-medium">
              {{ dish }}
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- Closure Notice -->
    <div v-if="business.temporarily_closed" class="mt-6 p-4 bg-red-50 border border-red-200 rounded-lg">
      <div class="flex items-center">
        <span class="text-red-600 text-lg mr-2">⚠️</span>
        <div>
          <h4 class="font-medium text-red-900">Temporarily Closed</h4>
          <p class="text-sm text-red-700">This business is currently temporarily closed.</p>
        </div>
      </div>
    </div>
  </BaseCard>
</template>

<script setup>
import { computed } from 'vue'
import BaseCard from '../ui/BaseCard.vue'
import { calculateCompletionPercentage } from '../../utils'

const props = defineProps({
  business: {
    type: Object,
    required: true
  },
  score: {
    type: Number,
    default: 0
  }
})

const completionPercentage = computed(() => {
  return calculateCompletionPercentage(props.business)
})

const hasSpecialFeaturesOrDishes = computed(() => {
  return (props.business.special_features && props.business.special_features.length > 0) ||
         (props.business.popular_dishes && props.business.popular_dishes.length > 0)
})

const getYearsInBusiness = () => {
  if (!props.business.established_year) return 'N/A'
  return new Date().getFullYear() - props.business.established_year
}

const getScoreCategory = (score) => {
  if (score >= 90) return 'Excellent'
  if (score >= 80) return 'Very Good'
  if (score >= 70) return 'Good'
  if (score >= 60) return 'Average'
  return 'Needs Improvement'
}

const getReviewVolumeText = (count) => {
  if (!count || count === 0) return 'No reviews'
  if (count >= 200) return 'High volume'
  if (count >= 100) return 'Good volume'
  if (count >= 50) return 'Moderate'
  if (count >= 20) return 'Low volume'
  return 'Very low'
}

const getPhotoStatus = (count) => {
  if (!count || count === 0) return 'No photos'
  if (count >= 30) return 'Excellent'
  if (count >= 20) return 'Very good'
  if (count >= 10) return 'Good'
  if (count >= 5) return 'Fair'
  return 'Limited'
}

const getCompletionStatus = (percentage) => {
  if (percentage >= 90) return 'Excellent'
  if (percentage >= 80) return 'Very good'
  if (percentage >= 70) return 'Good'
  if (percentage >= 60) return 'Fair'
  return 'Incomplete'
}

const hasContactInfo = () => {
  return !!(props.business.phone || props.business.email || props.business.website)
}

const getProfileStatus = () => {
  const completion = completionPercentage.value
  if (completion >= 80) return 'Complete'
  if (completion >= 60) return 'Good'
  if (completion >= 40) return 'Basic'
  return 'Incomplete'
}

const getProfileStatusColor = () => {
  const completion = completionPercentage.value
  if (completion >= 80) return 'bg-green-500'
  if (completion >= 60) return 'bg-blue-500'
  if (completion >= 40) return 'bg-yellow-500'
  return 'bg-red-500'
}
</script> 
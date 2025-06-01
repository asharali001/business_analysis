<template>
  <BaseCard variant="default">
    <template #header>
      <h2 class="text-xl font-bold text-gray-900 flex items-center">
        📊 Business Metrics Comparison
      </h2>
    </template>

    <div class="space-y-8">
      <!-- Key Metrics Overview -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <!-- Rating Comparison -->
        <div class="text-center p-6 bg-gradient-to-br from-blue-50 to-blue-100 rounded-xl">
          <h3 class="text-lg font-semibold text-blue-900 mb-4">⭐ Customer Rating</h3>
          <div class="space-y-3">
            <div>
              <div class="text-2xl font-bold text-blue-700">{{ yourBusiness.average_rating || 0 }}/5</div>
              <div class="text-sm text-blue-600">{{ yourBusiness.name }}</div>
            </div>
            <div class="text-xs text-gray-500">vs</div>
            <div>
              <div class="text-2xl font-bold text-gray-700">{{ competitor.average_rating || 0 }}/5</div>
              <div class="text-sm text-gray-600">{{ competitor.name }}</div>
            </div>
          </div>
          <div class="mt-3">
            <div v-if="(yourBusiness.average_rating || 0) > (competitor.average_rating || 0)" 
                 class="text-green-600 text-sm font-medium">
              ↗️ {{ ((yourBusiness.average_rating || 0) - (competitor.average_rating || 0)).toFixed(1) }} higher
            </div>
            <div v-else-if="(yourBusiness.average_rating || 0) < (competitor.average_rating || 0)" 
                 class="text-orange-600 text-sm font-medium">
              ↘️ {{ ((competitor.average_rating || 0) - (yourBusiness.average_rating || 0)).toFixed(1) }} lower
            </div>
            <div v-else class="text-gray-600 text-sm font-medium">
              🤝 Equal rating
            </div>
          </div>
        </div>

        <!-- Review Volume Comparison -->
        <div class="text-center p-6 bg-gradient-to-br from-green-50 to-green-100 rounded-xl">
          <h3 class="text-lg font-semibold text-green-900 mb-4">💬 Review Volume</h3>
          <div class="space-y-3">
            <div>
              <div class="text-2xl font-bold text-green-700">{{ yourBusiness.total_reviews || yourBusiness.review_count || 0 }}</div>
              <div class="text-sm text-green-600">{{ yourBusiness.name }}</div>
            </div>
            <div class="text-xs text-gray-500">vs</div>
            <div>
              <div class="text-2xl font-bold text-gray-700">{{ competitor.total_reviews || competitor.review_count || 0 }}</div>
              <div class="text-sm text-gray-600">{{ competitor.name }}</div>
            </div>
          </div>
          <div class="mt-3">
            <div v-if="(yourBusiness.total_reviews || yourBusiness.review_count || 0) > (competitor.total_reviews || competitor.review_count || 0)" 
                 class="text-green-600 text-sm font-medium">
              ↗️ {{ (yourBusiness.total_reviews || yourBusiness.review_count || 0) - (competitor.total_reviews || competitor.review_count || 0) }} more reviews
            </div>
            <div v-else-if="(yourBusiness.total_reviews || yourBusiness.review_count || 0) < (competitor.total_reviews || competitor.review_count || 0)" 
                 class="text-orange-600 text-sm font-medium">
              ↘️ {{ (competitor.total_reviews || competitor.review_count || 0) - (yourBusiness.total_reviews || yourBusiness.review_count || 0) }} fewer reviews
            </div>
            <div v-else class="text-gray-600 text-sm font-medium">
              🤝 Equal reviews
            </div>
          </div>
        </div>

        <!-- Photos Comparison -->
        <div class="text-center p-6 bg-gradient-to-br from-purple-50 to-purple-100 rounded-xl">
          <h3 class="text-lg font-semibold text-purple-900 mb-4">📸 Photo Gallery</h3>
          <div class="space-y-3">
            <div>
              <div class="text-2xl font-bold text-purple-700">{{ yourBusiness.image_count || 0 }}</div>
              <div class="text-sm text-purple-600">{{ yourBusiness.name }}</div>
            </div>
            <div class="text-xs text-gray-500">vs</div>
            <div>
              <div class="text-2xl font-bold text-gray-700">{{ competitor.image_count || 0 }}</div>
              <div class="text-sm text-gray-600">{{ competitor.name }}</div>
            </div>
          </div>
          <div class="mt-3">
            <div v-if="(yourBusiness.image_count || 0) > (competitor.image_count || 0)" 
                 class="text-green-600 text-sm font-medium">
              ↗️ {{ (yourBusiness.image_count || 0) - (competitor.image_count || 0) }} more photos
            </div>
            <div v-else-if="(yourBusiness.image_count || 0) < (competitor.image_count || 0)" 
                 class="text-orange-600 text-sm font-medium">
              ↘️ {{ (competitor.image_count || 0) - (yourBusiness.image_count || 0) }} fewer photos
            </div>
            <div v-else class="text-gray-600 text-sm font-medium">
              🤝 Equal photos
            </div>
          </div>
        </div>
      </div>

      <!-- Service Features Comparison -->
      <div>
        <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
          🛎️ Service Features Comparison
        </h3>
        <div class="overflow-hidden border border-gray-200 rounded-lg">
          <table class="w-full">
            <thead class="bg-gray-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Feature</th>
                <th class="px-6 py-3 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">{{ yourBusiness.name }}</th>
                <th class="px-6 py-3 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">{{ competitor.name }}</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="feature in serviceFeatures" :key="feature.key" class="hover:bg-gray-50">
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                  {{ feature.icon }} {{ feature.label }}
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-center">
                  <span :class="yourBusiness[feature.key] ? 'text-green-600' : 'text-red-500'" class="text-lg">
                    {{ yourBusiness[feature.key] ? '✓' : '✗' }}
                  </span>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-center">
                  <span :class="competitor[feature.key] ? 'text-green-600' : 'text-red-500'" class="text-lg">
                    {{ competitor[feature.key] ? '✓' : '✗' }}
                  </span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Business Profile Completeness -->
      <div>
        <h3 class="text-lg font-semibold text-gray-900 mb-4 flex items-center">
          ✅ Profile Completeness Comparison
        </h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div>
            <h4 class="font-medium text-gray-900 mb-3">{{ yourBusiness.name }}</h4>
            <div class="space-y-3">
              <div class="flex items-center justify-between text-sm">
                <span>Overall Completeness</span>
                <span class="font-bold text-blue-600">{{ getCompletionPercentage(yourBusiness) }}%</span>
              </div>
              <div class="w-full bg-gray-200 rounded-full h-2">
                <div class="bg-blue-600 h-2 rounded-full transition-all duration-500" 
                     :style="`width: ${getCompletionPercentage(yourBusiness)}%`"></div>
              </div>
            </div>
          </div>
          
          <div>
            <h4 class="font-medium text-gray-900 mb-3">{{ competitor.name }}</h4>
            <div class="space-y-3">
              <div class="flex items-center justify-between text-sm">
                <span>Overall Completeness</span>
                <span class="font-bold text-orange-600">{{ getCompletionPercentage(competitor) }}%</span>
              </div>
              <div class="w-full bg-gray-200 rounded-full h-2">
                <div class="bg-orange-600 h-2 rounded-full transition-all duration-500" 
                     :style="`width: ${getCompletionPercentage(competitor)}%`"></div>
              </div>
            </div>
          </div>
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
  yourBusiness: {
    type: Object,
    required: true
  },
  competitor: {
    type: Object,
    required: true
  }
})

const serviceFeatures = computed(() => [
  { key: 'offers_delivery', label: 'Delivery', icon: '🚚' },
  { key: 'offers_takeout', label: 'Takeout', icon: '🥡' },
  { key: 'offers_dine_in', label: 'Dine-in', icon: '🍽️' },
  { key: 'accepts_reservations', label: 'Reservations', icon: '📅' },
  { key: 'has_wifi', label: 'WiFi', icon: '📶' },
  { key: 'accepts_credit_cards', label: 'Credit Cards', icon: '💳' },
  { key: 'wheelchair_accessible', label: 'Accessible', icon: '♿' },
  { key: 'outdoor_seating', label: 'Outdoor Seating', icon: '🌞' },
  { key: 'has_parking', label: 'Parking', icon: '🅿️' }
])

function getCompletionPercentage(business) {
  return calculateCompletionPercentage(business)
}
</script> 
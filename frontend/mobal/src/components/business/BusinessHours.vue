<template>
  <BaseCard variant="default">
    <template #header>
      <h2 class="text-xl font-bold text-gray-900 flex items-center">
        🕒 Business Hours & Operations
      </h2>
    </template>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
      <!-- Business Hours -->
      <div>
        <div class="flex items-center justify-between mb-4">
          <h3 class="font-semibold text-gray-900">Operating Hours</h3>
          <div class="flex items-center">
            <div :class="[
              'px-3 py-1 rounded-full text-sm font-medium',
              business.is_open ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
            ]">
              {{ business.is_open ? 'Currently Open' : 'Currently Closed' }}
            </div>
          </div>
        </div>

        <div v-if="business.business_hours" class="space-y-2">
          <div v-for="(dayObj, index) in business.business_hours" :key="index" 
               class="flex justify-between items-center p-3 bg-gray-50 rounded-lg">
            <span class="font-medium text-gray-900 capitalize">{{ Object.keys(dayObj)[0] }}</span>
            <span class="text-gray-700">{{ Object.values(dayObj)[0] || 'Closed' }}</span>
          </div>
        </div>
        <div v-else class="p-4 bg-yellow-50 border border-yellow-200 rounded-lg">
          <p class="text-yellow-800">Business hours not available</p>
        </div>

        <!-- Temporary Closure Notice -->
        <div v-if="business.temporarily_closed" class="mt-4 p-4 bg-red-50 border border-red-200 rounded-lg">
          <p class="text-red-800 font-medium">⚠️ Temporarily Closed</p>
          <p class="text-red-700 text-sm">This business is currently temporarily closed.</p>
        </div>
      </div>

      <!-- Service Options & Features -->
      <div>
        <h3 class="font-semibold text-gray-900 mb-4">Service Options</h3>
        
        <!-- Service Options -->
        <div class="mb-6">
          <h4 class="text-sm font-medium text-gray-700 mb-3">Available Services</h4>
          <div class="grid grid-cols-2 gap-3">
            <div class="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
              <span class="text-gray-600">Dine-in</span>
              <span :class="business.offers_dine_in ? 'text-green-600' : 'text-red-500'">
                {{ business.offers_dine_in ? '✓' : '✗' }}
              </span>
            </div>
            <div class="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
              <span class="text-gray-600">Takeout</span>
              <span :class="business.offers_takeout ? 'text-green-600' : 'text-red-500'">
                {{ business.offers_takeout ? '✓' : '✗' }}
              </span>
            </div>
            <div class="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
              <span class="text-gray-600">Delivery</span>
              <span :class="business.offers_delivery ? 'text-green-600' : 'text-red-500'">
                {{ business.offers_delivery ? '✓' : '✗' }}
              </span>
            </div>
            <div class="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
              <span class="text-gray-600">Reservations</span>
              <span :class="business.accepts_reservations ? 'text-green-600' : 'text-red-500'">
                {{ business.accepts_reservations ? '✓' : '✗' }}
              </span>
            </div>
          </div>
        </div>

        <!-- Additional Features -->
        <div>
          <h4 class="text-sm font-medium text-gray-700 mb-3">Additional Features</h4>
          <div class="grid grid-cols-2 gap-3">
            <div class="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
              <span class="text-gray-600">WiFi</span>
              <span :class="business.has_wifi ? 'text-green-600' : 'text-red-500'">
                {{ business.has_wifi ? '✓' : '✗' }}
              </span>
            </div>
            <div class="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
              <span class="text-gray-600">Parking</span>
              <span :class="business.has_parking ? 'text-green-600' : 'text-red-500'">
                {{ business.has_parking ? '✓' : '✗' }}
              </span>
            </div>
            <div class="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
              <span class="text-gray-600">Wheelchair Accessible</span>
              <span :class="business.wheelchair_accessible ? 'text-green-600' : 'text-red-500'">
                {{ business.wheelchair_accessible ? '✓' : '✗' }}
              </span>
            </div>
            <div class="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
              <span class="text-gray-600">Credit Cards</span>
              <span :class="business.accepts_credit_cards ? 'text-green-600' : 'text-red-500'">
                {{ business.accepts_credit_cards ? '✓' : '✗' }}
              </span>
            </div>
            <div class="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
              <span class="text-gray-600">Outdoor Seating</span>
              <span :class="business.outdoor_seating ? 'text-green-600' : 'text-red-500'">
                {{ business.outdoor_seating ? '✓' : '✗' }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>


  </BaseCard>
</template>

<script setup>
import BaseCard from '../ui/BaseCard.vue'

const props = defineProps({
  business: {
    type: Object,
    required: true
  }
})
</script> 
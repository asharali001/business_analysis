<template>
  <div class="bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden">
    <!-- Header Section -->
    <div class="bg-gradient-to-r from-blue-50 to-indigo-50 p-6 border-b border-gray-200">
      <div class="flex items-start justify-between">
        <div>
          <h3 class="text-lg font-semibold text-gray-900 flex items-center">
            {{ icon }} {{ title }}
          </h3>
          <h4 class="text-2xl font-bold text-gray-900 mt-1">{{ business.name }}</h4>
          <div class="flex items-center mt-2 space-x-4">
            <span class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-blue-100 text-blue-800">
              {{ business.category || 'Business' }}
            </span>
            <span v-if="business.established_year" class="text-sm text-gray-600">
              Est. {{ business.established_year }}
            </span>
            <span v-if="business.price_range" class="text-sm font-medium text-green-600">
              {{ business.price_range }}
            </span>
          </div>
        </div>
        <div class="text-right">
          <div class="text-3xl font-bold text-blue-600">{{ score }}/100</div>
          <div class="text-sm text-gray-500">Business Score</div>
        </div>
      </div>
    </div>

    <div class="p-6 space-y-6">
      <!-- Contact & Location -->
      <div>
        <h5 class="text-lg font-semibold text-gray-900 mb-3 flex items-center">
          📍 Contact & Location
        </h5>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
          <div v-if="business.full_address || business.address" class="flex items-start space-x-2">
            <span class="text-gray-400 mt-0.5">📍</span>
            <span class="text-gray-700">{{ business.full_address || business.address }}</span>
          </div>
          <div v-if="business.phone" class="flex items-center space-x-2">
            <span class="text-gray-400">📞</span>
            <a :href="`tel:${business.phone}`" class="text-blue-600 hover:underline">{{ business.phone }}</a>
          </div>
          <div v-if="business.website" class="flex items-center space-x-2">
            <span class="text-gray-400">🌐</span>
            <a :href="business.website" target="_blank" class="text-blue-600 hover:underline truncate">
              {{ business.website.replace(/https?:\/\//, '') }}
            </a>
          </div>
          <div v-if="business.email" class="flex items-center space-x-2">
            <span class="text-gray-400">✉️</span>
            <a :href="`mailto:${business.email}`" class="text-blue-600 hover:underline">{{ business.email }}</a>
          </div>
        </div>
      </div>

      <!-- Key Performance Metrics -->
      <div>
        <h5 class="text-lg font-semibold text-gray-900 mb-3 flex items-center">
          📊 Performance Metrics
        </h5>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div class="text-center p-4 bg-gray-50 rounded-lg">
            <div class="text-2xl font-bold text-gray-900">{{ business.average_rating || 0 }}/5</div>
            <div class="text-xs text-gray-600">Average Rating</div>
          </div>
          <div class="text-center p-4 bg-gray-50 rounded-lg">
            <div class="text-2xl font-bold text-gray-900">{{ business.total_reviews || business.review_count || 0 }}</div>
            <div class="text-xs text-gray-600">Total Reviews</div>
          </div>
          <div class="text-center p-4 bg-gray-50 rounded-lg">
            <div class="text-2xl font-bold text-gray-900">{{ business.image_count || 0 }}</div>
            <div class="text-xs text-gray-600">Photos</div>
          </div>
          <div class="text-center p-4 bg-gray-50 rounded-lg">
            <div class="text-2xl font-bold text-gray-900">{{ getCompletionPercentage() }}%</div>
            <div class="text-xs text-gray-600">Profile Complete</div>
          </div>
        </div>        
      </div>

      <!-- Business Hours -->
      <div v-if="business.business_hours && Object.keys(business.business_hours).length > 0">
        <h5 class="text-lg font-semibold text-gray-900 mb-3 flex items-center">
          🕒 Business Hours
        </h5>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-2 text-sm">
          <div v-if="business.business_hours" class="space-y-2">
          <div v-for="(dayObj, index) in business.business_hours" :key="index" 
               class="flex justify-between items-center p-3 bg-gray-50 rounded-lg">
            <span class="font-medium text-gray-900 capitalize">{{ Object.keys(dayObj)[0] }}</span>
            <span class="text-gray-700">{{ Object.values(dayObj)[0] || 'Closed' }}</span>
          </div>
        </div>
        </div>
        <div class="mt-2 flex items-center text-sm">
          <span :class="business.is_open ? 'text-green-600' : 'text-red-600'" class="flex items-center">
            <span class="w-2 h-2 rounded-full mr-2" :class="business.is_open ? 'bg-green-500' : 'bg-red-500'"></span>
            {{ business.is_open ? 'Currently Open' : 'Currently Closed' }}
            {{ business.temporarily_closed ? ' (Temporarily Closed)' : '' }}
          </span>
        </div>
      </div>

      <!-- Service Options -->
      <div>
        <h5 class="text-lg font-semibold text-gray-900 mb-3 flex items-center">
          🛎️ Service Options
        </h5>
        <div class="flex flex-wrap gap-2">
          <span v-if="business.offers_delivery" class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-green-100 text-green-800">
            🚚 Delivery
          </span>
          <span v-if="business.offers_takeout" class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-blue-100 text-blue-800">
            🥡 Takeout
          </span>
          <span v-if="business.offers_dine_in" class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-purple-100 text-purple-800">
            🍽️ Dine-in
          </span>
          <span v-if="business.accepts_reservations" class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-orange-100 text-orange-800">
            📅 Reservations
          </span>
          <span v-if="business.has_wifi" class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-indigo-100 text-indigo-800">
            📶 WiFi
          </span>
          <span v-if="business.accepts_credit_cards" class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-gray-100 text-gray-800">
            💳 Cards Accepted
          </span>
          <span v-if="business.wheelchair_accessible" class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-teal-100 text-teal-800">
            ♿ Accessible
          </span>
          <span v-if="business.outdoor_seating" class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-yellow-100 text-yellow-800">
            🌞 Outdoor Seating
          </span>
        </div>

        <!-- Special Features -->
        <div v-if="business.special_features && business.special_features.length > 0" class="mt-3">
          <div class="flex flex-wrap gap-2">
            <span v-for="feature in business.special_features" :key="feature" 
                  class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-emerald-100 text-emerald-800">
              ✨ {{ feature }}
            </span>
          </div>
        </div>
      </div>

      <!-- Popular Dishes -->
      <div v-if="business.popular_dishes && business.popular_dishes.length > 0">
        <h5 class="text-lg font-semibold text-gray-900 mb-3 flex items-center">
          🍴 Popular Items
        </h5>
        <div class="flex flex-wrap gap-2">
          <span v-for="dish in business.popular_dishes" :key="dish" 
                class="inline-flex items-center px-3 py-2 rounded-lg text-sm font-medium bg-amber-100 text-amber-800 border border-amber-200">
            🌟 {{ dish }}
          </span>
        </div>
      </div>

      <!-- Business Description -->
      <div v-if="business.description">
        <h5 class="text-lg font-semibold text-gray-900 mb-3 flex items-center">
          📝 About This Business
        </h5>
        <p class="text-sm text-gray-700 leading-relaxed bg-gray-50 p-4 rounded-lg">{{ business.description }}</p>
      </div>

      <!-- Social Media Links -->
      <div v-if="business.facebook_url || business.instagram_url || business.twitter_url">
        <h5 class="text-lg font-semibold text-gray-900 mb-3 flex items-center">
          🔗 Social Media
        </h5>
        <div class="flex space-x-3">
          <a v-if="business.facebook_url" :href="business.facebook_url" target="_blank" 
             class="flex items-center px-3 py-2 bg-blue-100 text-blue-800 rounded-lg hover:bg-blue-200 transition-colors text-sm">
            📘 Facebook
          </a>
          <a v-if="business.instagram_url" :href="business.instagram_url" target="_blank" 
             class="flex items-center px-3 py-2 bg-pink-100 text-pink-800 rounded-lg hover:bg-pink-200 transition-colors text-sm">
            📸 Instagram
          </a>
          <a v-if="business.twitter_url" :href="business.twitter_url" target="_blank" 
             class="flex items-center px-3 py-2 bg-sky-100 text-sky-800 rounded-lg hover:bg-sky-200 transition-colors text-sm">
            🐦 Twitter
          </a>
        </div>
      </div>

      <!-- Profile Completeness -->
      <div>
        <h5 class="text-lg font-semibold text-gray-900 mb-3 flex items-center">
          ✅ Profile Completeness
        </h5>
        <div class="grid grid-cols-2 md:grid-cols-3 gap-3 text-sm">
          <div class="flex items-center justify-between">
            <span class="text-gray-600">Phone:</span>
            <span :class="business.phone ? 'text-green-600' : 'text-red-500'">
              {{ business.phone ? '✓' : '✗' }}
            </span>
          </div>
          <div class="flex items-center justify-between">
            <span class="text-gray-600">Website:</span>
            <span :class="business.website ? 'text-green-600' : 'text-red-500'">
              {{ business.website ? '✓' : '✗' }}
            </span>
          </div>
          <div class="flex items-center justify-between">
            <span class="text-gray-600">Hours:</span>
            <span :class="business.has_hours ? 'text-green-600' : 'text-red-500'">
              {{ business.has_hours ? '✓' : '✗' }}
            </span>
          </div>
          <div class="flex items-center justify-between">
            <span class="text-gray-600">Description:</span>
            <span :class="business.has_description ? 'text-green-600' : 'text-red-500'">
              {{ business.has_description ? '✓' : '✗' }}
            </span>
          </div>
          <div class="flex items-center justify-between">
            <span class="text-gray-600">Menu:</span>
            <span :class="business.has_menu ? 'text-green-600' : 'text-red-500'">
              {{ business.has_menu ? '✓' : '✗' }}
            </span>
          </div>
          <div class="flex items-center justify-between">
            <span class="text-gray-600">Photos:</span>
            <span :class="business.image_count > 0 ? 'text-green-600' : 'text-red-500'">
              {{ business.image_count > 0 ? '✓' : '✗' }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { calculateCompletionPercentage } from '../../utils'

const props = defineProps({
  business: {
    type: Object,
    required: true
  },
  score: {
    type: Number,
    required: true
  },
  title: {
    type: String,
    required: true
  },
  icon: {
    type: String,
    required: true
  }
})

function getCompletionPercentage() {
  return calculateCompletionPercentage(props.business)
}
</script> 
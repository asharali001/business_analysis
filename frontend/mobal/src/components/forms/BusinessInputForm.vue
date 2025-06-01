<template>
  <div class="max-w-2xl mx-auto">
    <div class="bg-white rounded-xl shadow-lg border border-gray-100 overflow-hidden">
      <!-- Header -->
      <div class="bg-gradient-to-r from-blue-600 to-indigo-600 px-6 py-5">
        <h2 class="text-xl font-bold text-white">Business Analysis & Comparison Tool</h2>
        <p class="text-blue-100 text-sm mt-1">Analyze your business profile or compare with competitors to discover opportunities</p>
      </div>
      
      <!-- Form -->
      <form @submit.prevent="submit" class="p-6 space-y-6">
        <!-- Business Name Field -->
        <div class="space-y-2">
          <label for="business" class="block text-sm font-semibold text-gray-700">
            Business Name or Website
            <span class="text-red-500">*</span>
          </label>
          <div class="relative">
            <input 
              id="business"
              v-model="business" 
              required 
              type="text"
              placeholder="e.g., apple.com or Apple Inc."
              class="w-full px-4 py-3 border border-gray-300 rounded-lg shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 bg-gray-50 focus:bg-white"
            />
            <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
              <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m8 0V6a2 2 0 012 2v6.294a23.934 23.934 0 01-4.844 3.017M16 6H8m0 0v-.5a3 3 0 016 0V6m-6 0a23.931 23.931 0 015.618 1.5M12 15v2a3 3 0 01-3 3H6a3 3 0 01-3-3v-6a3 3 0 013-3h3a3 3 0 013 3v1z" />
              </svg>
            </div>
          </div>
        </div>

        <!-- Competitors Field -->
        <div class="space-y-2">
          <label for="competitors" class="block text-sm font-semibold text-gray-700">
            Competitors
            <span class="text-gray-400 font-normal">(optional - leave empty for analysis only)</span>
          </label>
          <div class="relative">
            <input 
              id="competitors"
              v-model="competitors" 
              type="text"
              placeholder="e.g., microsoft.com, google.com, amazon.com"
              class="w-full px-4 py-3 border border-gray-300 rounded-lg shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 bg-gray-50 focus:bg-white"
            />
            <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
              <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
              </svg>
            </div>
          </div>
          <p class="text-xs text-gray-500 mt-1">
            💡 Add competitors for comparison, or leave empty for business analysis only
          </p>
        </div>

        <!-- Style/Tone Selection -->
        <div class="space-y-2">
          <label class="block text-sm font-semibold text-gray-700">
            Suggestion Style
            <span class="text-gray-400 font-normal">(optional)</span>
          </label>
          <div class="flex space-x-4">
            <label class="flex items-center">
              <input 
                v-model="suggestionStyle" 
                type="radio" 
                value="casual" 
                class="mr-2 text-blue-600 focus:ring-blue-500"
              />
              <span class="text-sm text-gray-700">💬 Casual & Friendly</span>
            </label>
            <label class="flex items-center">
              <input 
                v-model="suggestionStyle" 
                type="radio" 
                value="data-driven" 
                class="mr-2 text-blue-600 focus:ring-blue-500"
              />
              <span class="text-sm text-gray-700">📊 Data-Driven & Professional</span>
            </label>
          </div>
          <p class="text-xs text-gray-500 mt-1">
            Choose how you'd like to receive your improvement suggestions
          </p>
        </div>

        <!-- Submit Button -->
        <div class="pt-2">
          <button 
            type="submit" 
            :disabled="props.isLoading"
            class="w-full bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 disabled:from-gray-400 disabled:to-gray-500 disabled:cursor-not-allowed text-white font-semibold py-3 px-6 rounded-lg shadow-md hover:shadow-lg transform hover:-translate-y-0.5 disabled:transform-none disabled:shadow-md transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
          >
            <span v-if="!props.isLoading" class="flex items-center justify-center space-x-2">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
              </svg>
              <span v-if="competitors.trim()">Start Comparison</span>
              <span v-else>Start Analysis</span>
            </span>
            <span v-else class="flex items-center justify-center space-x-2">
              <div class="animate-spin rounded-full h-5 w-5 border-b-2 border-white"></div>
              <span v-if="competitors.trim()">Analyzing Competition...</span>
              <span v-else>Analyzing Business...</span>
            </span>
          </button>
        </div>
        
        </form>
      
      <!-- Footer -->
      <div class="bg-gray-50 px-6 py-3 border-t border-gray-100">
        <p class="text-xs text-gray-500 text-center">
          🔒 Your data is processed securely and never stored permanently
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
const emit = defineEmits(['compare']);

const props = defineProps({
  isLoading: Boolean,
});

const business = ref('');
const competitors = ref('');
const suggestionStyle = ref('casual');

function submit() {
  emit('compare', {
    business: business.value,
    competitors: competitors.value.split(',').map(s => s.trim()).filter(Boolean),
    suggestionStyle: suggestionStyle.value,
  });
}

</script>

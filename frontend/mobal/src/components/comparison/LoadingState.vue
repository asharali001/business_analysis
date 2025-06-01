<template>
  <div class="text-center py-12">
    <div class="bg-white rounded-xl shadow-lg border border-gray-100 p-12 max-w-2xl mx-auto">
      <div class="flex items-center justify-center space-x-3 mb-6">
        <div class="animate-spin rounded-full h-10 w-10 border-b-2 border-blue-600"></div>
        <span class="text-xl text-gray-700 font-medium">
          Analyzing Business Profile...
        </span>
      </div>
      
      <!-- Progress steps -->
      <div class="space-y-4 mb-6">
        <div class="flex items-center justify-center space-x-2">
          <div class="w-4 h-4 bg-blue-600 rounded-full animate-pulse"></div>
          <span class="text-sm text-gray-600">Gathering business data</span>
        </div>
        <div class="flex items-center justify-center space-x-2">
          <div class="w-4 h-4 bg-blue-400 rounded-full animate-pulse animation-delay-300"></div>
          <span class="text-sm text-gray-600">Finding competitors</span>
        </div>
        <div class="flex items-center justify-center space-x-2">
          <div class="w-4 h-4 bg-blue-300 rounded-full animate-pulse animation-delay-600"></div>
          <span class="text-sm text-gray-600">Generating AI insights</span>
        </div>
      </div>
      
      <!-- Progress bar -->
      <div class="bg-gray-200 rounded-full h-3 mb-4">
        <div class="bg-gradient-to-r from-blue-600 to-indigo-600 h-3 rounded-full animate-pulse transition-all duration-1000" style="width: 75%"></div>
      </div>
      
      <p class="text-sm text-gray-500">
        Processing your business profile and generating competitive insights...
      </p>
    </div>
  </div>
</template>

<style scoped>
.animation-delay-300 {
  animation-delay: 300ms;
}
.animation-delay-600 {
  animation-delay: 600ms;
}
</style> 
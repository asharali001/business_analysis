<template>
  <nav class="bg-white shadow-sm border-b border-gray-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <!-- Logo and brand -->
        <router-link to="/" class="flex items-center space-x-3 hover:opacity-80 transition-opacity">
          <div class="w-10 h-10 bg-gradient-to-r from-blue-600 to-indigo-600 rounded-lg flex items-center justify-center">
            <span class="text-white font-bold text-lg">M</span>
          </div>
          <div>
            <h1 class="text-xl font-bold text-gray-900">Mobal</h1>
            <p class="text-xs text-gray-500">Business Comparator</p>
          </div>
        </router-link>

        <!-- Navigation items (if needed in the future) -->
        <div class="hidden md:flex items-center space-x-4">
          <!-- Add navigation items here if needed -->
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
// No additional logic needed for now
</script> 
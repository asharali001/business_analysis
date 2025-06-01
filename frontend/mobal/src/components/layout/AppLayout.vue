<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Navigation Header -->
    <AppHeader />
    
    <!-- Main content area -->
    <main class="flex-1">
      <slot />
    </main>
    
    <!-- Footer -->
    <AppFooter />
  </div>
</template>

<script setup>
import AppHeader from './AppHeader.vue'
import AppFooter from './AppFooter.vue'
</script> 
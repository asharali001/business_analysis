<template>
  <BaseCard v-if="hasImages" variant="default">
    <template #header>
      <h2 class="text-xl font-bold text-gray-900 flex items-center">
        📸 Business Photos
      </h2>
    </template>

    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
      <div v-for="(image, index) in displayedImages" :key="index" class="relative group">
        <img 
          :src="image.url" 
          :alt="image.title || 'Business photo'"
          class="w-full h-32 object-cover rounded-lg hover:scale-105 transition-transform duration-200 cursor-pointer"
          @click="openImageModal(image)"
          @error="handleImageError($event)"
        />
        <div v-if="image.title" 
             class="absolute bottom-0 left-0 right-0 bg-black bg-opacity-60 text-white text-xs p-2 rounded-b-lg opacity-0 group-hover:opacity-100 transition-opacity">
          {{ image.title }}
        </div>
      </div>
    </div>

    <div v-if="business.images.length > maxImagesDisplay" class="text-center mt-4">
      <BaseButton variant="outline" size="sm" @click="showAllImages = !showAllImages">
        {{ showAllImages ? 'Show Less' : `Show All ${business.images.length} Photos` }}
      </BaseButton>
    </div>
  </BaseCard>

  <BaseCard v-else variant="default">
    <template #header>
      <h2 class="text-xl font-bold text-gray-900 flex items-center">
        📸 Business Photos
      </h2>
    </template>

    <div class="text-center py-8">
      <div class="text-gray-400 text-4xl mb-2">📷</div>
      <h3 class="text-lg font-medium text-gray-900 mb-2">No Photos Available</h3>
      <p class="text-gray-600">This business doesn't have any photos uploaded yet.</p>
    </div>
  </BaseCard>
</template>

<script setup>
import { computed, ref } from 'vue'
import BaseCard from '../ui/BaseCard.vue'
import BaseButton from '../ui/BaseButton.vue'
import { UI_CONSTANTS } from '../../constants'

const props = defineProps({
  business: {
    type: Object,
    required: true
  }
})

const showAllImages = ref(false)
const maxImagesDisplay = UI_CONSTANTS.MAX_IMAGES_DISPLAY

const hasImages = computed(() => {
  return props.business.images && props.business.images.length > 0
})

const displayedImages = computed(() => {
  if (!props.business.images) return []
  
  if (showAllImages.value) {
    return props.business.images
  }
  
  return props.business.images.slice(0, maxImagesDisplay)
})

function openImageModal(image) {
  // Simple implementation - open in new tab
  // You could implement a proper modal here
  window.open(image.url, '_blank')
}

function handleImageError(event) {
  // Hide broken images gracefully
  event.target.style.display = 'none'
}
</script> 
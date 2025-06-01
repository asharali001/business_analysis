<template>
  <BaseCard v-if="hasDescription" variant="default">
    <template #header>
      <h2 class="text-xl font-bold text-gray-900 flex items-center">
        📝 Business Description
      </h2>
    </template>

    <p class="text-gray-700 leading-relaxed">{{ business.description }}</p>
  </BaseCard>
</template>

<script setup>
import { computed } from 'vue'
import BaseCard from '../ui/BaseCard.vue'

const props = defineProps({
  business: {
    type: Object,
    required: true
  }
})

const hasDescription = computed(() => {
  return props.business.description && props.business.description.trim().length > 0
})
</script> 
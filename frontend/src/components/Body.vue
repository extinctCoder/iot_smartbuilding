<script setup>
import CardOne from './Shared/CardOne.vue';
</script>

<template>
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-4">
    <CardOne title="voltage" value="220"></CardOne>
    <CardOne title="current" value="025"></CardOne>
    <CardOne title="power" value="025"></CardOne>
    <CardOne title="voltage" value="025"></CardOne>
  </div>
  <div
    class="border-2 border-dashed rounded-lg border-gray-300 dark:border-gray-600 h-96 mb-4"
  ></div>
  <div class="grid grid-cols-2 gap-4 mb-4">
    <div
      class="border-2 border-dashed rounded-lg border-gray-300 dark:border-gray-600 h-48 md:h-72"
    ></div>
    <div
      class="border-2 border-dashed rounded-lg border-gray-300 dark:border-gray-600 h-48 md:h-72"
    ></div>
    <div
      class="border-2 border-dashed rounded-lg border-gray-300 dark:border-gray-600 h-48 md:h-72"
    ></div>
    <div
      class="border-2 border-dashed rounded-lg border-gray-300 dark:border-gray-600 h-48 md:h-72"
    ></div>
  </div>
  <div
    class="border-2 border-dashed rounded-lg border-gray-300 dark:border-gray-600 h-96 mb-4"
  ></div>
  <div class="grid grid-cols-2 gap-4">
    <div
      class="border-2 border-dashed rounded-lg border-gray-300 dark:border-gray-600 h-48 md:h-72"
    ></div>
    <div
      class="border-2 border-dashed rounded-lg border-gray-300 dark:border-gray-600 h-48 md:h-72"
    ></div>
    <div
      class="border-2 border-dashed rounded-lg border-gray-300 dark:border-gray-600 h-48 md:h-72"
    ></div>
    <div
      class="border-2 border-dashed rounded-lg border-gray-300 dark:border-gray-600 h-48 md:h-72"
    ></div>
  </div>
</template>

<style scoped></style>

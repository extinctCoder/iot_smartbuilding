<script setup>
import CardOne from '../components/Shared/CardOne.vue';
</script>

<template>
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-4">
    <CardOne title="voltage" value="220"></CardOne>
    <CardOne title="current" value="025"></CardOne>
    <CardOne title="power" value="025"></CardOne>
    <CardOne title="voltage" value="025"></CardOne>
  </div>
</template>

<style scoped></style>

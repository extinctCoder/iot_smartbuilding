<script setup>
import CardOne from '../components/Shared/CardOne.vue';
</script>

<template>
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mb-4">
    <CardOne title="voltage" chanel="l1/101/voltage"></CardOne>
    <CardOne title="current" chanel="l1/101/current"></CardOne>
    <CardOne title="power" chanel="l1/101/power"></CardOne>
  </div>
</template>

<style scoped></style>

<!-- 
 function sendCommand() {
    output_steam.send('topic/ddsfsd', 'payload', 0, true);
  } -->

<!-- const output_steam = new paho.Client(
    '127.0.0.1',
    8888,
    'browser_' + Math.random().toString(16).substring(2, 8)
  ); -->

<script setup>
import CardOne from '../components/Shared/CardOne.vue';

import { onMounted, onUnmounted } from 'vue';

import paho from 'paho-mqtt';

onMounted(() => {
  const input_steam = new paho.Client(
    '127.0.0.1',
    8888,
    'browser_' + Math.random().toString(16).substring(2, 8)
  );
  const output_steam = new paho.Client(
    '127.0.0.1',
    8888,
    'browser_' + Math.random().toString(16).substring(2, 8)
  );
  input_steam.onMessageArrived = onMessageArrived;
  input_steam.connect({ onSuccess: onConnect });

  function onConnect() {
    input_steam.send('topic/ddsfsd', 'payload', 0, true);
  }
  function onMessageArrived(message) {
    console.log('onMessageArrived:' + message.payloadString);
  }

  function sendCommand() {
    output_steam.send('topic/ddsfsd', 'payload', 0, true);
  }
});
</script>

<template>
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-4">
    <CardOne title="voltage" value="220"></CardOne>
    <CardOne title="current" value="025"></CardOne>
    <CardOne title="power" value="025"></CardOne>
    <CardOne title="voltage" value="025"></CardOne>
    <button @click="send_msg">Disconnect WebSocket</button>
  </div>
</template>

<style scoped></style>

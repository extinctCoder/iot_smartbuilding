<script setup>
import CardOne from '../components/Shared/CardOne.vue';

import { defineComponent, ref } from 'vue';
import { useWebSocketStore } from '../stores/websocketStore';

const websocketStore = useWebSocketStore();
const messageInput = ref('');

const connectWebSocket = () => {
  websocketStore.connect('ws://127.0.0.1:8888');
};

const sendMessage = () => {
  websocketStore.sendMessage(messageInput.value);
  messageInput.value = '';
};

const disconnectWebSocket = () => {
  websocketStore.disconnect();
};
</script>

<template>
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-4">
    <CardOne title="voltage" value="220"></CardOne>
    <CardOne title="current" value="025"></CardOne>
    <CardOne title="power" value="025"></CardOne>
    <CardOne title="voltage" value="025"></CardOne>
    <div>
      <button @click="connectWebSocket">Connect WebSocket</button>
      <button @click="sendMessage('Hello, WebSocket')">Send Message</button>
      <!--<button @click="disconnectWebSocket">Disconnect WebSocket</button>
    <div v-for="message in $websocket.messages" :key="message">
      {{ message }}
    </div> -->
    </div>
  </div>
</template>

<style scoped></style>

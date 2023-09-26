<script setup>
const props = defineProps(['title', 'chanel']);

import { onMounted } from 'vue';

import paho from 'paho-mqtt';

onMounted(() => {
  const input_steam = new paho.Client(
    '127.0.0.1',
    8888,
    'browser_' + Math.random().toString(16).substring(2, 8)
  );

  input_steam.onMessageArrived = onMessageArrived;
  input_steam.connect({ onSuccess: onConnect });
  function onConnect() {
    input_steam.subscribe(props.chanel);
  }
  function onMessageArrived(message) {
    console.log('onMessageArrived:' + message.payloadString);
  }
});
</script>

<template>
  <section
    class="bg-white border-2 border-dashed border-gray-300 rounded-lg dark:border-gray-600"
  >
    <div class="max-w-screen-xl px-4 py-8 mx-auto text-center lg:py-16 lg:px-6">
      <div class="flex flex-col items-center justify-center">
        <dt class="mb-2 text-3xl md:text-4xl font-extrabold">{{ value }}</dt>
        <dd class="font-light text-gray-500 dark:text-gray-400">{{ title }}</dd>
      </div>
    </div>
  </section>
</template>

<style scoped></style>

<script setup>
import { onMounted, ref } from 'vue';

import paho from 'paho-mqtt';

const props = defineProps(['chanel']);
const command_data = ref('ON');
const output_steam = new paho.Client(
  '127.0.0.1',
  8888,
  'browser_' + Math.random().toString(16).substring(2, 8)
);

onMounted(() => {
  output_steam.connect();
});
function sendCommand() {
  if (command_data.value === 'ON') {
    command_data.value = 'OFF';
  } else {
    command_data.value = 'ON';
  }
  console.log(props.chanel);
  output_steam.send(props.chanel, command_data.value, 0, true);
}
</script>

<template>
  <button @click="sendCommand"
    class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">
    {{ command_data }}
  </button>
</template>

<style scoped></style>

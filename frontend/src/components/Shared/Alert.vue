<script setup>
import { onMounted } from 'vue';
import { ref } from 'vue';
import paho from 'paho-mqtt';

const props = defineProps(['title', 'chanel']);
const network_data = ref(0);

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
        network_data.value = message.payloadString;
        console.log('onMessageArrived: ->  ' + network_data.value);
    }
});
</script>

<template>
    <div class="p-4 mb-4 text-sm text-blue-800 rounded-lg bg-blue-50 dark:bg-gray-800 dark:text-blue-400" role="alert">
        <span class="font-medium">{{ network_data }}</span>
    </div>
</template>

<style scoped></style>

<script setup>
import CardOne from '../components/Shared/CardOne.vue';
import Action from '../components/Shared/Action.vue';
import Alert from '../components/Shared/Alert.vue';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const props = defineProps(['voltage', 'current', 'power', 'control']);
// const route = useRoute();
// const voltage = ref(route.path + '/voltage')
// const current = ref(route.path + '/current')
// const power = ref(route.path + '/power')
// const control = ref(route.path + '/control')

onMounted(() => {
  // const route = useRoute();
  // // voltage.value = ;
  // // current.value = ;
  // const pow = route.path + '/power';
  // // control.value = ;
  // console.log(voltage.value)
});
</script>
<template>
  <div class="grid grid-cols-1 py-4">

    <h1
      class="mb-4 text-4xl font-extrabold leading-none text-center tracking-tight text-blue-700 md:text-5xl lg:text-6xl dark:text-white">
      Room NO : {{ $route.path }}</h1>
    <p class="mb-6 text-lg text-center font-normal text-gray-500 lg:text-xl sm:px-16 xl:px-48 dark:text-gray-400">
      Information
      about the room</p>


  </div>
  <div class="grid grid-cols-1 py-4">
    <Alert :chanel="$route.fullPath + '/alert'"></Alert>
  </div>
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mb-4">
    <CardOne title="voltage" :chanel="$route.fullPath + '/voltage'"></CardOne>
    <CardOne title="current" :chanel="$route.fullPath + '/current'"></CardOne>
    <CardOne title="power" :chanel="$route.fullPath + '/power'"></CardOne>
  </div>
  <div class="grid grid-cols-1">
    <Action :chanel="$route.fullPath + '/control'"></Action>
  </div>
</template>
<style style scoped></style>

<script setup>
import { onMounted } from 'vue';
import {
  initAccordions,
  initCarousels,
  initCollapses,
  initDials,
  initDismisses,
  initDrawers,
  initDropdowns,
  initModals,
  initPopovers,
  initTabs,
  initTooltips,
} from 'flowbite';
import Header from './components/Header.vue';
import Sidebar from './components/Sidebar.vue';
import Body from './components/Body.vue';
import Footer from './components/Footer.vue';
import mqtt from 'mqtt';

onMounted(() => {
  initAccordions();
  initCarousels();
  initCollapses();
  initDials();
  initDismisses();
  initDrawers();
  initDropdowns();
  initModals();
  initPopovers();
  initTabs();
  initTooltips();

  let client = mqtt.connect('broker.emqx.io');
  client.subscribe('+/+/#');

  client.on('message', function (topic, message) {
    console.log(message);
  });
});
</script>

<template>
  <div class="antialiased">
    <Header></Header>
    <sidebar></sidebar>
    <div class="p-4 md:ml-64 h-auto pt-20">
      <div id="app">
        <router-view></router-view>
      </div>

      <!-- <div class="pt-5">
        <Footer></Footer>
      </div> -->
    </div>
  </div>
</template>

<style scoped></style>

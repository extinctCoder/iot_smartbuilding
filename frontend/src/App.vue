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
});
</script>

<template>
  <div class="antialiased bg-gray-50 dark:bg-gray-900">
    <Header></Header>
    <sidebar></sidebar>
    <div class="p-4 md:ml-64 h-auto pt-20">
      <Body></Body>
      <!-- <div class="pt-5">
        <Footer></Footer>
      </div> -->
    </div>
  </div>
</template>

<style scoped></style>

<script>
import onMounted from 'vue';
import AuthenticatedLayout from './layouts/AuthenticatedLayout.vue';
import UnauthenticatedLayout from './layouts/UnauthenticatedLayout.vue'
import Header from './components/Header.vue';
import Sidebar from './components/Sidebar.vue';
import Footer from './components/Footer.vue';
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


export default {
  data() {
    return {
      isAuthenticated: true,
    };
  },
  computed: {
    layoutComponent() {
      return this.isAuthenticated ? AuthenticatedLayout : UnauthenticatedLayout;
    },
  },
};
</script>

<template>
  <div id="app">
    <component :is="layoutComponent"></component>
  </div>
</template>

<style scoped></style> 
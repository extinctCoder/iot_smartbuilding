<script setup>

const props = defineProps(['title', 'link_name', 'link_id']);

</script>

<template>
  <li>
    <router-link :to="{ name: link_name, params: { id: link_id } }"
      class="flex items-center p-2 pl-11 w-full text-base font-medium text-gray-900 rounded-lg transition duration-75 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700">{{
        title }}</router-link>
  </li>
</template>

<style scoped></style>

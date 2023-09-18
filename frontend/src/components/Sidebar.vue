<script setup>
import SidebarItem from './Shared/SidebarItem.vue';
import SearchMobile from './SearchMobile.vue';
</script>

<template>
  <aside
    class="fixed top-0 left-0 z-40 w-64 h-screen pt-14 transition-transform -translate-x-full bg-white border-r border-gray-200 md:translate-x-0 dark:bg-gray-800 dark:border-gray-700"
    aria-label="Sidenav"
    id="drawer-navigation"
  >
    <div class="overflow-y-auto py-5 px-3 h-full bg-white dark:bg-gray-800">
      <SearchMobile></SearchMobile>
      <ul class="space-y-2">
        <li>
          <router-link
            to="/"
            class="flex items-center p-2 text-base font-medium text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group"
          >
            <svg
              aria-hidden="true"
              class="w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path d="M2 10a8 8 0 018-8v8h8a8 8 0 11-16 0z"></path>
              <path d="M12 2.252A8.014 8.014 0 0117.748 8H12V2.252z"></path>
            </svg>
            <span class="ml-3">Overview</span>
          </router-link>
        </li>
      </ul>
      <ul
        class="pt-5 mt-5 space-y-2 border-t border-gray-200 dark:border-gray-700"
      >
        <li>
          <router-link
            to="/room"
            type="button"
            class="flex items-center p-2 w-full text-base font-medium text-gray-900 rounded-lg transition duration-75 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700"
            aria-controls="dropdown-pages"
            data-collapse-toggle="dropdown-pages"
          >
            <font-awesome-icon :icon="['fas', 'layer-group']" />
            <span class="flex-1 ml-3 text-left whitespace-nowrap">Rooms</span>
            <svg
              aria-hidden="true"
              class="w-6 h-6"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                clip-rule="evenodd"
              ></path>
            </svg>
          </router-link>
          <ul id="dropdown-pages" class="hidden py-2 space-y-2">
            <SidebarItem
              title="101"
              link_name="room_detail"
              link_id="101"
            ></SidebarItem>
            <SidebarItem
              title="102"
              link_name="room_detail"
              link_id="102"
            ></SidebarItem>
            <SidebarItem
              title="103"
              link_name="room_detail"
              link_id="103"
            ></SidebarItem>
            <SidebarItem
              title="201"
              link_name="room_detail"
              link_id="201"
            ></SidebarItem>
            <SidebarItem
              title="202"
              link_name="room_detail"
              link_id="202"
            ></SidebarItem>
            <SidebarItem
              title="203"
              link_name="room_detail"
              link_id="203"
            ></SidebarItem>
          </ul>
        </li>
      </ul>
    </div>
    <div
      class="hidden absolute bottom-0 left-0 justify-center p-4 space-x-4 w-full lg:flex bg-white dark:bg-gray-800 z-20"
    >
      <a
        href="https://github.com/extinctcoder"
        class="inline-flex justify-center p-2 text-gray-500 rounded cursor-pointer dark:text-gray-400 hover:text-gray-900 dark:hover:text-white hover:bg-gray-100 dark:hover:bg-gray-600"
      >
        <font-awesome-icon :icon="['fas', 'house-chimney']" />
      </a>
    </div>
  </aside>
</template>

<style scoped></style>

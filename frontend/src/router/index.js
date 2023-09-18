import { createRouter, createWebHistory } from 'vue-router';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: import('../views/HomeView.vue'),
    },
    {
      path: '/login',
      name: 'login',
      component: import('../views/LoginView.vue'),
    },
    {
      path: '/logout',
      name: 'logout',
      component: import('../views/LogoutView.vue'),
    },
    {
      path: '/profile',
      name: 'profile',
      redirect: (to) => {
        return { path: '/' };
      },
      component: import('../views/ProfileView.vue'),
    },
    {
      path: '/setting',
      name: 'setting',
      redirect: (to) => {
        return { path: '/' };
      },
      component: import('../views/SettingView.vue'),
    },
    {
      path: '/room',
      name: 'room_list',
      redirect: (to) => {
        return { path: '/' };
      },
      component: () => import('../views/RoomListView.vue'),
    },
    {
      path: '/room/:id',
      name: 'room_detail',
      component: () => import('../views/RoomDetailView.vue'),
    },
  ],
});

export default router;

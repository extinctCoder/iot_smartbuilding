import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import LoginView from '../views/LoginView.vue';
import LogoutView from '../views/LogoutView.vue';
import ProfileView from '../views/ProfileView.vue';
import SettingView from '../views/SettingView.vue';
import RoomListView from '../views/RoomListView.vue';
import RoomDetailView from '../views/RoomDetailView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/logout',
      name: 'logout',
      component: LogoutView,
    },
    {
      path: '/profile',
      name: 'profile',
      redirect: (to) => {
        return { path: '/' };
      },
      component: ProfileView,
    },
    {
      path: '/setting',
      name: 'setting',
      redirect: (to) => {
        return { path: '/' };
      },
      component: SettingView,
    },
    {
      path: '/room',
      name: 'room_list',
      redirect: (to) => {
        return { path: '/' };
      },
      component: RoomListView,
    },
    {
      path: '/room/:id',
      name: 'room_detail',
      component: RoomDetailView,
    },
  ],
});

export default router;

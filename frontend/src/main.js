import { createApp } from 'vue';
import { createPinia } from 'pinia';
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

import App from './App.vue';
import router from './router';
import './assets/style.css';

import { createPahoMqttPlugin } from 'vue-paho-mqtt';
import {
  faUserSecret,
  faLayerGroup,
  faHouseChimney,
} from '@fortawesome/free-solid-svg-icons';

library.add(faUserSecret);
library.add(faLayerGroup);
library.add(faHouseChimney);

const app = createApp(App);

app.use(createPinia());
app.use(router);

app.config.productionTip = false;

app.component('font-awesome-icon', FontAwesomeIcon).mount('#app');

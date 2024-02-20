import './assets/main.css';

import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';

const startApp = (channel: any) => {
  const app = createApp(App);
  app.provide('vsk', channel.objects.vsk);
  app.use(createPinia());

  app.mount('#app');
};

// @ts-ignore
new QWebChannel(qt.webChannelTransport, startApp);

import { createApp } from 'vue';
import { createPinia } from 'pinia';
import i18n from './plugins/i18n';
import App from './App.vue';

const startApp = (channel: any) => {
  const app = createApp(App);
  app.provide('vsk', channel.objects.vsk);
  app.use(createPinia());
  app.use(i18n());

  app.mount('#app');
};

// @ts-ignore
new QWebChannel(qt.webChannelTransport, startApp);

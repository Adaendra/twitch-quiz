import Vue from 'vue';
import App from './app.vue';
import router from "./router";
import store from "./stores";

new Vue({
  el: '#app',
  router, // Declare Router definition
  store,  // Declare Stores
  render: h => h(App)
});

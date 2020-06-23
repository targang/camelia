import Vue from 'vue';
import App from './App.vue';

import 'bootstrap';
import '../../assets/scss/main.scss';

import { library } from '@fortawesome/fontawesome-svg-core';
import {
  faVk,
  faFacebook,
  faInstagram,
  faWhatsapp,
} from '@fortawesome/free-brands-svg-icons';
import { faPhoneAlt, faTrash } from '@fortawesome/free-solid-svg-icons';
import { faEnvelope } from '@fortawesome/free-regular-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

library.add(
  faVk,
  faTrash,
  faFacebook,
  faInstagram,
  faWhatsapp,
  faEnvelope,
  faPhoneAlt
);

Vue.component('fa-icon', FontAwesomeIcon);

new Vue({
  render: (h) => h(App),
}).$mount('#app');

import Vue from 'vue';
import app from './app.vue';

import 'bootstrap';
import '../../../node_modules/bootstrap/dist/css/bootstrap.css';
import '../../assets/scss/main.scss';

import { library } from '@fortawesome/fontawesome-svg-core';
import {
  faVk,
  faFacebook,
  faInstagram,
  faWhatsapp,
} from '@fortawesome/free-brands-svg-icons';
import {
  faPhoneAlt,
  faDollarSign,
  faAward,
  faTruck,
} from '@fortawesome/free-solid-svg-icons';
import { faEnvelope } from '@fortawesome/free-regular-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

library.add(
  faVk,
  faFacebook,
  faInstagram,
  faWhatsapp,
  faEnvelope,
  faPhoneAlt,
  faDollarSign,
  faAward,
  faTruck
);

Vue.component('fa-icon', FontAwesomeIcon);

new Vue({
  render: (h) => h(app),
}).$mount('#app');

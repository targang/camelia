<template>
  <div id="app">
    <base-navbar :count="cartCount" />

    <section>
      <parallax-img>
        <main-section />
      </parallax-img>
    </section>

    <section>
      <video-section />
    </section>

    <section>
      <parallax-img>
        <advantages-section />
      </parallax-img>
    </section>

    <section>
      <stuff-section />
    </section>

    <section>
      <parallax-img>
        <badge-section />
      </parallax-img>
    </section>

    <base-footer />
  </div>
</template>

<script>
import BaseNavbar from '../../components/BaseNavbar';
import BaseFooter from '../../components/BaseFooter';

import ParallaxImg from './components/ParallaxImg';

import MainSection from './components/MainSection';
import VideoSection from './components/VideoSection';
import AdvantagesSection from './components/AdvantagesSection';
import StuffSection from './components/StuffSection';
import BadgeSection from './components/BadgeSection';

export default {
  name: 'App',
  components: {
    BaseNavbar,
    BaseFooter,
    ParallaxImg,
    MainSection,
    VideoSection,
    AdvantagesSection,
    StuffSection,
    BadgeSection,
  },
  data() {
    return {
      cartCount: 0,
    };
  },
  created() {
    fetch('/cart/length')
      .then((responce) => {
        return responce.json();
      })
      .then((data) => {
        this.cartCount = parseInt(data.data.count);
      });
  },
};
</script>

<style lang="scss">
$primary-col: #800000;

section {
  color: $primary-col;
  &:first-of-type {
    margin-top: 108px;
  }
}
</style>

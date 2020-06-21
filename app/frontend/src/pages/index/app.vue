<template>
  <div id="app">
    <BaseNavbar></BaseNavbar>

    <section>
      <parallax-img>
        <first-section></first-section>
      </parallax-img>
    </section>

    <section>
      <second-section></second-section>
    </section>

    <section>
      <parallax-img>
        <third-section></third-section>
      </parallax-img>
    </section>

    <section>
      <fourth-section></fourth-section>
    </section>

    <section>
      <parallax-img>
        <fifth-section></fifth-section>
      </parallax-img>
    </section>

    <base-footer></base-footer>
  </div>
</template>

<script>
import BaseNavbar from '../../components/BaseNavbar';
import BaseFooter from '../../components/BaseFooter';

import ParallaxImg from './components/ParallaxImg';

import FirstSection from './components/FirstSection';
import SecondSection from './components/SecondSection';
import ThirdSection from './components/ThirdSection';
import FourthSection from './components/FourthSection';
import FifthSection from './components/FifthSection';

export default {
  name: 'app',
  components: {
    BaseNavbar,
    BaseFooter,
    ParallaxImg,
    FirstSection,
    SecondSection,
    ThirdSection,
    FourthSection,
    FifthSection,
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

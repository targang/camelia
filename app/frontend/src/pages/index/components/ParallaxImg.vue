<template>
  <div class="parallax-img">
    <div class="parallax-img__inner py-lg-3 py-md-2">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ParallaxImg',
};
</script>

<style lang="scss">
.parallax-img {
  background-image: url('../assets/background.webp');
  background-size: cover;
  background-attachment: fixed;
  background-position: center center;
  background-repeat: no-repeat;

  &__inner {
    background-color: rgba(255, 255, 255, 0.7);
  }
}
</style>

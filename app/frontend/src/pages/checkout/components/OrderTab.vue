<template>
  <div v-show="isActive">
    <slot />
  </div>
</template>

<script>
export default {
  name: 'OrderTab',
  props: {
    selected: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      isActive: false,
    };
  },
  created() {
    this.isActive = this.selected;
  },
};
</script>

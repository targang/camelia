<template>
  <div class="col-md order-md-first">
    <div class="card border-0 shadow rounded mx-auto">
      <div class="card-body">
        <h4 class="card-title">Оформление заказа</h4>

        <slot />

        <div class="order-progress">
          <div class="order-progress--bar">
            <div
              class="order-progress--bar-completed"
              :style="
                `width: ${parseInt(
                  ((activeCount - 1) / (tabs.length - 1)) * 100
                )}%`
              "
            ></div>
          </div>
          <div
            v-for="(tab, index) in tabs"
            :key="`tab-${index}`"
            class="order-progress--point"
            :class="{
              active: tab.isActive,
              complete: index < activeCount,
            }"
          ></div>
        </div>

        <div class="d-flex">
          <button
            class="btn btn-secondary mx-1"
            :class="{ disabled: activeCount == 1 }"
            @click="prevTab"
          >
            Назад
          </button>
          <button
            class="btn btn-primary mx-1"
            v-if="activeCount != tabs.length"
            @click="nextTab"
          >
            Вперед
          </button>
          <button v-else class="btn btn-primary mx-1">Завершить</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OrderForm',
  data() {
    return {
      tabs: [],
      activeCount: 1,
    };
  },
  mounted() {
    this.tabs = this.$children;
  },
  methods: {
    nextTab() {
      if (this.activeCount == this.tabs.length) return;
      this.tabs[this.activeCount - 1].isActive = false;

      this.activeCount += 1;
      this.tabs[this.activeCount - 1].isActive = true;
    },
    prevTab() {
      if (this.activeCount == 1) return;
      this.tabs[this.activeCount - 1].isActive = false;

      this.activeCount -= 1;
      this.tabs[this.activeCount - 1].isActive = true;
    },
  },
};
</script>

<style lang="scss" scoped>
.order-progress {
  margin-top: 2rem;
  margin-bottom: 1.5rem;
  margin-left: auto;
  margin-right: auto;

  max-width: 300px;
  position: relative;
  display: flex;
  justify-content: space-between;

  &--bar {
    position: absolute;
    left: 0;
    right: 0;
    height: 3px;
    background-color: #e2e2e2;
    z-index: 0;

    &-completed {
      transition: width ease 0.5s;
      height: 100%;
      background-color: #800000;
    }
  }
  &--point {
    width: 1rem;
    height: 1rem;
    border-radius: 50%;
    z-index: 1;
    transform: translateY(-50%);
    background-color: #ffffff;
    border: 3px solid rgb(212, 212, 212);
    box-shadow: 0 0 0 0.1rem rgba(212, 212, 212, 0.9), 0 0 0 0.6rem #ffffff;

    &.complete {
      border-color: #800000;
      box-shadow: 0 0 0 0.1rem rgba(147, 38, 38, 0.9), 0 0 0 0.6rem #ffffff;
    }

    &.active {
      border-color: #800000;
      box-shadow: 0 0 0 0.4rem rgba(147, 38, 38, 0.9), 0 0 0 0.9rem #ffffff;
    }
  }
}
</style>

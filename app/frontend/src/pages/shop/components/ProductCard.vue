<template>
  <div class="col-12 col-sm-6 col-md-4 col-lg-3 my-3">
    <div class="card product-item border-0 h-100">
      <img :src="imgsrc" class="card-img-top product-img mx-auto" />
      <div class="card-body d-flex flex-column">
        <h4 class="card-title">{{ title }}</h4>
        <p class="card-text mt-auto">{{ price }},00₽</p>
        <button
          data-target="#addCartModal"
          data-toggle="modal"
          class="btn btn-primary add-cart"
          @click="addToCart"
        >
          Купить
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProductCart',
  props: {
    imgsrc: String,
    title: String,
    price: Number,
    productId: Number,
  },
  methods: {
    addToCart() {
      this.$emit('buy-click', {
        productId: this.productId,
        imgsrc: this.imgsrc,
        title: this.title,
        price: this.price,
      });
    },
  },
};
</script>

<style lang="scss">
.product-img {
  max-width: 400px;
}
</style>

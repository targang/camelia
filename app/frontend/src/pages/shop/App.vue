<template>
  <div id="app">
    <base-navbar :count="cartCount" />

    <section class="container py-4">
      <h2 class="mb-4">Магазин</h2>

      <div class="row py-md-4">
        <product-card
          v-for="product in products"
          :imgsrc="product.imagePath"
          :title="product.title"
          :product-id="parseInt(product.id)"
          :price="parseInt(product.price)"
          :key="product.vendorCode"
          @buy-click="buyClick"
        />
      </div>
    </section>

    <cart-modal
      :product-id="modalList.productId"
      :imgsrc="modalList.imgsrc"
      :title="modalList.title"
      :price="modalList.price"
      @submit-add="submitAdd"
    />

    <base-footer />
  </div>
</template>

<script>
import BaseNavbar from '../../components/BaseNavbar';
import BaseFooter from '../../components/BaseFooter';

import ProductCard from './components/ProductCard';
import CartModal from './components/CartModal';

export default {
  name: 'App',
  components: {
    BaseNavbar,
    BaseFooter,
    ProductCard,
    CartModal,
  },
  data() {
    return {
      products: [],
      modalList: {
        productId: null,
        imgsrc: '',
        title: '',
        price: null,
      },
      cartCount: 0,
    };
  },
  methods: {
    buyClick(list) {
      this.modalList = list;
    },
    submitAdd(count) {
      console.log(count);
      this.cartCount = parseInt(count);
    },
  },
  created() {
    fetch('/cart/length')
      .then((responce) => {
        return responce.json();
      })
      .then((data) => {
        this.cartCount = parseInt(data.data.count);
      });
    fetch('/get_products')
      .then((responce) => {
        return responce.json();
      })
      .then((data) => {
        this.products = data.data.products;
      });
  },
};
</script>

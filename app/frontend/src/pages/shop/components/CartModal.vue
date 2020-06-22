<template>
  <div
    class="modal fade bd-example-modal-lg show"
    id="addCartModal"
    role="dialog"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body p-4 p-md-5">
          <div class="row d-flex mb-4">
            <img
              :src="imgsrc"
              id="cardModalImg"
              class="img-fluid w-50 rounded mx-auto"
              alt=""
            />
          </div>
          <h4 class="modal-title text-center mb-3">{{ title }}</h4>
          <p class="modal-text text-center">{{ price * count }},00₽</p>
          <div class="d-flex justify-content-center">
            <div class="flex-column mr-2">
              <input
                class="form-control"
                type="number"
                min="1"
                name="product_count"
                id="product_count"
                v-model="count"
              />
            </div>
            <div class="flex-column ml-2">
              <button class="btn btn-primary" @click.prevent="submitAdd">
                Добавить в корзину
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import $ from 'jquery';

export default {
  name: 'CartModal',
  data() {
    return { count: 1 };
  },
  props: {
    productId: Number,
    imgsrc: String,
    title: String,
    price: Number,
  },
  methods: {
    submitAdd() {
      fetch('add_to_cart', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          productId: this.productId.toString(),
          productCount: this.count.toString(),
        }),
      })
        .then((responce) => {
          return responce.json();
        })
        .then((data) => {
          this.$emit('submit-add', data.data.count);
        });
      $('#addCartModal').modal('hide');
    },
  },
};
</script>

<style lang="scss" scoped>
input[name='product_count'] {
  width: 70px;
  border-radius: 8px;
}
</style>

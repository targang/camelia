<template>
  <transition name="fadeout">
    <tr>
      <th>{{ title }}</th>
      <td class="d-table-cell d-md-none">
        <span>{{ price }},00₽</span>
        <input
          class="form-control cart-count-field"
          type="number"
          :name="productId + '-count'"
          :id="productId + '-count'"
          v-model="countData"
          min="1"
        />
      </td>
      <td class="d-none d-md-table-cell cart-cost">{{ price }},00₽</td>
      <td class="d-none d-md-table-cell cccount">
        <input
          class="form-control cart-count-field"
          type="number"
          :name="productId + '-count'"
          :id="productId + '-count'"
          v-model="countData"
          min="1"
        />
      </td>

      <td class="sum-cart-el">{{ price * countData }},00₽</td>
      <td>
        <a href="javascript:void(0)" @click="deleteClick" class="text-danger"
          ><fa-icon :icon="['fas', 'trash']"
        /></a>
      </td>
    </tr>
  </transition>
</template>

<script>
export default {
  name: 'CartTr',
  props: {
    productId: {
      type: Number,
      required: true,
    },
    title: {
      type: String,
      required: true,
    },
    price: {
      type: Number,
      required: true,
    },
    count: {
      type: Number,
      required: true,
    },
  },
  data() {
    return { countData: this.count };
  },
  methods: {
    deleteClick() {
      // Запрос на сервер
      fetch('/cart/remove', {
        method: 'POST',
        body: JSON.stringify({ productId: this.productId.toString() }),
      })
        .then((response) => {
          if (!response.ok) throw Error(response.statusText);
          return response.json();
        })
        .then((data) => {
          // Вызываем событие delete-click
          this.$emit('delete-click', {
            count: data.data.count,
            id: this.productId,
          });
        })
        .catch((error) => console.error(error));
    },
  },
  watch: {
    countData: function(after, before) {
      // Валидация значения
      if (!before || before < 1 || before % 1 !== 0 || before === after) return;

      let isValid = true;
      if (!after || after < 1) {
        isValid = false;
        after = 1;
      }
      if (after % 1 !== 0) {
        isValid = false;
        after = parseInt(after);
      }

      // Разница
      let dif = after - before;

      // Запрос на сервер
      fetch('/cart/add', {
        method: 'POST',
        body: JSON.stringify({
          productId: this.productId.toString(),
          productCount: dif.toString(),
        }),
      })
        .then((response) => {
          if (!response.ok) throw Error(response.statusText);
        })
        .then(() => {
          this.$emit('count-change', { id: this.productId, count: after });
        });

      if (!isValid) this.countData = after;
    },
  },
};
</script>

<style lang="scss" scoped>
.cart-count-field {
  width: 60px !important;
}
.fadeout {
  &-enter-active,
  &-leave-active {
    transition: opacity ease-out 0.3s;
  }
  &-enter,
  &-leave-to {
    opacity: 0;
  }
}
</style>

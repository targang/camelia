<template>
  <div class="d-flex align-items-end flex-column">
    <div
      class="card shadow table-responsive border-0"
      style="max-width: 532px;"
    >
      <div class="card-body">
        <h2 class="card-title">Сумма заказов</h2>
        <table class="table my-3">
          <tbody>
            <tr class="">
              <th scope="row"><span class="text-uppercase">Подытог</span></th>
              <td class="total-summary">{{ sum }}₽</td>
            </tr>
            <tr class="">
              <th scope="row"><span class="text-uppercase">Доставка</span></th>
              <td>
                Стоимость доставки будет подсчитана во время оформления покупки.
              </td>
            </tr>
            <tr class="">
              <th scope="row"><span class="text-uppercase">Итого</span></th>
              <td>
                <strong class="total-summary">{{ sum }}₽</strong>
              </td>
            </tr>
          </tbody>
        </table>
        <a href="/checkout" class="btn btn-primary">Оформить заказ</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Totalcard',
  props: {
    sum: {
      type: Number,
      required: true,
    },
  },
};
</script>

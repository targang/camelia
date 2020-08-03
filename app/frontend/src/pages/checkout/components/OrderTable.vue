<template>
  <div class="col-md order-md-last">
    <div class="card border-0 shadow-md mx-2">
      <div class="card-body">
        <h4 class="card-title">Ваш заказ</h4>

        <div class="table-responsive mt-3">
          <table class="table mb-sm-0">
            <tbody>
              <slot />
              <tr>
                <th class="text-uppercase">Сумма</th>
                <td>{{ total }},00₽</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OrderTable',
  props: {
    total: {
      type: Number,
      required: true,
    },
  },
};
</script>

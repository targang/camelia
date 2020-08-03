<template>
  <tr>
    <th>{{ title }} x{{ count }}</th>
    <td>{{ price }},00₽</td>
  </tr>
</template>

<script>
export default {
  name: 'OrderItem',
  props: {
    title: {
      type: String,
      required: true,
    },
    count: {
      type: Number,
      required: true,
    },
    price: {
      type: Number,
      required: true,
    },
  },
};
</script>

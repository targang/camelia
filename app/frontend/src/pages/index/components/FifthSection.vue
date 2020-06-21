<template>
  <div class="container py-5">
    <div class="row">
      <div class="col-md text-center px-4">
        <div
          class="shadow-lg border border-light rounded-circle mx-auto mb-3 features-icon"
        >
          <fa-icon :icon="['fas', 'dollar-sign']"></fa-icon>
        </div>
        <h4>Выгодная цена</h4>
        <p style="font-size: large;">
          Цена зефирной глины Camelia Flowers Soft Вас приятно удивит
        </p>
      </div>
      <div class="col-md text-center px-4">
        <div
          class="shadow-lg border border-light rounded-circle mx-auto mb-3 features-icon"
        >
          <fa-icon :icon="['fas', 'award']"></fa-icon>
        </div>
        <h4>Качество</h4>
        <p style="font-size: large;">
          Зефирная глина для лепки цветов Camelia Flowers Soft обладает отличным
          качеством при невысокой цене
        </p>
      </div>
      <div class="col-md text-center px-4">
        <div
          class="shadow-lg border border-light rounded-circle mx-auto mb-3 features-icon"
        >
          <fa-icon :icon="['fas', 'truck']"></fa-icon>
        </div>
        <h4>Доставка по России</h4>
        <p style="font-size: large;">
          Почта России, CDEK, Boxberry, DPD, СберЛогистика — самые выгодные
          тарифы доставки
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FifthSection',
};
</script>

<style lang="scss">
.features-icon {
  width: 100px;
  height: 100px;
  font-size: 40px;
  position: relative;
  svg {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
}
</style>

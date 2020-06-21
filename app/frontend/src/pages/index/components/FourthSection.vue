<template>
  <div class="container py-5">
    <h1 class="text-center">Нас рекомендуют</h1>
    <div class="row">
      <div class="col-12 col-md-4">
        <div class="card border-0">
          <div class="card-body">
            <div class="recommend-img rounded-circle mx-auto">
              <img
                class="rounded-circle mx-auto d-block"
                src="../assets/stuff/ludmilaevteeva.jpg"
                alt=""
              />
            </div>
            <h4 class="my-3 card-title text-center">Людмила Евтеева</h4>
            <h1 class="card-title text-center">
              <a class="instagram-icon mx-2" href="#"
                ><fa-icon :icon="['fab', 'instagram']"></fa-icon></a
              ><a class="vk-icon mx-2" href="#"
                ><fa-icon :icon="['fab', 'vk']"></fa-icon
              ></a>
            </h1>
          </div>
        </div>
      </div>

      <div class="col-12 col-md-4">
        <div class="card border-0">
          <div class="card-body">
            <div class="recommend-img rounded-circle mx-auto">
              <img
                class="rounded-circle mx-auto d-block"
                src="../assets/stuff/venerasafina.jpg"
                alt=""
              />
            </div>
            <h4 class="my-3 card-title text-center">Венера Сафина</h4>
            <h1 class="card-title text-center">
              <a class="instagram-icon mx-2" href="#"
                ><fa-icon :icon="['fab', 'instagram']"></fa-icon></a
              ><a class="vk-icon mx-2" href="#"
                ><fa-icon :icon="['fab', 'vk']"></fa-icon
              ></a>
            </h1>
          </div>
        </div>
      </div>

      <div class="col-12 col-md-4">
        <div class="card border-0">
          <div class="card-body">
            <div class="recommend-img rounded-circle mx-auto">
              <img
                class="rounded-circle mx-auto d-block"
                src="../assets/stuff/mariyagarbuzova.jpg"
                alt=""
              />
            </div>
            <h4 class="my-3 card-title text-center">Мария Гарбузова</h4>
            <h1 class="card-title text-center">
              <a class="instagram-icon mx-2" href="#"
                ><fa-icon :icon="['fab', 'instagram']"></fa-icon></a
              ><a class="vk-icon mx-2" href="#"
                ><fa-icon :icon="['fab', 'vk']"></fa-icon
              ></a>
            </h1>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FourthSection',
};
</script>

<style>
.recommend-img {
  width: 158px;
  padding: 4px;
  background: linear-gradient(
    45deg,
    #f09433 0%,
    #e6683c 25%,
    #dc2743 50%,
    #cc2366 75%,
    #bc1888 100%
  );
}
</style>

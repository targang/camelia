<template>
  <nav
    class="navbar navbar-expand-lg navbar-light bg-white shadow-sm fixed-top"
    :class="{ 'navbar-hide': !showNavbar }"
  >
    <div class="container">
      <div class="navbar-brand flex-column">
        <a class="navbar-brand" href="/">
          <h3>Camelia Flowers</h3>
        </a>
        <hr class="my-0" />
        <small class="font-italic d-inline-block d-lg-none">
          <a class="navbar-icon mx-2 facebook-icon" href="#">
            <fa-icon :icon="['fab', 'facebook']"></fa-icon>
          </a>
          <a class="navbar-icon mx-2 instagram-icon" href="#">
            <fa-icon :icon="['fab', 'instagram']"></fa-icon>
          </a>
          <a class="navbar-icon mx-2 vk-icon" href="#">
            <fa-icon :icon="['fab', 'vk']"></fa-icon>
          </a>
          <a class="navbar-icon mx-2 whatsapp-icon" href="#">
            <fa-icon :icon="['fab', 'whatsapp']"></fa-icon>
          </a>
          <a class="navbar-icon mx-2" href="#">
            <fa-icon :icon="['far', 'envelope']"></fa-icon>
          </a>
          <a class="navbar-icon mx-2" href="#">
            <fa-icon :icon="['fas', 'phone-alt']"></fa-icon>
          </a>
        </small>
        <small class="font-italic d-none d-lg-inline-block"
          >Творить может каждый!</small
        >
      </div>

      <button
        class="navbar-toggler navbar-toggler-right align-self-center border-0"
        type="button"
        data-toggle="collapse"
        data-target="#navbar-collapse"
        style="position: relative;"
      >
        <span class="navbar-toggler-icon"></span>
        <div
          id="nav-noti"
          style="width: 8px;height:8px;position: absolute;right: 12px;bottom: 6px;"
          class="rounded-circle bg-danger"
        ></div>
      </button>
      <div
        class="collapse navbar-collapse flex-column ml-lg-0 ml-3 mt-1 mt-lg-0"
        id="navbar-collapse"
      >
        <div class="flex-column ml-auto">
          <ul class="navbar-nav flex-row d-none d-lg-flex mb-lg-2">
            <li class="nav-item">
              <a class="nav-link py-1 pr-3 facebook-icon" href="#">
                <fa-icon :icon="['fab', 'facebook']"></fa-icon>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link py-1 pr-3 instagram-icon" href="#">
                <fa-icon :icon="['fab', 'instagram']"></fa-icon>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link py-1 pr-3 vk-icon" href="#">
                <fa-icon :icon="['fab', 'vk']"></fa-icon>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link py-1 pr-3 whatsapp-icon" href="#">
                <fa-icon :icon="['fab', 'whatsapp']"></fa-icon>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link py-1 pr-3" href="#">shop@camelia-flowers.ru</a>
            </li>
            <li class="nav-item">
              <a class="nav-link py-1 pr-3" href="#">+7 905 025-34-85</a>
            </li>
            <li class="nav-item disabled">
              <a class="nav-link py-1 pr-3" href="#">Пн-Пт 8.00-17.00</a>
            </li>
          </ul>
          <ul class="navbar-nav justify-content-around mt-lg-2">
            <li class="nav-item">
              <a class="nav-link font-weight-bolder text-uppercase" href="#"
                >Магазин</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link font-weight-bolder text-uppercase" href="#">
                Корзина
                <span class="badge badge-pill badge-danger" id="cart-count"
                  >0</span
                >
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link font-weight-bolder text-uppercase" href="#"
                >Оформление заказа</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link font-weight-bolder text-uppercase" href="#">
                Личный кабинет
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'BaseNavbar',
  data() {
    return { showNavbar: true, lastScroll: 0 };
  },
  methods: {
    navbarOnScroll() {
      let scroll = window.pageYOffset || document.documentElement.scrollTop;
      if (scroll < 0) return;

      if (Math.abs(scroll - this.lastScroll) < 60) {
        return;
      }

      this.showNavbar = scroll < this.lastScroll;
      this.lastScroll = scroll;
    },
  },
  mounted() {
    window.addEventListener('scroll', this.navbarOnScroll);
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.navbarOnScroll);
  },
};
</script>

<style lang="scss">
.navbar {
  transition: transform 0.5s ease;
  &-hide {
    transform: translateY(-100%);
  }
  &-toggler {
    &:focus {
      outline: none;
    }
  }
  &-icon {
    color: rgba($color: #000000, $alpha: 0.5);
  }
}
</style>

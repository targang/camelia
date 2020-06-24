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
          <a
            class="navbar-icon mx-2 facebook-icon"
            href="https://www.facebook.com/safneaflowers"
          >
            <fa-icon :icon="['fab', 'facebook']"></fa-icon>
          </a>
          <a
            class="navbar-icon mx-2 instagram-icon"
            href="https://www.instagram.com/safnea_flowers"
          >
            <fa-icon :icon="['fab', 'instagram']"></fa-icon>
          </a>
          <a
            class="navbar-icon mx-2 vk-icon"
            href="https://vk.com/safnea_flowers"
          >
            <fa-icon :icon="['fab', 'vk']"></fa-icon>
          </a>
          <a
            class="navbar-icon mx-2 whatsapp-icon"
            href="https://wa.me/79050253485"
          >
            <fa-icon :icon="['fab', 'whatsapp']"></fa-icon>
          </a>
          <a class="navbar-icon mx-2" href="mailto:shop@camelia-flowers.ru">
            <fa-icon :icon="['far', 'envelope']"></fa-icon>
          </a>
          <a class="navbar-icon mx-2" href="tel:79050253485">
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
        <div id="nav-noti" v-if="count" class="rounded-circle bg-danger"></div>
      </button>
      <div
        class="collapse navbar-collapse flex-column ml-lg-0 ml-3 mt-1 mt-lg-0"
        id="navbar-collapse"
      >
        <div class="flex-column ml-auto">
          <ul class="navbar-nav flex-row d-none d-lg-flex mb-lg-2">
            <li class="nav-item">
              <a
                class="nav-link py-1 pr-3 facebook-icon"
                href="https://www.facebook.com/safneaflowers"
              >
                <fa-icon :icon="['fab', 'facebook']"></fa-icon>
              </a>
            </li>
            <li class="nav-item">
              <a
                class="nav-link py-1 pr-3 instagram-icon"
                href="https://www.instagram.com/safnea_flowers"
              >
                <fa-icon :icon="['fab', 'instagram']"></fa-icon>
              </a>
            </li>
            <li class="nav-item">
              <a
                class="nav-link py-1 pr-3 vk-icon"
                href="https://vk.com/safnea_flowers"
              >
                <fa-icon :icon="['fab', 'vk']"></fa-icon>
              </a>
            </li>
            <li class="nav-item">
              <a
                class="nav-link py-1 pr-3 whatsapp-icon"
                href="https://wa.me/79050253485"
              >
                <fa-icon :icon="['fab', 'whatsapp']"></fa-icon>
              </a>
            </li>
            <li class="nav-item">
              <a
                class="nav-link py-1 pr-3"
                href="mailto:shop@camelia-flowers.ru"
                >shop@camelia-flowers.ru</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link py-1 pr-3" href="tel:79050253485"
                >+7 905 025-34-85</a
              >
            </li>
            <li class="nav-item disabled">
              <span class="nav-link py-1 pr-3">Пн-Пт 8.00-17.00</span>
            </li>
          </ul>
          <ul class="navbar-nav justify-content-around mt-lg-2">
            <li class="nav-item">
              <a
                class="nav-link nav-link-primary font-weight-bolder text-uppercase"
                href="/shop"
                >Магазин</a
              >
            </li>
            <li class="nav-item">
              <a
                class="nav-link nav-link-primary font-weight-bolder text-uppercase"
                href="/cart"
              >
                Корзина
                <span
                  class="badge badge-pill badge-danger"
                  id="cart-count"
                  v-if="count"
                  >{{ count }}</span
                >
              </a>
            </li>
            <li class="nav-item">
              <a
                class="nav-link nav-link-primary font-weight-bolder text-uppercase"
                href="/checkout"
                >Оформление заказа</a
              >
            </li>
            <li class="nav-item">
              <a
                class="nav-link nav-link-primary font-weight-bolder text-uppercase"
                href="/auth"
              >
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
  props: {
    count: Number,
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
#nav-noti {
  width: 8px;
  height: 8px;
  position: absolute;
  right: 12px;
  bottom: 6px;
}
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
.nav-link {
  position: relative;
  color: rgba(0, 0, 0, 0.7) !important;

  @media screen and (min-width: 991.98px) {
    &-primary::after {
      background: none repeat scroll 0 0 transparent;
      content: '';
      display: block;
      height: 2px;
      left: 50%;
      bottom: 5px;
      position: absolute;
      background: rgba(0, 0, 0, 0.6);
      transition: width 0.5s ease 0s, left 0.5s ease 0s;
      width: 0;
    }
    &-primary:hover {
      color: #000000;
      &::after {
        width: 90%;
        left: 5%;
      }
    }
  }
}
</style>

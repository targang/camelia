<template>
  <div id="app">
    <base-navbar :count="cartCount" />

    <section class="container py-5" v-if="cartCount">
      <div class="row">
        <order-table :total="totalSum">
          <order-item
            v-for="item in orderItems"
            :key="`item-${item.id}`"
            :title="item.title"
            :price="parseInt(item.price)"
            :count="parseInt(item.count)"
          />
        </order-table>
        <order-form>
          <order-tab :selected="true">
            <div class="form-group">
              <label for="name">Имя</label>
              <input
                type="text"
                class="form-control"
                name="name"
                v-model="formName"
              />
              <div class="invalid-feedback">
                Заполните это поле
              </div>
            </div>
            <div class="form-group">
              <label for="surname">Фамилия</label>
              <input
                type="text"
                class="form-control"
                name="surname"
                v-model="formSurname"
              />
              <div class="invalid-feedback">
                Заполните это поле
              </div>
            </div>
            <div class="form-group">
              <label for="phone">Телефон</label>
              <input
                type="phone"
                class="form-control"
                name="phone"
                v-model="formPhone"
              />
              <div class="invalid-feedback">
                Заполните это поле
              </div>
            </div>
            <div class="form-group">
              <label for="email">Эл. почта</label>
              <input
                type="email"
                class="form-control"
                name="email"
                v-model="formEmail"
              />
              <div class="invalid-feedback">
                Заполните это поле
              </div>
            </div>
          </order-tab>
          <order-tab>
            <div class="form-group">
              <label for="country">Страна</label>
              <vue-single-select
                placeholder=""
                :options="countryList.map((country) => country.name)"
                input-id="country"
                v-model="formCountry"
                value=""
              />
              <div class="invalid-feedback">
                Заполните это поле
              </div>
            </div>
            <div class="form-group">
              <label :for="formCountry === 'Россия' ? 'city-s' : 'city'"
                >Населенный пункт</label
              >
              <vue-single-select
                placeholder=""
                :options="
                  cityList
                    ? cityList.map(
                        (city) => `${city.name}, ${city.administrativeArea}`
                      )
                    : []
                "
                :disabled="!formCountry"
                input-id="city-s"
                v-model="formCity"
                v-show="formCountry === 'Россия'"
                value=""
              />
              <input
                class="form-control"
                :disabled="!formCountry"
                name="city"
                id="city"
                type="text"
                v-model="formCity"
                v-show="formCountry !== 'Россия'"
              />
            </div>
            <div class="form-group">
              <label for="address">Адрес</label>
              <input
                type="text"
                class="form-control"
                name="address"
                v-model="formAddress"
              />
            </div>
            <div class="form-group">
              <label for="zip">Индекс</label>
              <input
                type="text"
                class="form-control"
                name="zip"
                v-model="formZip"
              />
            </div>
          </order-tab>
          <order-tab>
            <div class="form-group">
              <label for="message">Примечание к заказу (необязательно)</label>
              <textarea
                name="message"
                id="message"
                class="form-control"
                rows="5"
              ></textarea>
            </div>
            <div class="form-group form-group-check">
              <p class="mb-1">Способ оплаты</p>
              <div class="form-check">
                <input
                  type="radio"
                  class="form-check-input"
                  name="payment"
                  id="payment-1"
                />
                <label for="payment-1" class="form-check-label"
                  >Онлайн оплата</label
                >
              </div>
              <div class="form-check">
                <input
                  type="radio"
                  class="form-check-input"
                  name="payment"
                  id="payment-2"
                />
                <label for="payment-2" class="form-check-label"
                  >Оплатить на почте</label
                >
              </div>
            </div>
            <div class="form-group form-group-check">
              <p class="mb-2">Служба доставки</p>
              <div
                class="form-check mb-2"
                v-for="(method, index) in shipmentMethods"
                :key="`shipment-${index}`"
              >
                <input
                  type="radio"
                  name="shipment"
                  class="form-check-input"
                  v-model="shipmentMethod"
                  :value="method.name"
                  :id="`shipment-${index}`"
                />
                <label :for="`shipment-${index}`" class="form-check-label"
                  >{{ method.name }} — {{ method.cost }}
                  <br />
                  <span class="text-muted font-weight-light">{{ method.days }}</span></label
                >
              </div>
            </div>
          </order-tab>
        </order-form>
      </div>
    </section>

    <section
      class="vh-100 d-flex align-items-center justify-content-center"
      v-else
    >
      <div
        class="card border-0 text-center align-items-center"
        style="max-width: 350px;"
      >
        <div class="mb-3" style="width: 150px;">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            version="1.1"
            id="Capa_1"
            x="0px"
            y="0px"
            viewBox="0 0 231.523 231.523"
            style="enable-background:new 0 0 231.523 231.523;"
            xml:space="preserve"
          >
            <g>
              <path
                d="M107.415,145.798c0.399,3.858,3.656,6.73,7.451,6.73c0.258,0,0.518-0.013,0.78-0.04c4.12-0.426,7.115-4.111,6.689-8.231   l-3.459-33.468c-0.426-4.12-4.113-7.111-8.231-6.689c-4.12,0.426-7.115,4.111-6.689,8.231L107.415,145.798z"
              />
              <path
                d="M154.351,152.488c0.262,0.027,0.522,0.04,0.78,0.04c3.796,0,7.052-2.872,7.451-6.73l3.458-33.468   c0.426-4.121-2.569-7.806-6.689-8.231c-4.123-0.421-7.806,2.57-8.232,6.689l-3.458,33.468   C147.235,148.377,150.23,152.062,154.351,152.488z"
              />
              <path
                d="M96.278,185.088c-12.801,0-23.215,10.414-23.215,23.215c0,12.804,10.414,23.221,23.215,23.221   c12.801,0,23.216-10.417,23.216-23.221C119.494,195.502,109.079,185.088,96.278,185.088z M96.278,216.523   c-4.53,0-8.215-3.688-8.215-8.221c0-4.53,3.685-8.215,8.215-8.215c4.53,0,8.216,3.685,8.216,8.215   C104.494,212.835,100.808,216.523,96.278,216.523z"
              />
              <path
                d="M173.719,185.088c-12.801,0-23.216,10.414-23.216,23.215c0,12.804,10.414,23.221,23.216,23.221   c12.802,0,23.218-10.417,23.218-23.221C196.937,195.502,186.521,185.088,173.719,185.088z M173.719,216.523   c-4.53,0-8.216-3.688-8.216-8.221c0-4.53,3.686-8.215,8.216-8.215c4.531,0,8.218,3.685,8.218,8.215   C181.937,212.835,178.251,216.523,173.719,216.523z"
              />
              <path
                d="M218.58,79.08c-1.42-1.837-3.611-2.913-5.933-2.913H63.152l-6.278-24.141c-0.86-3.305-3.844-5.612-7.259-5.612H18.876   c-4.142,0-7.5,3.358-7.5,7.5s3.358,7.5,7.5,7.5h24.94l6.227,23.946c0.031,0.134,0.066,0.267,0.104,0.398l23.157,89.046   c0.86,3.305,3.844,5.612,7.259,5.612h108.874c3.415,0,6.399-2.307,7.259-5.612l23.21-89.25C220.49,83.309,220,80.918,218.58,79.08z    M183.638,165.418H86.362l-19.309-74.25h135.895L183.638,165.418z"
              />
              <path
                d="M105.556,52.851c1.464,1.463,3.383,2.195,5.302,2.195c1.92,0,3.84-0.733,5.305-2.198c2.928-2.93,2.927-7.679-0.003-10.607   L92.573,18.665c-2.93-2.928-7.678-2.927-10.607,0.002c-2.928,2.93-2.927,7.679,0.002,10.607L105.556,52.851z"
              />
              <path
                d="M159.174,55.045c1.92,0,3.841-0.733,5.306-2.199l23.552-23.573c2.928-2.93,2.925-7.679-0.005-10.606   c-2.93-2.928-7.679-2.925-10.606,0.005l-23.552,23.573c-2.928,2.93-2.925,7.679,0.005,10.607   C155.338,54.314,157.256,55.045,159.174,55.045z"
              />
              <path
                d="M135.006,48.311c0.001,0,0.001,0,0.002,0c4.141,0,7.499-3.357,7.5-7.498l0.008-33.311c0.001-4.142-3.356-7.501-7.498-7.502   c-0.001,0-0.001,0-0.001,0c-4.142,0-7.5,3.357-7.501,7.498l-0.008,33.311C127.507,44.951,130.864,48.31,135.006,48.311z"
              />
            </g>
            <g></g>
            <g></g>
            <g></g>
            <g></g>
            <g></g>
            <g></g>
            <g></g>
            <g></g>
            <g></g>
            <g></g>
            <g></g>
            <g></g>
            <g></g>
            <g></g>
            <g></g>
          </svg>
        </div>
        <div class="card-body">
          <h4 class="card-title">Ваша корзина пуста</h4>
          <a href="/shop" class="btn btn-primary mt-3">Перейти в магазин</a>
        </div>
      </div>
    </section>

    <base-footer />
  </div>
</template>

<script>
import BaseNavbar from '../../components/BaseNavbar';
import BaseFooter from '../../components/BaseFooter';

import VueSingleSelect from '../../../node_modules/vue-single-select';

import OrderTable from './components/OrderTable';
import OrderItem from './components/OrderItem';
import OrderForm from './components/OrderForm';
import OrderTab from './components/OrderTab';

export default {
  name: 'App',
  components: {
    BaseNavbar,
    BaseFooter,
    OrderTable,
    OrderItem,
    OrderForm,
    OrderTab,
    VueSingleSelect,
  },
  data() {
    return {
      cartCount: 0,
      orderItems: [],
      countryList: [],
      cityList: [],
      shipmentMethods: [],

      formName: '',
      formSurname: '',
      formPhone: '',
      formEmail: '',
      formCountry: '',
      formCity: '',
      formAddress: '',
      formZip: '',
      shipmentMethod: '',
    };
  },
  watch: {
    formCountry: function(val) {
      // Следим за вводом города
      var cityListener = (e) => {
        let city = e.target.value;

        fetch(`/checkout/get_cities?query=${city}`)
          .then((response) => {
            return response.json();
          })
          .then((data) => {
            // Подставляем значения из Shiptor API
            this.cityList = data.data.cities;
          });
      };

      if (!val) {
        this.formCity = null;
      }

      if (val !== 'Россия') {
        this.cityList = [];
      } else {
        document
          .querySelector('#city-s')
          .removeEventListener('input', cityListener);

        document
          .querySelector('#city-s')
          .addEventListener('input', cityListener);
      }
    },
    formCity: function(val) {
      if (!val) return;

      let kladr;

      for (const city of this.cityList) {
        if (`${city.name}, ${city.administrativeArea}` === val) {
          kladr = city.kladrId;
        }
      }

      fetch('/checkout/calculate_shipping', {
        method: 'POST',
        body: JSON.stringify({
          city: kladr,
        }),
      })
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          this.shipmentMethods = data.data;
        });
    },
  },
  computed: {
    totalSum: function() {
      let total = 0;
      for (const item of this.orderItems) {
        total += parseInt(item.count) * parseInt(item.price);
      }
      return total;
    },
  },
  created() {
    fetch('/cart/length')
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        this.cartCount = parseInt(data.data.count);
      });

    fetch('/cart/items')
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        this.orderItems = data.data;
      });

    fetch('/checkout/get_countries')
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        this.countryList = this.countryList.concat(data.data.countryList);
      });
  },
};
</script>

<style lang="scss">
#app {
  padding-top: 91px;
}
.search-input:focus {
  color: #495057;
  background-color: #fff;
  border-color: #ff0101;
  outline: 0;
  box-shadow: 0 0 0 0.2rem rgba(128, 0, 0, 0.25);
}
</style>

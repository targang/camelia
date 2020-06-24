<template>
  <footer class="footer">
    <div class="top-footer">
      <div class="container py-5">
        <div class="row">
          <div class="col-sm-6 col-md-3">
            <a class="footer-link" href="/howto_checkout">Как оформить заказ</a
            ><br />
            <a class="footer-link" href="/delivery_terms">Условия доставки</a
            ><br />
            <a class="footer-link" href="/return_conditions">Условия возврата</a
            ><br />
          </div>
          <div class="col-sm-6 col-md-9">
            <a class="footer-link" href="/public_offer">Публичная оферта</a
            ><br />
            <a class="footer-link" href="/privacy_policy"
              >Положение об обработке персональных данных</a
            ><br />
            <a class="footer-link" href="/concent">Согласие</a><br />
          </div>
        </div>
      </div>
    </div>
    <div class="bottom-footer">
      <div class="container py-3" style="color: #777777;font-size: small;">
        <p style="margin-bottom: 10px;">
          © 2020
          <a class="footer-link" href="/">Camelia Flowers</a>
          – Все права защищены
        </p>
        <p style="margin-bottom: 10px;">
          Designed by
          <a class="footer-link" href="https://sverstaem.site/">Amema Studio</a>
        </p>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'BaseFooter',
};
</script>

<style lang="scss">
.footer {
  position: absolute;
  bottom: 0;
  width: 100%;
}
.top-footer {
  background-color: #313131;
}
.bottom-footer {
  background-color: #282828;
}
.footer-link {
  color: #8f8f8f;
  font-size: small;
  &:hover {
    color: #ffffff;
  }
}
</style>

module.exports = {
  publicPath: '/dist/',
  pages: {
    index: {
      entry: 'src/pages/index/main.js',
      template: 'public/index.html',
      filename: 'index.html',
      title: 'Camelia Flowers | Творить может каждый',
    },
    shop: {
      entry: 'src/pages/shop/main.js',
      template: 'public/index.html',
      filename: 'shop.html',
      title: 'Каталог | Camelia Flowers',
    },
    cart: {
      entry: 'src/pages/cart/main.js',
      template: 'public/index.html',
      filename: 'cart.html',
      title: 'Корзина | Camelia Flowers',
    },
    checkout: {
      entry: 'src/pages/checkout/main.js',
      template: 'public/index.html',
      filename: 'checkout.html',
      title: 'Оформление заказа | Camelia Flowers',
    },
  },
  devServer: {
    proxy: {
      '^/static': {
        target: 'http://127.0.0.1:5000',
      },
      '^/shop/all': {
        target: 'http://127.0.0.1:5000',
      },
      '^/cart/length': {
        target: 'http://127.0.0.1:5000',
      },
      '^/cart/items': {
        target: 'http://127.0.0.1:5000',
      },
      '^/cart/add': {
        target: 'http://127.0.0.1:5000',
      },
      '^/cart/remove': {
        target: 'http://127.0.0.1:5000',
      },
      '^/checkout/get_countries': {
        target: 'http://127.0.0.1:5000',
      },
      '^/checkout/get_cities': {
        target: 'http://127.0.0.1:5000',
      },
      '^/checkout/calculate_shipping': {
        target: 'http://127.0.0.1:5000',
      },
    },
  },
};

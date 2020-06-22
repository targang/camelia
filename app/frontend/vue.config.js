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
  },
  devServer: {
    proxy: {
      ['^/cart']: {
        target: 'http://127.0.0.1:5000',
      },
      ['^/checkout']: {
        target: 'http://127.0.0.1:5000',
      },
      ['^/auth']: {
        target: 'http://127.0.0.1:5000',
      },
      ['^/static']: {
        target: 'http://127.0.0.1:5000',
      },
      ['^/get_products']: {
        target: 'http://127.0.0.1:5000',
      },
      ['^/add_to_cart']: {
        target: 'http://127.0.0.1:5000',
      },
      ['^/get_cart_length']: {
        target: 'http://127.0.0.1:5000',
      },
    },
  },
};

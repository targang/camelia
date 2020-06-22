module.exports = {
  publicPath: '/dist/',
  pages: {
    index: {
      entry: 'src/pages/index/main.js',
      template: 'public/index.html',
      filename: 'index.html',
      title: 'Camelia Flowers | Творить может каждый',
    },
  },
  devServer: {
    proxy: {
      ['^/shop']: {
        target: 'http://localhost:5000',
      },
      ['^/cart']: {
        target: 'http://localhost:5000',
      },
      ['^/checkout']: {
        target: 'http://localhost:5000',
      },
      ['^/auth']: {
        target: 'http://localhost:5000',
      },
      ['^/static']: {
        target: 'http://localhost:5000',
      },
    },
  },
};

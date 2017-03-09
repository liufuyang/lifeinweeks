// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueD3 from 'vue-d3'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.css'
import VueResource from 'vue-resource'
import VeeValidate from 'vee-validate'

import { store } from './store'

Vue.use(VueMaterial)
Vue.use(VueD3)
Vue.use(VueResource)
Vue.use(VeeValidate)

Vue.material.registerTheme('default', {
  primary: 'orange',
  accent: 'teal'
  // warn: 'red'
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})

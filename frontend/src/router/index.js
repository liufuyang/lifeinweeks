import Vue from 'vue'
import Router from 'vue-router'
import Home from 'components/Home'
import Hello from 'components/Hello'
import Sandbox from 'components/Sandbox'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/about',
      name: 'Hello',
      component: Hello
    },
    {
      path: '/s',
      name: 'Sandbox',
      component: Sandbox
    }
  ]
})

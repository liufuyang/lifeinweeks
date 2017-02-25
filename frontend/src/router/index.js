import Vue from 'vue'
import Router from 'vue-router'
import Home from 'components/Home'
import Hello from 'components/Hello'
import WeekCalendar from 'components/WeekCalendar'
import Sandbox from 'components/Sandbox'
import D3 from 'components/D3'
import DemoVuex from 'components/DemoVue/DemoVuex'

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
      path: '/week',
      name: 'WeekCalendar',
      component: WeekCalendar
    },
    {
      path: '/s',
      name: 'Sandbox',
      component: Sandbox
    },
    {
      path: '/d',
      name: 'D3',
      component: D3
    },
    {
      path: '/demo-vuex',
      name: 'DemoVuex',
      component: DemoVuex
    }
  ]
})

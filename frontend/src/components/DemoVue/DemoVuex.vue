<template>
  <div id="demo-vuex">
    <app-registration></app-registration>
    <app-registrations></app-registrations>
  </div>
</template>

<script>
import Registration from './DemoRegistration.vue'
import Registrations from './DemoRegistrations.vue'
export default {
  components: {
    appRegistration: Registration,
    appRegistrations: Registrations
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

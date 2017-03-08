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

<template>
  <div id="app">
    <md-layout md-align="end" md-gutter="16">
      <md-layout md-flex-xsmall="33" md-flex-small="33" md-flex-medium="20" md-flex="10" >
        <user-auth></user-auth>
      </md-layout>
    </md-layout>

    <!-- <img src="./assets/logo.png"> -->
    <router-view></router-view>

    <md-card>
      <md-card-content>
        <div class="md-subhead">
          Frontend powered by Vue.js. @ 2017 lifeinweeks
        </div>
      </md-card-content>
    </md-card>

  </div>
</template>

<script>
import UserAuth from './components/utils/UserAuth'

export default {
  name: 'app',
  components: {
    'user-auth': UserAuth
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
  margin-top: 5px;
  margin-left: 30px;
  margin-right: 30px;
}
</style>

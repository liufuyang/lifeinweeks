<template>
  <div class="home">
    <md-card>
      <md-card-header>
        <div class="md-title">
          {{ msg }}
        </div>
        <div class="md-subhead">
          by lifeinweeks.ml
        </div>
      </md-card-header>
      <md-card-content>
        <md-button class="md-raised md-primary"
          v-on:click="fillTable()">Fill table
        </md-button>
      </md-card-content>
    </md-card>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      msg: 'Welcome to Life in Weeks!'
    }
  }
}
</script>

<template>
  <div id="registrations">
    <div class="summary">
      <h3>Registrations</h3>
      <h5>Total: {{ total }}</h5>
    </div>
    <hr>
    <div class="row" v-for="registration in registrations">
      <h4>{{ registration.name }}</h4>
      <span @click="unregister(registration)">(Unregister)</span>
      <div class="date">{{ registration.date }}</div>
    </div>
  </div>
</template>

<script>
// Sweet part:
import { mapGetters } from 'vuex'

export default {
  computed: {
    ...mapGetters({ // ES2015 feature. https://www.youtube.com/watch?v=iw1eajzWQAM&index=2&list=PL55RiY5tL51pT0DNJraU93FhMzhXxtDAo
      registrations: 'registrations',
      total: 'totalNumberOfRegistrations'
    }),
    justAnotherOne () {
      return true
    }
  },
  // computed: {
  //   registrations () {
  //     return this.$store.getters.registrations
  //   },
  //   total () {
  //     return this.$store.getters.totalNumberOfRegistrations
  //   }
  // },
  methods: {
    unregister (registration) {
      // this.$store.commit({
      //   type: 'unregister',
      //   userId: registration.userId
      // })
      this.$store.commit('unregister', registration)
    }
  }
}
</script>

<style scoped>
#registrations {
  box-shadow: 1px 1px 2px 1px #ccc;
  margin: 20px;
  padding: 20px;
  display: inline-block;
  width: 300px;
  vertical-align: top;
  text-align: left;
}
.summary {
  text-align: center;
}
.row h4 {
  display: inline-block;
  width: 30%;
  margin: 0 0 10px 0;
  box-sizing: border-box;
}
.row span {
  width: 30%;
  color: red;
  cursor: pointer;
}
.row span:hover {
  color: darkred;
}
.date {
  display: inline-block;
  width: 38%;
  text-align: right;
  box-sizing: border-box;
}
</style>

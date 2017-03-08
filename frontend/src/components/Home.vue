<template>
  <div class="home">
    <md-card>
      <md-card-header>
        <div class="md-title">
          {{ msg }}
        </div>
        <div v-show="false" class="md-subhead">
          by lifeinweeks.ml
        </div>
      </md-card-header>
      <md-card-content>
        <div v-show="!authenticated" class="md-subheading">
          <span>Enter your birthday here or login</span>
        </div>
        <date-picker v-show="!authenticatedAndBirthdayUpdated"></date-picker>

        <md-card-content v-show="authenticated">
          <div class="md-subheading">
            <span>See how many weeks have passed in your life...</span>
          </div>
          <div class="md-subheading">
            Carpe Diem
          </div>
          <div class="md-subheading">
            {{time}}
          </div>
        </md-card-content>

        <week-calendar></week-calendar>

      </md-card-content>

      <div v-show="!authenticated">
        <div class="md-title">
          Carpe Diem
        </div>
        <div class="md-subheading">
          {{time}}
        </div>
      </div>
    </md-card>
    <br />
  </div>
</template>

<script>
import WeekCalender from './WeekCalendar'
import DatePicker from './utils/DatePicker'
import UserAuth from './utils/UserAuth'

export default {
  name: 'home',
  data () {
    return {
      msg: 'Welcome to Life in Weeks!',
      time: updateTime(this)
    }
  },
  computed: {
    authenticated () {
      return this.$store.getters.isAuthenticated
    },
    authenticatedAndBirthdayUpdated () {
      return this.$store.getters.isAuthenticated && this.$store.getters.isBirthdayUpdatedViaLogin
    }
  },
  components: {
    'week-calendar': WeekCalender,
    'date-picker': DatePicker,
    'user-auth': UserAuth
  }
}

function updateTime (obj) {
  let interval = setInterval(() => {
    let val = generateTimeString().next()
    if (val.done) {
      clearInterval(interval)
    } else {
      obj.time = val.value
      return obj.time
    }
  }, 31)
}

function* generateTimeString () {
  while (true) {
    let time = new Date()
    let ms = time.getMilliseconds()
    ms = '000' + ms
    ms = ms.substr(ms.length - 3)
    yield time.toLocaleTimeString() + ' \'' + ms
  }
}
</script>

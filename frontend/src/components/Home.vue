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
        <div class="md-title">
          Under Construction
        </div>
        <div class="md-subheading">
          {{time}}
        </div>
      </md-card-header>
      <md-card-content>
        <date-picker></date-picker>
        <week-calendar></week-calendar>
      </md-card-content>
    </md-card>
  </div>
</template>

<script>
import WeekCalender from './WeekCalendar'
import DatePicker from './utils/DatePicker'
export default {
  name: 'home',
  data () {
    return {
      msg: 'Welcome to Life in Weeks!',
      time: updateTime(this)
    }
  },
  components: {
    'week-calendar': WeekCalender,
    'date-picker': DatePicker
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

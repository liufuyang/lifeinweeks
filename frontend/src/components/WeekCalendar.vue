<template>
  <div class="week-calendar">
    <svg>
    </svg>
    <div v-show="false">
      {{userBirthday}}
    </div>
  </div>
</template>


<script>
import _ from 'lodash'

const CELL_SIZE = 8
const COLOR_POOL = ['#35495e', '#41b883']

let WeekCalendar = {
  name: 'week-calendar',
  data () {
    return {
      message: ''
    }
  },
  methods: {

  },
  computed: {
    userBirthday () {
      // TODO this will be updated twice during initiate, which might be a bug
      // https://github.com/marcosmoura/vue-material/issues/590
      updateWeekView(this, this.$store.getters.userBirthday)

      return this.$store.getters.userBirthday
    }
  },
  mounted () {
    _init_.call(this)
  },
  components: {
  }
}

function _init_ () {
  // An init method called when component is mounted
  this.$http.get('/api/get').then(
    response => {
      initDraw.call(this, response.body)
    },
    response => {}
  )
}

let updateWeekView = _.debounce(function (vm, birthday) {
  // TODO this will be updated twice during initiate, which might be a bug
  // https://github.com/marcosmoura/vue-material/issues/590
  // We use debounce here to get over doulbe api calling
  console.log('updating week view via calling backend')

  vm.$http.post('/api/week-data', {birthday: birthday}).then(
    response => {
      updateDraw.call(vm, response.body)
    },
    response => {}
  )
}, 200)

function initDraw (data) {
  // data = [
  //   {year_num: 0, week_num: 0}, {year_num: 0, week_num: 1},
  //   {year_num: 1, week_num: 0}, {year_num: 1, week_num: 1}
  // ]
  let scale = this.$d3.scaleLinear()
    .domain([0, 90]) // Data space
    .range([0, 900]) // Pixel space

  let svg = this.$d3.select('svg')
  svg.attr('width', 520)
  svg.attr('height', 900)

  svg.selectAll('rect').data(data).enter().append('rect')
    .attr('x', function (d) { return scale(d.week_num) }) // function (d, i) { return i * CELL_SIZE }
    .attr('y', function (d) { return scale(d.year_num) })
    .attr('width', CELL_SIZE)
    .attr('height', CELL_SIZE)
    .style('fill', d => COLOR_POOL[d.color])
}

function updateDraw (data) {
  this.$d3.select('svg').selectAll('rect').data(data)
    .style('fill', d => COLOR_POOL[d.color])
}

export default WeekCalendar

</script>

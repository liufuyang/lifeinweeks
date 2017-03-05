<template>
  <div class="week-calendar">
    <svg>
    </svg>
  </div>
</template>


<script>
let WeekCalendar = {
  name: 'week-calendar',
  data () {
    return {
      message: ''
    }
  },
  methods: {

  },
  mounted () {
    _init_.call(this)
  }
}

function _init_ () {
  this.$http.get('/api/get').then(
    response => {
      draw.call(this, response.body)
    },
    response => {}
  )
}

function draw (data) {
  let cellSize = 8
  let colorPool = ['#ff5722', '#0fffff']
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
    .attr('x', function (d) { return scale(d.week_num) }) // function (d, i) { return i * cellSize }
    .attr('y', function (d) { return scale(d.year_num) })
    .attr('width', cellSize)
    .attr('height', cellSize)
    .style('fill', d => colorPool[d.color])
}
export default WeekCalendar

</script>

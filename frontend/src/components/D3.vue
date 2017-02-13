<template>
  <div class="d3-sandbox">
    <p>
      This is a paragraph
    </p>
  </div>
</template>


<script>
let D3Sandbox = {
  name: 'd3-sandbox',
  data () {
    return {
    }
  },
  methods: {
  },
  mounted () {
    _init_.call(this)
  }
}

function _init_ () {
  this.$d3.select('p').text('Hello world')

  let canvas = this.$d3.select('p')
    .append('svg')
    .attr('width', 500)
    .attr('height', 500)

  canvas.append('circle')
    .attr('cx', 250)
    .attr('cy', 250)
    .attr('r', 50)
    .attr('fill', 'red')

  canvas.append('rect')
    .attr('width', 100)
    .attr('height', 50)

  canvas.append('line')
    .attr('x1', 0)
    .attr('y1', 100)
    .attr('x2', 400)
    .attr('y2', 400)
    .attr('stroke', 'green')
    .attr('stroke-width', 5)
}

export default D3Sandbox

</script>

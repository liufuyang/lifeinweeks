<template>
  <div class="d3-sandbox">
    <p>
      This is a paragraph
    </p>
    <form novalidate @submit.stop.prevent="submit">
    <md-input-container>
      <label>Try type something here</label>
      <md-input type="text" :value="msg" v-on:input.native="changeOutsideComponentMessage"/>
    </md-input-container>
    <p>
      {{ message }}
    </p>
  </form>
  </div>
</template>


<script>
let D3Sandbox = {
  name: 'd3-sandbox',
  props: ['msg'], // used for passing values into this component
  data () {
    return {
      message: ''
    }
  },
  methods: {
    changeOutsideComponentMessage (event) {
      this.message = event.target.value
      this.$emit('messageChanged', this.message)
    }
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
    .attr('r', 100)
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

<template>
  <div class="hello">
    <br />

    <md-card>
      <md-card-header>
        <div class="md-title">
          About lifeinweeks
        </div>
        <div class="md-subhead">
          cap diem, seize the day
        </div>
        <br />
        <div class="md-subheading">
          {{time}}
        </div>
      </md-card-header>
      <md-card-content>
        <md-button class="md-icon-button md-raised md-accent">
          <md-icon>thumb_up</md-icon>
        </md-button>
      </md-card-content>
    </md-card>

    <h2>Essential Links</h2>
    <ul>
      <li><a href="https://vuejs.org" target="_blank">Core Docs</a></li>
      <li><a href="https://forum.vuejs.org" target="_blank">Forum</a></li>
      <li><a href="https://gitter.im/vuejs/vue" target="_blank">Gitter Chat</a></li>
      <li><a href="https://twitter.com/vuejs" target="_blank">Twitter</a></li>
      <br>
      <li><a href="http://vuejs-templates.github.io/webpack/" target="_blank">Docs for This Template</a></li>
    </ul>
    <h2>Ecosystem</h2>
    <ul>
      <li><a href="http://router.vuejs.org/" target="_blank">vue-router</a></li>
      <li><a href="http://vuex.vuejs.org/" target="_blank">vuex</a></li>
      <li><a href="http://vue-loader.vuejs.org/" target="_blank">vue-loader</a></li>
      <li><a href="https://github.com/vuejs/awesome-vue" target="_blank">awesome-vue</a></li>
    </ul>
  </div>
</template>

<script>
const Sandbox = {
  name: 'hello',
  data () {
    return {
      time: updateTime(this)
    }
  },
  methods: {
  }
}

export default Sandbox

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

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>

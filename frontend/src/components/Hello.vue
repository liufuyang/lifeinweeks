<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
  </br>
    <md-card>
      <md-card-header>
        <div class="md-title">
          Material Design with Vue.js 2 Demo Card
        </div>
        <div class="md-subhead">
          by lifeinweeks.ml
        </div>
      </md-card-header>
      <md-card-content>
        <md-button class="md-raised md-primary" @click.native="fillTable()">Fill
        </md-button>
        <md-button class="md-raised"  @click.native="clearTable()">Clear
        </md-button>
        <md-button class="md-icon-button md-raised md-primary">
          <md-icon>message</md-icon>
        </md-button>
        <md-button class="md-icon-button md-raised md-accent">
          <md-icon>add</md-icon>
        </md-button>
        <md-button class="md-icon-button md-raised md-accent">
          <md-icon>thumb_up</md-icon>
        </md-button>
        <md-button class="md-icon-button md-raised md-warn">
          <md-icon>send</md-icon>
        </md-button>
      </md-card-content>
      
      <md-table>
        <md-table-header>
          <md-table-row>
            <md-table-head>Name</md-table-head>
            <md-table-head>Phone</md-table-head>
            <md-table-head>Email</md-table-head>
          </md-table-row>
        </md-table-header>
        <md-table-body>
          <md-table-row v-for="contact in contacts">
            <md-table-cell>{{contact.name}}</md-table-cell>
            <md-table-cell>{{contact.phone}}</md-table-cell>
            <md-table-cell>{{contact.email}}</md-table-cell>
          </md-table-row>
        </md-table-body>
      </md-table>
      
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
    
    <div id="example-1">
      <button v-on:click="clearTable()">Clear table</button>
      <p>The clear table button above has been clicked {{ counter }} times.</p>
    </div>
  
  </div>
</template>

<script>
export default {
  name: 'hello',
  data () {
    return {
      counter: 0,
      msg: 'Welcome to Your Vue.js App',
      contacts: [{
        name: 'Sebastian',
        phone: '11223344',
        email: 'secret@google.com'
      }]
    }
  },
  methods: {
    fillTable: function () {
      this.contacts.push({
        name: 'Sebastian',
        phone: '11223344',
        email: 'secret@google.com'
      })

      this.contacts.push({
        name: 'Johannes',
        phone: '44332211',
        email: 'doom@google.com'
      })
    },
    clearTable: function () {
      console.log('fillTable clicked')
      this.counter += 1
      this.contacts.splice(0, this.contacts.length)
    }
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

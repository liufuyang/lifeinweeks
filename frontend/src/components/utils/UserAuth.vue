<template>
  <div class="user-auth">
        <md-button @click.native="login()" v-show="!authenticated" class="md-primary">Login</md-button>
        <md-button @click.native="logout()" v-show="authenticated">Logout</md-button>
  </div>
</template>

<script>
import Auth0Lock from 'auth0-lock'

export default {
  name: 'user-auth',
  data () {
    return {
      lock: new Auth0Lock('zgoOpRtyeelzaDnHsJuH8d2kpG1n0wK7', 'liufuyang.eu.auth0.com')
    }
  },
  computed: {
    authenticated () {
      return this.$store.getters.isAuthenticated
    }
  },
  mounted () {
    // check and save initial state
    this.$store.dispatch('setAuthenticated', checkAuth())
    this.lock.on('authenticated', (authResult) => {
      console.log('authenticated')
      localStorage.setItem('id_token', authResult.idToken)
      this.lock.getProfile(authResult.idToken, (error, profile) => {
        if (error) {
          // Handle error
          console.log(error)
          return
        }
        // console.log(profile)
        // Set the token and user profile in local storage
        localStorage.setItem('profile', JSON.stringify(profile))
        localStorage.setItem('birthday', profile.birthday)

        this.$store.dispatch('setAuthenticated', true)

        if (profile.birthday) {
          const birthday = new Date(profile.birthday)
          if (birthday) {
            this.$store.dispatch('updateUserBirthday', birthday)
            localStorage.setItem('birthday_updated', 'true')
          }
        }
      })
    })
    this.lock.on('authorization_error', (error) => {
      // handle error when authorizaton fails
      console.log(error)
    })
  },
  methods: {
    login () {
      this.lock.show()
    },
    logout () {
      // To log out, we just need to remove the token and profile
      // from local storage
      localStorage.removeItem('id_token')
      localStorage.removeItem('profile')
      localStorage.removeItem('birthday')
      localStorage.removeItem('birthday_updated')
      this.$store.dispatch('setAuthenticated', false)
    }
    // Make a secure call to the server by attaching
    // the user's JWT as an Authorization header
    // getSecretThing () {
    //   var jwtHeader = { 'Authorization': 'Bearer ' + localStorage.getItem('id_token') }
    //   this.$http.get('/api/secured/ping', (data) => {
    //     console.log(data)
    //     this.secretThing = data.text
    //   }, {
    //     headers: jwtHeader
    //   }).error((err) => console.log(err))
    // }
  }
}

// Utility to check auth status
function checkAuth () {
  return !!localStorage.getItem('id_token')
}

// https://auth0.com/docs/connections/social/facebook
</script>

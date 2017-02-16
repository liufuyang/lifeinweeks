import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    registrations: [], // for demo purpose
    users: [ // for demo purpose
            {id: 1, name: 'Max', registered: false},
            {id: 2, name: 'Anna', registered: false},
            {id: 3, name: 'Chris', registered: false},
            {id: 4, name: 'Sven', registered: false}
    ],
    currentUserState: {
      login: false,
      birthday: null
    }
  },
  getters: {
    unregisteredUsers (state) { // for demo purpose
      return state.users.filter(user => !user.registered)
    },
    registrations (state) { // for demo purpose
      return state.registrations
    },
    totalNumberOfRegistrations (state) { // for demo purpose
      return state.registrations.length
    },
    isUserLoggedIn (state) {
      return state.currentUserState.login
    }
  }
})

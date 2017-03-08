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
    },
    user: {
      authenticated: !!localStorage.getItem('id_token'),
      birthday: _initAnonymBirthday(),
      birthdayUpdatedViaLogin: !!localStorage.getItem('birthday_updated')
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
    },
    // For lifeinweeks
    userBirthday (state) {
      return state.user.birthday
    },
    userBirthdayYear (state) {
      return state.user.birthday.getFullYear()
    },
    userBirthdayMonth (state) {
      return state.user.birthday.getMonth()
    },
    userBirthdayDate (state) {
      return state.user.birthday.getDate()
    },
    // For authentication
    isAuthenticated (state) {
      return state.user.authenticated
    },
    isBirthdayUpdatedViaLogin (state) {
      return state.user.birthdayUpdatedViaLogin
    }
  },
  mutations: { // no async allowed !!
    register (state, user) {
      const date = new Date()
      user.registered = true
      const registration = {
        userId: user.id,
        name: user.name,
        date: date.toLocaleDateString()}
      state.registrations.push(registration)
    },
    unregister (state, registration) {
      const user = state.users.find(user => user.id === registration.userId)
      user.registered = false
      state.registrations.splice(state.registrations.indexOf(registration), 1)
    },
    // For lifeinweeks
    updateuserbirthday (state, birthday) {
      state.user.birthday = birthday
      state.user.birthdayUpdatedViaLogin = true
    },
    updateuserbyear (state, year) {
      state.user.birthday = new Date(state.user.birthday)
      state.user.birthday.setFullYear(year)
    },
    updateuserbmonth (state, month) {
      state.user.birthday = new Date(state.user.birthday)
      state.user.birthday.setMonth(month)
    },
    updateuserbdate (state, date) {
      state.user.birthday = new Date(state.user.birthday)
      state.user.birthday.setDate(date)
    },
    // For authentication
    setauthenticated (state, authenticated) {
      state.user.authenticated = authenticated
    }
  },
  actions: {
    registerAsync (context, user) {
      setTimeout(() => {
        context.commit('register', user)
      }, 1000)
    },
    unregisterAsync ({ commit }, registration) {
      commit('unregister', registration)
    },
    // For lifeinweeks
    updateUserBirthday ({commit}, birthday) {
      commit('updateuserbirthday', birthday)
    },
    updateUserBirthdayYear ({commit}, year) {
      commit('updateuserbyear', year)
    },
    updateUserBirthdayMonth ({commit}, month) {
      commit('updateuserbmonth', month)
    },
    updateUserBirthdayDate ({commit}, date) {
      commit('updateuserbdate', date)
    },
    setAuthenticated ({commit}, authenticated) {
      commit('setauthenticated', authenticated)
    }
  }
})

function _initAnonymBirthday () {
  // Note that localStorage won't refresh with page refresh
  const birthday = localStorage.getItem('birthday')
  if (birthday) {
    return new Date(birthday)
  }
  let d = new Date()
  d.setFullYear(d.getFullYear() - 30)
  return d
}

<template>
  <div class="date-picker">

    <md-layout md-gutter="10" md-align="center">
      <md-layout md-flex-xsmall="100" md-flex-small="33" md-flex-medium="20" md-flex="10" md-flex-offset="1">
        <md-input-container v-bind:class="{ 'md-input-invalid': month_invalid}">
          <label for="month">Month</label>
          <md-select name="month" id="month" v-model="userBirthdayMonth">
            <md-option v-for="month in month_opt_en" v-bind:value="month.value">
              {{month.name}}
            </md-option>
          </md-select>
        </md-input-container>
      </md-layout>

      <md-layout md-flex-xsmall="100" md-flex-small="33" md-flex-medium="10" md-flex="5" md-flex-offset="5">
        <md-input-container v-bind:class="{ 'md-input-invalid': errors.has('user-birthday-date') || date_invalid}">
          <label>Date</label>
          <md-input
            v-model="userBirthdayDate" type="number"
            data-vv-name="user-birthday-date" v-validate="'between:1,31'"
          >
          </md-input>
        </md-input-container>
      </md-layout>

      <md-layout md-flex-xsmall="100" md-flex-small="33" md-flex-medium="10" md-flex="5" md-flex-offset="5">
        <md-input-container v-bind:class="{ 'md-input-invalid': errors.has('user-birthday-year') || year_invalid}">
          <label>Year</label>
          <md-input
            v-model="userBirthdayYear" type="number"
            data-vv-name="user-birthday-year" v-validate="'between:1900,2100'"
            >
          </md-input>
        </md-input-container>
      </md-layout>

    </md-layout>
  </div>
</template>

<script>
import _ from 'lodash'
// import moment from 'moment'

export default {
  name: 'date-picker',
  data () {
    return {
      month_opt: Array.from(new Array(12), (x, i) => i),
      month_opt_en: [
        {value: 0, name: 'January'},
        {value: 1, name: 'February'},
        {value: 2, name: 'March'},
        {value: 3, name: 'April'},
        {value: 4, name: 'May'},
        {value: 5, name: 'June'},
        {value: 6, name: 'July'},
        {value: 7, name: 'August'},
        {value: 8, name: 'September'},
        {value: 9, name: 'October'},
        {value: 10, name: 'November'},
        {value: 11, name: 'December'}
      ],
      date_invalid: false,
      month_invalid: false,
      year_invalid: false
    }
  },
  computed: {
    userBirthdayYear: {
      get () {
        return this.$store.getters.userBirthdayYear // using getters
      },
      set: _.debounce(function (year) {
        // validation
        this.year_invalid = false
        if (!validateMonth(
          year,
          this.$store.getters.userBirthday.getMonth(),
          this.$store.getters.userBirthday.getDate())) {
          this.year_invalid = true
          return
        }
        this.$store.commit('updateuserbyear', year) // use mutation, syncronized
        // this.$store.dispatch('updateUserBirthdayYear', year) // use action, asyncronized
      }, 1000)
    },
    userBirthdayMonth: {
      get () {
        return this.$store.getters.userBirthdayMonth // using getters
      },
      set (month) {
        // validation
        this.month_invalid = false
        if (!validateMonth(
          this.$store.getters.userBirthday.getFullYear(),
          month,
          this.$store.getters.userBirthday.getDate())) {
          this.month_invalid = true
          return
        }
        this.$store.dispatch('updateUserBirthdayMonth', month)
      }
    },
    userBirthdayDate: {
      get () {
        return this.$store.getters.userBirthdayDate // using getters
      },
      set: _.debounce(function (date) {
        // validation
        this.date_invalid = false
        if (!validateMonth(
          this.$store.getters.userBirthday.getFullYear(),
          this.$store.getters.userBirthday.getMonth(),
          date)) {
          this.date_invalid = true
          return
        }
        this.$store.dispatch('updateUserBirthdayDate', date) // use action, asyncronized
      }, 1000)
    }
  },
  methods: {
  },
  mounted () {
  }
}

function validateMonth (y, m, d) {
  if (y === '') return false
  if (m === '') return false
  if (d === '') return false
  // year between:1900,2100
  if (y < 1900 || y > 2100) return false
  // if (d < 1 || d > 31) return false

  // let r = moment({y: y, M: m, d: d}).isValid()
  return true
}

</script>

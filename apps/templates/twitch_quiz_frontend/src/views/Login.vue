<template>
  <h1>{{ msg }}</h1>
  <clock></clock>
</template>

<script>
import Clock from './../components/clock.vue';

export default {
  data () {
    return {
      msg: 'LOGIN'
    }
  },
  components: {
    Clock
  }
};
</script>

<style>

</style>

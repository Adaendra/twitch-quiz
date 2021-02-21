<template>
  <h1>{{ msg }}</h1>
  <clock></clock>
</template>

<script>
import Clock from '@/components/clock.vue';

export default {
  data () {
    return {
      msg: 'Welcome to Vue.js World!'
    }
  },
  components: {
    Clock
  }
};
</script>

<style>

</style>

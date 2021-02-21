<template>
  <!--<RwvHeader />-->
  <router-view></router-view>
  <!--<RwvFooter />-->
</template>

<script>
  import Clock from './components/clock.vue';

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
  body {
    font : 100% Helvetica, sans-serif;
    color: #ecf0f1;
    background-color: #34495e;
    overflow: hidden;
  }
  .container {
    position: absolute;
    top: 0px;
    left: 0px;
    width: 100%;
    height: 100%;
  }
</style>

<template>
  <!--<RwvHeader />-->
  <router-view></router-view>
  <!--<RwvFooter />-->
</template>

<script>
  export default {
    data () {
      return {}
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

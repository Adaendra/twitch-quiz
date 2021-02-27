<template>
  <h1>{{ msg }}</h1>
  <clock></clock>
</template>

<script>
import Clock from './../components/clock.vue';

const socket = io("localhost:5000");

export default {
  data () {
    return {
        msg: 'Home'
    }
  },
  methods: {
    test(json) {
      console.log('response :: ', json);
    }
  },
  mounted () {
    console.log('Mounted')
    socket.emit('my_event', {"message": "test"});
    socket.on('my_response', (json) => {
      console.log('response :: ', json);
    });
  },
  components: {
    Clock
  }
};
</script>

<style>

</style>

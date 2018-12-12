<template>
  <div id="app">
    <router-link v-bind:to="'/'">HelloArmy</router-link>
    <router-link v-bind:to="'/lyricsgen'">LyricsGen</router-link>
    <router-view></router-view>
  </div>
</template>

<script>
  export default {
    name: 'app',
  }
</script>

<style>
#app {
  font-family: 'Helvetica';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

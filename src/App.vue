<template>
  <div id="app">
    <app-header/>
    <!--
    <router-link v-bind:to="'/'">HelloArmy</router-link>
    <router-link v-bind:to="'/lyricsgen'">LyricsGen</router-link>
  -->
    <router-view/>
  </div>
</template>

<script>
  import Header from './components/Header.vue';
  export default {
    name: 'app',
    components:{
      appHeader: Header
    }
  }
</script>

<style>
#app {
  font-family: 'Helvetica';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 160px;
}

router-link{

}
</style>

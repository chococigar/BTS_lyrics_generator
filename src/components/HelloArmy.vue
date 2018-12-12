<template>
  <div class="helloarmy">
    <p>반가워요 Army</p>
    <p>당신의 이름은 무엇인가요?</p>
    <br>
    <p>HELLO BTS ARMY</p>
    <p>WHAT IS YOUR NAME?</p>
    <input id='userName' @keyup.enter="addMessage" v-model="userInput" type="text">
  </div>
</template>

<script>

  export default {
    name: 'helloarmy',
    data: function(){
      return {
        userInput:''
      }
    },
    methods:{
      addMessage(){
        this.$router.push({
          path: '/lyricsgen',
          query: {user: this.userInput}
        });
      }
    },
    props: {
      userName: {
        type: String,
        default: 'User'
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

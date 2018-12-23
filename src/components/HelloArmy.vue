<template>
  <div class="helloarmy">
    <div class="kor ques">
      <p>반가워요 BTS 아미</p>
      <p>당신의 이름은 무엇인가요?</p></div>
    <div class="eng ques">
      <p>HELLO BTS ARMY</p>
      <p>WHAT IS YOUR NAME?</p></div>
    <input id='userName' @keyup.enter="addMessage" v-model="userInput" placeholder="이름을 적어주세요" type="text">

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
.helloarmy{
  font-family: 'Typo_SsangmunDong';
  text-align: left;
  padding-left:172px;
  font-size:30px;
  margin-top:180px;
}

input{
    border:none;
    border-bottom: 2px #D3D3D3 solid;
    color: #D3D3D3;
    font-family: 'Typo_SsangmunDong';
    font-size:30px;
    margin:0px;
    padding:0px;
}

.ques{
  margin-bottom:40px;
}

</style>

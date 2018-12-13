<template>
  <div class="lyricsgen">
     <div id="mainnav" class="row">
          <ul style="order:0"><a>BTS Lyrics generator</a></ul>
          <ul style="order:1"><a>about</a></ul>
          <ul style="order:2"><a>shop</a></ul>
      </div>
      <div class="container">
          {{ generated_lyrics }}
          <ul class="buttonsbox">
              <button id="refresh" v-on:click='updateLyrics'>Nice!</button>
              <button id="refresh">Meh</button>
          </ul>
    </div>
    
    <!--<img src="@/assets/logo.png"/>-->
  </div>
</template>

<script>

  console.log("sup");

  var backgroundColors = [
      '#0080ff',
      '#ffbf00',
      '#01df3a',
      '#ff0080',
      '#9966ff',
      '#ff0033'
  ];

  var setRandomBackground = function() {
      var bgcolor = backgroundColors[Math.floor(Math.random() * backgroundColors.length)];
      $('body').css('background-color', bgcolor);
  }

  var markov_next = function(curr, probDict) {
      var keys = Object.keys(probDict);
      if (!(probDict.hasOwnProperty(curr))) {
          return keys[Math.floor(Math.random() * keys.length)];
      } else {
          var succProbs = probDict[curr];
          var randProb = Math.random();
          var currProb = 0;
          for (var succ in succProbs) {
              currProb += succProbs[succ];
              if (randProb <= currProb) return succ;
              return keys[Math.floor(Math.random() * keys.length)];
          }
      }
  }

  var newline_lyrics = function(l_array, min = 1, max = 6) {
      var words_left = l_array.length;
      var out_lyrics = "";
      var stanza_num = 0;
      var cur = 0;
      while (words_left >= 1) {
          stanza_num = min + Math.min(Math.floor(Math.random() * (max - min)), words_left);

          out_lyrics += l_array.slice(cur, cur + stanza_num).join(" ");
          out_lyrics += "<br>";
          words_left -= stanza_num;
          cur += stanza_num;
      }
      return out_lyrics;
  }

  var generate_lyrics = function(curr, probDict, T = 200, detail) {
      var lyrics = [curr];
      for (var t in Array.from({
              length: T
          }, (x, i) => i)) {
          var next_word = markov_next(lyrics[-1], probDict);
          console.log(next_word);
          lyrics.push(next_word);
          console.log(detail[next_word]);
          console.log(detail[next_word]['t']);
      }

      return lyrics.join(' ');
  }

  var show_lyrics = function(lpdict, startWord, detail) {
      var lyrics = generate_lyrics(startWord, lpdict, 12, detail);
      console.log("lyrics is : ", lyrics);
      return lyrics;
  }

  import HelloArmy from '../components/HelloArmy.vue';
  console.log("imported data : " , HelloArmy.data());


  import $ from 'jquery'
  //import lyricsProbDict from './../assets/testdict.json'
  import lyricsProbDict from './../../python/boy_meets_evil_freq.json'
  import words_detail from './../../python/words_detail.json'
  console.log(words_detail);
  console.log("asdf");
  setRandomBackground();

  export default {
    name: 'lyricsgen',
    data: function(){
      return{
        generated_lyrics: ''
      }
    },
    mounted() {
      this.generated_lyrics=show_lyrics(lyricsProbDict, this.$route.query.user, words_detail);
    },
    methods: {
      updateLyrics: function(){
        setRandomBackground();
        this.generated_lyrics = show_lyrics(lyricsProbDict, this.$route.query.user, words_detail);
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

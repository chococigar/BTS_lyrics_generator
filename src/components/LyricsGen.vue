<template>
  <div class="lyricsgen">
      <div class="container">
          <div id="gen">{{ generated_lyrics }}</div>
          <ul class="buttonsbox">
              <button id="refresh" v-on:click='updateLyrics'>Nice!</button>
              <button id="refresh">Meh</button>
          </ul>
    </div>
    
    <!--<img src="@/assets/logo.png"/>-->
  </div>
</template>

<script>
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

  var markov_next = function(curr, probDict, detail) {
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
      //var lyrics = [curr];
      var lyrics = curr+' ';
      for (var t in Array.from({
              length: T
          }, (x, i) => i)) {
          var next_word = markov_next(lyrics[-1], probDict, detail);
          //console.log("next word : ", next_word);
          
          console.log(next_word);
          console.log(detail[next_word]['t']);
          console.log(detail[next_word]['s']);
          console.log(detail[next_word]['e']);
          var hasNewline = Math.floor(Math.random()*3);
          console.log(hasNewline);
          if (hasNewline==1) next_word+='\n';
          else next_word+= ' ';
          //lyrics.push(next_word);
          lyrics += next_word;
      }
      //return lyrics.join(' ');
      return lyrics;
  }

  var show_lyrics = function(lpdict, startWord, detail) {
      var lyrics = generate_lyrics(startWord, lpdict, 12, detail);
      console.log("lyrics is : ", lyrics);
      return lyrics;
  }

  import HelloArmy from '../components/HelloArmy.vue';
  import $ from 'jquery'
  //import lyricsProbDict from './../assets/testdict.json'
  import lyricsProbDict from './../../python/Wings.json'
  import words_detail from './../../python/wings_detail.json'
  //setRandomBackground();

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
        //setRandomBackground();
        this.generated_lyrics = show_lyrics(lyricsProbDict, this.$route.query.user, words_detail);
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
p.c {
  white-space: pre;
}
.lyricsgen{
  font-family: 'Typo_SsangmunDong';
  text-align: left;
  padding-left:172px;
}
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
#gen{
  font-size:40px;
  white-space: pre;
}

</style>

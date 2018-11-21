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
    //$('li').css('background-color', bgcolor);
}

var sum = function(obj) {
    var sum = 0;
    for (var el in obj) {
        if (obj.hasOwnProperty(el)) {
            sum += parseFloat(obj[el]);
        }
    }
    return sum;
};

var make_dicts = function(file_data) {
    var n_words = file_data.replace(/\r?\n|\r/g, "<br> ");
    n_words = n_words.replace(/"/g, "").replace(/'/g, "").replace(/\(|\)/g, "");
    var words = n_words.split(" ");

    var freqDict = {};
    var curr, succ;

    for (var i = 0; i < words.length; ++i) {
        curr = words[i];
        succ = words[words.length - i - 1];
        if (!freqDict.hasOwnProperty(curr)) { //if doesn't exist
            freqDict[curr] = {};
            freqDict[curr][succ] = 1;
        } else {
            if (!(freqDict[curr].hasOwnProperty(succ))) {
                freqDict[curr][succ] = 1;
            } else {
                freqDict[curr][succ] += 1;
            }
        }
    }

    var probDict = {};

    for (var curr in freqDict) {
        probDict[curr] = {};
        var currTotal = sum(freqDict[curr]);
        for (var succ in freqDict[curr]) {
            probDict[curr][succ] = freqDict[curr][succ] / currTotal;
        }
    }
    return probDict;
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
    //phrases : 1~8
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

var generate_lyrics = function(curr, probDict, T = 200) {
    lyrics = [curr];
    for (var t in Array.from({
            length: T
        }, (x, i) => i)) {
        lyrics.push(markov_next(lyrics[-1], probDict));
    }
    return lyrics.join(' ');
    //return newline_lyrics(lyrics);
}

var show_lyrics = function() {
    var startWord = "지윤";
    var lyrics = generate_lyrics(startWord, lyricsProbDict, 12);
    console.log(lyrics);
    $('#lyricsbox').html(lyrics);
}

function get_file(path, callback) {
    return new Promise(function(resolve, reject) {
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4) { // The request is done; did it work?
                if (xhr.status == 200) {
                    resolve(xhr.responseText);
                } else {
                    reject(xhr);
                }
            }
        };
        xhr.open("GET", path);
        xhr.send();
    });
}

//no need to make lyrics prob dict all the time. 

get_file("./data/bts.txt")
    .then(function(data) {

        console.log(data);
        lyricsProbDict = make_dicts(data);
        console.log(lyricsProbDict);
        $('#refresh').on('click', function() {
            setRandomBackground();
            show_lyrics();
        });
        setRandomBackground();
        show_lyrics();

    })
    .catch(function(xhr) {
        console.log("error");
    });
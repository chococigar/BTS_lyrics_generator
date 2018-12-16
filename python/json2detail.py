import json
import glob
import os



with open('./wings_detail.json', encoding='utf-8') as feedsjson:
	dic = json.load(feedsjson)

#with open('lyrics_raw/Wings/Boy_meets_evil.json', encoding='utf-8') as feedsjson:
#	raw = json.load(feedsjson)

dic = {}
startbool = 0
endbool = 0

path = './lyrics_raw/Wings/*.json'


for filename in glob.glob(os.path.join(path)):
	with open(filename, 'r') as file:
		lyricsdic = json.load(file)
		title = lyricsdic['t']
		print("title : ", title)
		album = lyricsdic['a']
		verses = lyricsdic['verses']
		for verse in verses:#par.strip().split("\n"): 
			singers = verse['v']
			for line in verse['r'].strip().split("\n"):
				words = line.strip().split(" ")
				for i in range(len(words)):
					if i==0:
						startbool = 1
					if i==len(words)-1:
						endbool = 1
					dic[words[i]]={'t':title, 'a':album, 'v':singers, 's':startbool, 'e':endbool}
					startbool = 0
					endbool = 0
    # do your stuff

#WHEN PARSING :GET RID OF COMMA AND PARENTHESIS
"""
for verse in raw['verses']:#par.strip().split("\n"): 
	singers = verse['v']
	for line in verse['r'].strip().split("\n"):
		words = line.strip().split(" ")
		for i in range(len(words)):
			if i==0:
				startbool = 1
			if i==len(words)-1:
				endbool = 1
			dic[words[i]]={'t':song, 'a':album, 'v':singers, 's':startbool, 'e':endbool}
			startbool = 0
			endbool = 0
"""

with open('./wings_detail.json', mode='w', encoding='utf-8') as feedsjson:
	json.dump(dic, feedsjson, ensure_ascii=False)

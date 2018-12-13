import json

with open('./words_detail.json', encoding='utf-8') as feedsjson:
	dic = json.load(feedsjson)

with open('lyrics_raw/Wings/Boy_meets_evil.json', encoding='utf-8') as feedsjson:
	raw = json.load(feedsjson)

song = raw['t']
album = raw['a']
startbool = 0
endbool = 0

#WHEN PARSING :GET RID OF COMMA AND PARENTHESIS

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



#dic['요로']={'t':'bst', 'a':'wings', 'v':['v', 'jk'], 's':0, 'e':0}
	

with open('./words_detail.json', mode='w', encoding='utf-8') as feedsjson:
	json.dump(dic, feedsjson, ensure_ascii=False)
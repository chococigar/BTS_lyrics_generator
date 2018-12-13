# -*- coding: utf-8 -*-

import pickle
import json

#  jk jm v jin  jhope rm suga
# 'jk','jm','v','jin','jhope','rm','suga'
album = 'Wings'
filename = 'Am_I_wrong'

itemlist = {'t':filename,
'a':album,
'verses':[{'v':['rm'],
'r':"""The world's goin' crazy"""},
{'v':['jhope'],
'r':"""넌 어때 how bout ya"""},
{'v':['rm'],
'r':"""You think it is okay"""},
{'v':['suga'],
'r':"""난 좀 아닌 것 같어"""},
{'v':['rm'],
'r':"""귀가 있어도 듣질 않어
눈이 있어도 보질 않어
다 마음에 물고기가 살어
걔 이름 selfish selfish"""},
{'v':['suga'],
'r':"""우린 다 개 돼지 화나서 개 되지
황새 VS 뱁새 전쟁이야 errday"""},
{'v':['jhope'],
'r':"""미친 세상이 yeah
우릴 미치게 해
그래 우린 다 crazy
자 소리질러
Mayday mayday"""},
{'v':['v', 'jk'],
'r':"""온 세상이 다 미친 것 같아
끝인 것 같아
Oh why (Oh why)
Oh why (Oh why)
Oh why why why why
Oh my God"""},
{'v':['jk'],
'r':"""내가 뭐 틀린 말했어
내가 뭐 거짓말했어
미쳤어 미쳤어
미쳤어 미쳤어"""},
{'v':['jm'],
'r':"""Going crazy
Crazy
Am I wrong
Am I wrong"""},
{'v':['jk'],
'r':"""어디로 가는지
세상이 미쳐 돌아가네"""},
{'v':['rm'],
'r':"""Are you ready for this
Are you ready for this
Are you ready for this
(No I'm not)"""},
{'v':['jhope'],
'r':"""그램마 니가 미친겨
미친 세상에 안미친게 미친겨
온 천지 사방이
Hell Yeah
온라인 오프라인이
Hell Yeah"""},
{'v':['rm'],
'r':"""뉴스를 봐도 아무렇지 않다면
그 댓글이 아무렇지 않다면
그 증오가 아무렇지 않다면
넌 정상 아닌게 비정상"""},
{'v':['jin', 'jk'],
'r':"""온 세상이 다 미친 것 같아
끝인 것 같아
Oh why (Oh why)
Oh why (Oh why)
Oh why why why why
Oh my God"""},
{'v':['jk'],
'r':"""내가 뭐 틀린 말했어
내가 뭐 거짓말했어
미쳤어 미쳤어
미쳤어 미쳤어"""},
{'v':['jm'],
'r':"""Going crazy
Crazy
Am I wrong
Am I wrong"""},
{'v':['jm'],
'r':"""어디로 가는지
세상이 미쳐 돌아가네"""},
{'v':['jk'],
'r':"""미친 세상 길을 잃어도"""},
{'v':['jm'],
'r':"""아직은 더 살고 싶어
찾고 싶어 나의 믿음을"""},
{'v':['jk'],
'r':"""내가 뭐 틀린 말했어
내가 뭐 거짓말했어
미쳤어 미쳤어
미쳤어 미쳤어"""},
{'v':['jm'],
'r':"""Going crazy
Crazy
Am I wrong
Am I wrong"""},
{'v':['jk'],
'r':"""어디로 가는지
세상이 미쳐 돌아가네"""},
{'v':['rm'],
'r':"""Are you ready for this
Are you ready for this
Are you ready for this"""}
]}


with open('lyrics_raw/'+album+'/'+filename+'.json', mode='w', encoding='utf-8') as feedsjson:
	json.dump(itemlist, feedsjson, ensure_ascii=False)


with open('lyrics_raw/'+album+'/'+filename+'.json', encoding='utf-8') as feedsjson:
	dic = json.load(feedsjson)

print(dic['verses'][0]['r'])
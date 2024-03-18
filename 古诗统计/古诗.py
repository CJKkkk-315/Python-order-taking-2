import json
import jieba
from collections import Counter
with open('poet.song.1000.json','r',encoding='utf8')as fp:
    json_data = json.load(fp)
data = []
words = []
for i in json_data:
    for j in i["paragraphs"]:
        data.append(j)
        word = j.replace('，','').replace('。','')
        word = jieba.cut(word)
        for k in word:
            words.append(k)
print(Counter(data))
print(Counter(words))
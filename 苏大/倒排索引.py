import os
import jieba
from collections import Counter
ext = 'txt'
files = os.listdir(os.getcwd()+'\数据文件')
files = [i for i in files if i.split('.')[-1] == ext]
files.sort()
file_encode = {}
file_word_list = {}
stop_words = []
for i in range(len(files)):
    file_encode[files[i]] = i
with open('停用词/baidu_stopwords.txt','r',encoding='utf-8') as f:
    stop_words += f.readlines()
with open('停用词/cn_stopwords.txt','r',encoding='utf-8') as f:
    stop_words += f.readlines()
with open('停用词/scu_stopwords.txt','r',encoding='utf-8') as f:
    stop_words += f.readlines()
with open('停用词/hit_stopwords.txt','r',encoding='utf-8') as f:
    stop_words += f.readlines()
stop_words = list(map(lambda x:x[:len(x)-1],stop_words))
all_words = []
for i in files:
    print(i)
    with open('数据文件\\'+i,'r',encoding='utf-8') as f:
        words = []
        fc = jieba.cut(''.join(f.readlines()).replace('\n','').replace('\xa0','').replace('\t','').replace('.',''))
        for word in fc:
            if word not in stop_words:
                words.append(word)
    file_word_list[i] = words
    all_words += words
index = {}
n = len(Counter(all_words))
for i,j in Counter(all_words).items():
    print(n)
    t = []
    for k,l in file_word_list.items():
        if i in l:
            t.append(file_encode[k])
    t.insert(0,j)
    index[i] = t
with open('res/index.txt','w',encoding='utf-8') as f:
    for i,j in index.items():
        f.write(i + ' ' + ' '.join(list(map(str,j))) + '\n')
f.close()
import numpy as np
import pandas as pd
import math
split_ress = [[] for i in range(1000)]
import os
ext = 'txt'
files = os.listdir(os.getcwd()+'/数据文件')
files = [i for i in files if i.split('.')[-1] == ext]
files.sort()
file_decode = {}
for i in range(len(files)):
    file_decode[i] = files[i]
with open('res/index.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
for i in lines:
    line = i.replace('\n','').split(' ')
    word = line[0]
    for num in line[2:]:
        split_ress[int(num)].append(word)

# print(split_ress)
#1.声明文档 分词 去重合并
wordSet = set(split_ress[0])
for i in split_ress[1:]:
    wordSet = wordSet.union(i)

#2.统计词项tj在文档Di中出现的次数，也就是词频。
def computeTF(wordSet,split):
    tf = dict.fromkeys(wordSet, 0)
    for word in split:
        tf[word] += 1
    return tf
tfs = []
for i in split_ress:
    tfs.append(computeTF(wordSet,i))
#3.计算逆文档频率IDF
def computeIDF(tfList):
    idfDict = dict.fromkeys(tfList[0],0) #词为key，初始值为0
    N = len(tfList)  #总文档数量
    for tf in tfList: # 遍历字典中每一篇文章
        for word, count in tf.items(): #遍历当前文章的每一个词
            if count > 0 : #当前遍历的词语在当前遍历到的文章中出现
                idfDict[word] += 1 #包含词项tj的文档的篇数df+1
    for word, Ni in idfDict.items(): #利用公式将df替换为逆文档频率idf
        idfDict[word] = math.log10(N/Ni)  #N,Ni均不会为0
    return idfDict   #返回逆文档频率IDF字典
idfs = computeIDF(tfs)
# print('idfs:\n',idfs)

#4.计算tf-idf(term frequency–inverse document frequency)
def computeTFIDF(tf, idfs): #tf词频,idf逆文档频率
    tfidf = {}
    for word, tfval in tf.items():
        tfidf[word] = tfval * idfs[word]
    return tfidf
tfidfs = []
for i in tfs:
    tfidfs.append(computeTFIDF(i, idfs))
tfidf = pd.DataFrame(tfidfs)
# print(tfidf)
#5.查询与文档Q最相似的文章
aw = dict.fromkeys(wordSet, 0)
q = input()
split_q = q.split(' ')   #分词
for i in split_q:
    if i not in aw:
        split_q.remove(i)
tf_q = computeTF(wordSet,split_q) #计算Q的词频
tfidf_q = computeTFIDF(tf_q, idfs) #计算Q的tf_idf(构建向量)
ans = pd.DataFrame(tfidfs + [tfidf_q])
# print(ans)
res = []
#6.计算Q和文档Di的相似度（可以简单地定义为两个向量的内积）
b = sum(list(map(lambda x:x**2,list(ans.loc[1000,:]))))**0.5
for i in range(1000):
    nj = (ans.loc[i,:]*ans.loc[1000,:]).sum()
    a = sum(list(map(lambda x:x**2,list(ans.loc[i,:]))))**0.5
    res.append([i,nj/(a*b)])
res.sort(key=lambda x:x[1],reverse=True)
f = []
for i in res:
    if i[1] and not pd.isna(i[1]):
        f.append(i)
res = f[::]
for i in res:
    name = file_decode[i[0]]
    with open('数据文件/' + name, 'r', encoding='utf-8') as f:
        t = []
        sentences = f.readlines()
        for sentence in sentences:
            for sq in split_q:
                if sq in sentence:
                    t.append(sentence.replace('\n', ''))
                    break
        if t:
            print(name, end='  ')
            print(i[1])
            for s in t:
                print(s)
        print('\n',end='')
l = []
for i,j in dict(ans.loc[0,:]).items():
    if str(int(j)) != '0':
        l.append(i+' '+str(int(j))+'\n')
name = file_decode[0]
with open(name,'w',encoding='utf-8') as f:
    for i in l:
        f.write(i)

import jieba
from collections import Counter
import wordcloud
from PIL import Image
import matplotlib.pyplot as plt
import numpy
def readf():
    with open('data.txt','r',encoding='utf-8') as f:
        data = f.readlines()
    data = [i.replace('\n','').replace('\xa0','') for i in data if i != '\n']
    return '。'.join(data)
def cutword(content):
    object_list = []
    seg_list_exact = jieba.cut(content, cut_all=False, HMM=True)
    with open('停用词库.txt', 'r', encoding='UTF-8') as meaninglessFile:
        stopwords = set(meaninglessFile.read().split('\n'))
    stopwords.add(' ')
    # 打开停用词文件，将分词成果去掉所有的停用词
    for word in seg_list_exact:
        if word not in stopwords:
            object_list.append(word)
    for i in sorted(Counter(object_list).items(), key=lambda x: x[1], reverse=True):
        print(i[0],i[1])
    with open('cipin.txt','w') as f:
        for i,j in Counter(object_list).items():
            f.write(i+' '+str(j)+'\n')
    return object_list
def ciyun(object_list):
    d = Counter(object_list)
    w = []
    for i,j in d.items():
        w.append([i,j])
    w.sort(key=lambda x:x[1],reverse=True)
    w = w[:200]
    d = {i[0]:i[1] for i in w}
    wc = wordcloud.WordCloud(
        font_path='C:/Windows/Fonts/simfang.ttf',
        background_color='white',
        max_words=500,
        max_font_size=120
    )
    wc.generate_from_frequencies(d)
    plt.figure('词云')
    plt.subplots_adjust(top=0.99, bottom=0.01, right=0.99, left=0.01, hspace=0, wspace=0)
    plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis('off')
    plt.show()
content = readf()
object_list = cutword(content)
ciyun(object_list)

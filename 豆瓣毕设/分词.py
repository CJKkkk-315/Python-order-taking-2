import jieba
import csv
import hashlib
md = set()
content = []
with open('content.csv','r',encoding='utf-8') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        content.append(i[0])
object_list = []
for i in content[:5000]:
    #对每一条新闻内容，进行jieba分词处理，模式选择精确分词模式
    seg_list_exact = jieba.cut(i, cut_all=False, HMM=True)
    with open('停用词库.txt', 'r', encoding='UTF-8') as meaninglessFile:
        stopwords = set(meaninglessFile.read().split('\n'))
    stopwords.add(' ')
    #打开停用词文件，将分词成果去掉所有的停用词
    for word in seg_list_exact:
        if word not in stopwords:
            object_list.append(word)
    print(len(object_list))
with open('word.csv','w',encoding='utf-8',newline='') as f:
    f_csv = csv.writer(f)
    for i in object_list:
        f_csv.writerow([i])

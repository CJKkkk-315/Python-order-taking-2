import pandas as pd
import matplotlib.pyplot as plt
import wordcloud
from collections import Counter
import jieba
import numpy
from PIL import Image
df = pd.read_excel('夏洛特烦恼.xlsx')
print(df)
df = df[['score','city','comment']]
df.dropna(axis=0, how='any',inplace=True)
df.to_csv('清洗后数据.csv',encoding='utf-8')
print(df)
data =df.values.tolist()
s = [i[0] for i in data]
s = Counter(s)
xy = [[i,j] for i,j in s.items()]
xy.sort(key=lambda x:x[0])
x = [str(i[0]) for i in xy]
y = [i[1] for i in xy]
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.bar(x,y)
plt.show()
s = [i[1] for i in data]
s = Counter(s)
xy = [[i,j] for i,j in s.items()]
xy.sort(key=lambda x:x[1],reverse=True)
xy = xy[:20]
x = [str(i[0]) for i in xy]
y = [i[1] for i in xy]
plt.pie(x=y,labels=x)
plt.show()
s = [i[2] for i in data]
object_list = []
with open('停用词库.txt', 'r', encoding='UTF-8') as meaninglessFile:
    stopwords = set(meaninglessFile.read().split('\n'))
stopwords.add(' ')
for i in s:
    #对每一行内容，进行jieba分词处理，模式选择精确分词模式
    seg_list_exact = jieba.cut(i, cut_all=False, HMM=True)
    #打开停用词文件，将分词成果去掉所有的停用词
    for word in seg_list_exact:
        if word not in stopwords:
            object_list.append(word)
# 统计词语出现频率
object_list = Counter(object_list)
# 选择词云背景图
mask = numpy.array(Image.open('heart.png'))
# 设置词云参数
wc = wordcloud.WordCloud(
    font_path = 'C:/Windows/Fonts/simfang.ttf',
    background_color='white',
    mask = mask,
    max_words = 500,
    max_font_size = 120
)
# 生成词云对象
wc.generate_from_frequencies(Counter(object_list))
wc.recolor(color_func=wordcloud.ImageColorGenerator(mask))
plt.figure('词云')
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
# 显示词云
plt.show()
import pandas as pd
import jieba
import matplotlib.pyplot as plt
import wordcloud
from snownlp import SnowNLP
from collections import Counter
import numpy
from PIL import Image
df =pd.read_excel('终极版.xlsx',sheet_name='市委书记和市长汇总')
data = df.values.tolist()
cate = []
season = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
content = ''
for i in data:
    content += i[7]
    season[i[2]-2020][i[3]//4] += 1
    cate.append(i[10])
xy = [[i,j] for i,j in Counter(cate).items()]
x = [i[0] for i in xy]
y = [i[1] for i in xy]
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.bar(x,y)
plt.show()
object_list = []
seg_list_exact = jieba.cut(content, cut_all=False, HMM=True)
for word in seg_list_exact:
    object_list.append(word)
d = Counter(object_list)
w = []
for i,j in d.items():
    w.append([i,j])
w.sort(key=lambda x:x[1],reverse=True)
d = {i[0]:i[1] for i in w}
mask = numpy.array(Image.open('star.jpg'))
wc = wordcloud.WordCloud(
    font_path='C:/Windows/Fonts/simfang.ttf',
    background_color='white',
    mask=mask,
    max_words=500,
    max_font_size=120
)
del d['许昌市']
del d['安阳市']
del d['鹤壁市']
del d['许昌']
del d['安阳']
del d['鹤壁']
wc.generate_from_frequencies(d)
wc.recolor(color_func=wordcloud.ImageColorGenerator(mask))
plt.figure('词云')
plt.subplots_adjust(top=0.99, bottom=0.01, right=0.99, left=0.01, hspace=0, wspace=0)
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()
x = ['春','夏','秋','冬']
plt.plot(x,season[0])
plt.plot(x,season[1])
plt.plot(x,season[2])
plt.show()
label = ['正面','负面']
v = [0,0]
for i in data[:500]:
    if SnowNLP(i[11]).sentiments > 0.5:
        v[0] += 1
    else:
        v[1] += 1
plt.bar(label,v)
plt.show()

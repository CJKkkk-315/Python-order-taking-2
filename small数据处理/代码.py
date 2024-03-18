import pandas
from collections import Counter
import wordcloud
from PIL import Image
import matplotlib.pyplot as plt
import numpy
data = pandas.read_csv('small_user.csv')
data = data.values.tolist()
d = {}
for i in data:
    try:
        d[i[0]].append(i[2])
    except:
        d[i[0]] = [i[2]]
s = []
for i in d.keys():
    s.append([d[i].count(4)/len(d[i]),i])
s.sort(reverse=True)
print('购买效率达人TOP10')
for i in range(10):
    print(s[i][1])
items = []
for i in data:
    if i[0] == 10001082:
        items.append(i[4])
d = {}
for i in data:
    d[i[0]] = 0
for i in data:
    if i[4] in items:
        d[i[0]] += 1
d = [[j,i] for i,j in d.items()]
d.sort(reverse=True)
print('10001082的同道中人TOP10')
for i in range(10):
    print(d[i][1])
bt = []
for i in data:
    if i[2] == 3:
        bt.append(i[4])
bt = Counter(bt)
btv = [i for i in bt.values()][:10]
btk = [i for i in bt.keys()][:10]
plt.pie(x = btv,labels=btk)
plt.show()
hot = []
for i in data:
    hot.append(str(i[0]))
hot = Counter(hot)
hot = [[j,i] for i,j in hot.items()]
hot.sort(reverse=True)
hot = hot[:10]
hotx = [i[1] for i in hot]
hoty = [i[0] for i in hot]
plt.bar(hotx,hoty)
plt.show()
ciyun = []
for i in data:
    ciyun.append(str(i[4]))
ciyun = Counter(ciyun)
mask = numpy.array(Image.open('无标题.png'))
wc = wordcloud.WordCloud(
    font_path='C:/Windows/Fonts/simfang.ttf',
    background_color='white',
    mask=mask,
    max_words=500,
    max_font_size=120
)
wc.generate_from_frequencies(ciyun)
plt.figure('词云')
plt.subplots_adjust(top=0.99, bottom=0.01, right=0.99, left=0.01, hspace=0, wspace=0)
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()
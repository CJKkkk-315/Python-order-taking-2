from PIL import Image
import matplotlib.pyplot as plt
import numpy
import csv
from collections import Counter
import wordcloud
data = []
with open('small_user.csv','r') as f:
    fcsv = csv.reader(f)
    for i in fcsv:
        data.append(i)
data = data[1:]
dic = {}
for i in data:
    if i[0] in dic:
        dic[i[0]].append(i[2])
    else:
        dic[i[0]] = [i[2]]
print('购买达人')
print(','.join([i[1] for i in sorted([[dic[i].count(4)/len(dic[i]),i] for i in dic.keys()],reverse=True)[:10]]))
like = [i[4] for i in data if i[0] == 10001082]
dic = {}
for i in data:
    if i[4] in like:
        dic[i[0]] += 1
    else:
        dic[i[0]] = 1
print('10001082的同道中人')
print(','.join([i[1] for i in sorted([[j,i] for i,j in dic.items()],reverse=True)[:10]]))
word = Counter([str(i[4]) for i in data])
mask = numpy.array(Image.open('数据处理.png'))
wc = wordcloud.WordCloud(
    font_path='C:/Windows/Fonts/simfang.ttf',
    background_color='white',
    mask=mask,
    max_font_size=120
)
wc.generate_from_frequencies(word)
wc.recolor(color_func=wordcloud.ImageColorGenerator(mask))
plt.subplots_adjust(top=0.99, bottom=0.01, right=0.99, left=0.01, hspace=0, wspace=0)
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.show()
plt.bar([i[1] for i in sorted([[v,k] for k,v in Counter([str(i[0]) for i in data]).items()],reverse=True)[:10]],[i[0] for i in sorted([[v,k] for k,v in Counter([str(i[0]) for i in data]).items()],reverse=True)[:10]])
plt.show()
plt.pie(x = [i for i in Counter([i[4] for i in data]).values()][:8],labels=[i for i in Counter([i[4] for i in data]).keys()][:8])
plt.show()
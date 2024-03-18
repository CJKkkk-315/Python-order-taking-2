import wordcloud
import matplotlib.pyplot as plt
import numpy
from PIL import Image
from collections import Counter
import csv
object_list = []
with open('movie(clear).csv','r',encoding='utf-8') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        cate = i[5].split('/')
        for j in cate:
            object_list.append(j)
mask = numpy.array(Image.open('1.png'))
plt.axis('off')
plt.imshow(mask)
wc = wordcloud.WordCloud(
    font_path = 'C:/Windows/Fonts/simfang.ttf',
    background_color='white',
    mask = mask,
    max_words = 100,
    max_font_size = 70
)
wc.generate_from_frequencies(Counter(object_list))
wc.recolor(color_func=wordcloud.ImageColorGenerator(mask))
plt.figure('词云')
plt.subplots_adjust(top=0.99,bottom=0.01,right=0.99,left=0.01,hspace=0,wspace=0)
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()
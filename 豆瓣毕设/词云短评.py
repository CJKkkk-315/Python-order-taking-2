
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy
from PIL import Image
from collections import Counter
import csv
object_list = []

with open('word.csv','r',encoding='utf-8') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        object_list.append(i[0])
mask = numpy.array(Image.open('1.png'))
plt.axis('off')
plt.imshow(mask)
wc = WordCloud(
    font_path = 'C:/Windows/Fonts/simfang.ttf',
    background_color='white',
    max_words = 500,
    max_font_size = 120
)
for i,j in Counter(object_list).items():
    if j > 10:
        print([i,j])
wc.generate_from_frequencies(Counter(object_list))
plt.figure('词云')
plt.subplots_adjust(top=0.99,bottom=0.01,right=0.99,left=0.01,hspace=0,wspace=0)
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()
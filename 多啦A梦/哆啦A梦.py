import csv
from collections import Counter
from pyecharts.charts import *
from pyecharts import options as opts
import wordcloud
import jieba
with open('哆啦A梦_2022_06.csv',encoding='utf-8') as f:
    data = [i for i in csv.reader(f)][1:]
star = []
for i in data:
    try:
        if i[2] != '无评价' and i[2] != '星级':
            star.append(i[2])
    except:
        continue
star = Counter(star)
xy = sorted(star.items())
x = [i[0] for i in xy]
y = [i[1] for i in xy]
pie = (
        Pie(init_opts=opts.InitOpts(width='1440px', height='800px'))
            .add(series_name='', data_pair=[(i, j) for i, j in zip(x, y)])
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
    )
pie.render('饼图.html')
bar1 = (
        Bar()
            .add_xaxis(x)
            .add_yaxis("数量", y, yaxis_index=0, )
            .extend_axis(yaxis=opts.AxisOpts())
            .set_global_opts(title_opts=opts.TitleOpts(title="柱状图"))
    )
bar1.render('柱状图.html')
good = ['三星','四星','五星']
bad = ['一星','两星']
goods = ''
bads = ''
for i in data:
    if i[2] in good:
        goods += i[3]
    elif i[2] in bad:
        bads += i[3]
goods = jieba.cut(goods)
goods = ' '.join(goods)
bads = jieba.cut(bads)
bads = ' '.join(bads)
wc = wordcloud.WordCloud(font_path = 'C:/Windows/Fonts/simfang.ttf')
wc.generate(goods)
wc.to_file('好评.png')
wc = wordcloud.WordCloud(font_path = 'C:/Windows/Fonts/simfang.ttf')
wc.generate(bads)
wc.to_file('差评.png')
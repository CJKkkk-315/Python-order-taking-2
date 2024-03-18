import matplotlib.pyplot as plt
from pyecharts.charts import *
from pyecharts import options as opts
import csv
data = []
people = []
sell = []
with open('movie(clear).csv','r',encoding='utf-8') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        data.append(i)
data = data[1:]
with open('sell.csv','r',encoding='utf-8') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        if i[6] != '无':
            sell.append(i)
sell = sell[1:]
with open('hot.csv','r',encoding='utf-8') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        people.append(i)
def date(data):
    d = {}
    xy = []
    for i in data:
        year = i[4].split('-')[0]
        try:
            d[year] += 1
        except:
            d[year] = 1
    for i,j in d.items():
        xy.append([i,j])
    xy.sort(key=lambda x:int(x[0]))
    x = [i[0] for i in xy]
    y = [i[1] for i in xy]
    bar1 = (
        Bar()
            .add_xaxis(x)
            .add_yaxis("电影数量", y, yaxis_index=0, )
            .extend_axis(yaxis=opts.AxisOpts())
            .set_global_opts(title_opts=opts.TitleOpts(title="电影分布情况"))
    )
    bar1.render('top250电影分布（年份）.html')
def season(data):
    d = {}
    xy = []
    for i in data:
        try:
            year = int(i[4].split('-')[1])
        except:
            continue
        try:
            d[year//4] += 1
        except:
            d[year//4] = 1
    for i,j in d.items():
        xy.append([i,j])
    xy.sort(key=lambda x:int(x[0]))
    x = [i[0] for i in xy]
    y = [i[1] for i in xy]
    bar1 = (
        Bar()
            .add_xaxis(['春','夏','秋','冬'])
            .add_yaxis("电影数量", y, yaxis_index=0, )
            .extend_axis(yaxis=opts.AxisOpts())
            .set_global_opts(title_opts=opts.TitleOpts(title="电影分布情况"))
    )
    bar1.render('top250电影分布（季节）.html')
def cate(data):
    d = {}
    xy = []
    for i in data:
        cate = i[5].split('/')
        for j in cate:
            try:
                d[j] += 1
            except:
                d[j] = 1
    for i,j in d.items():
        xy.append([i,j])
    x = [i[0] for i in xy]
    y = [i[1] for i in xy]
    pie = (
        Pie(init_opts=opts.InitOpts(width='1440px', height='800px'))
            .add(series_name='', data_pair=[(i, j) for i, j in zip(x, y)])
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
    )

    pie.render('top250电影分布（类型）.html')
def la(data):
    d = {}
    xy = []
    for i in data:
        cate = i[10].split('/')
        for j in cate:
            try:
                d[j] += 1
            except:
                d[j] = 1
    other = 0
    for i,j in d.items():
        if j <= 3:
            other += 1
        else:
            xy.append([i,j])
    x = [i[0] for i in xy]
    y = [i[1] for i in xy]
    x.append('其他')
    y.append(other)
    pie = (
        Pie(init_opts=opts.InitOpts(width='1440px', height='800px'))
            .add(series_name='', data_pair=[(i, j) for i, j in zip(x, y)])
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
    )
    pie.render('top250电影分布（语言）.html')
def place(data):
    d = {}
    xy = []
    for i in data:
        cate = i[9].split('/')
        for j in cate:
            try:
                d[j] += 1
            except:
                d[j] = 1
    other = 0
    for i, j in d.items():
        if j <= 3:
            other += 1
        else:
            xy.append([i, j])
    x = [i[0] for i in xy]
    y = [i[1] for i in xy]
    x.append('其他')
    y.append(other)
    pie = (
        Pie(init_opts=opts.InitOpts(width='1440px', height='800px'))
            .add(series_name='', data_pair=[(i, j) for i, j in zip(x, y)])
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
    )
    pie.render('top250电影分布（地区）.html')
def hotmovie(data):
    d = {}
    xy = []
    for i in data:
        xy.append([i[0], i[-3]])
    xy.sort(key=lambda x: int(x[1]),reverse=True)
    xy = xy[:10]
    x = [i[0] for i in xy]
    y = [i[1] for i in xy]
    bar1 = (
        Bar()
            .add_xaxis(x,)
            .add_yaxis("人气", y, yaxis_index=0, )
            .extend_axis(yaxis=opts.AxisOpts())
            .set_global_opts(title_opts=opts.TitleOpts(title="电影分布情况"),xaxis_opts=opts.AxisOpts(
            axislabel_opts={"interval":"0"}
        ),)
    )
    bar1.render('人气电影top10.html')
def hotpeople(data):
    d = {}
    xy = []
    for i in data:
        try:
            xy.append([i[0], int(i[1].replace(' 人收藏',''))])
        except:
            continue
    xy.sort(key=lambda x: int(x[1]),reverse=True)
    xy = xy[:10]
    x = [i[0] for i in xy]
    y = [i[1] for i in xy]
    bar1 = (
        Bar()
            .add_xaxis(x,)
            .add_yaxis("人气", y, yaxis_index=0, )
            .extend_axis(yaxis=opts.AxisOpts())
            .set_global_opts(title_opts=opts.TitleOpts(title="电影分布情况"),xaxis_opts=opts.AxisOpts(
            axislabel_opts={"interval":"0","rotate":20}
        ),)
    )
    bar1.render('人气明星top10.html')
def datehot(data):
    xy = []
    for i in data:
        year = i[4].split('-')[0]
        xy.append([year,int(i[-3])])
    xy.sort(key=lambda x: int(x[0]))
    x = [i[0] for i in xy]
    y = [i[1] for i in xy]
    point = (Scatter(init_opts=opts.InitOpts(width="720px", height="320px"))
             .add_xaxis(xaxis_data=x)
             .add_yaxis(series_name='', y_axis=y, label_opts=opts.LabelOpts(is_show=False))
             )
    point.render('人气时间分布.html')
def datesell(data):
    xy = []
    for i in data:
        year = i[1]
        xy.append([year, float(i[6].replace('万',''))])
    xy.sort(key=lambda x: int(x[0]))
    x = [i[0] for i in xy]
    y = [i[1] for i in xy]
    point = (Scatter(init_opts=opts.InitOpts(width="720px", height="320px"))
             .add_xaxis(xaxis_data=x)
             .add_yaxis(series_name='', y_axis=y, label_opts=opts.LabelOpts(is_show=False))
             )
    point.render('年份-票房.html')
def sellcate(data):
    d = {}
    xy = []
    for i in data:
        cate = i[3].split('/')
        for j in cate:
            try:
                d[j] += round(float(i[6].replace('万','')),2)
            except:
                d[j] = round(float(i[6].replace('万','')),2)
    for i, j in d.items():
        xy.append([i, j])
    x = [i[0] for i in xy]
    y = [round(i[1],2) for i in xy]
    pie = (
        Pie(init_opts=opts.InitOpts(width='1440px', height='800px'))
            .add(series_name='', data_pair=[(i, j) for i, j in zip(x, y)])
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
    )
    pie.render('类型-票房.html')
def sellplace(data):
    d = {}
    xy = []
    for i in data:
        cate = i[5].split('/')
        for j in cate:
            try:
                d[j] += round(float(i[6].replace('万','')),2)
            except:
                d[j] = round(float(i[6].replace('万','')),2)
    for i, j in d.items():
        xy.append([i, j])
    x = [i[0] for i in xy]
    y = [round(i[1],2) for i in xy]
    pie = (
        Pie(init_opts=opts.InitOpts(width='1440px', height='800px'))
            .add(series_name='', data_pair=[(i, j) for i, j in zip(x, y)])
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
    )
    pie.render('地区-票房.html')
def catepoint(data):
    xy = []
    for i in data:
        for j in i[5].split('/'):
            xy.append([j,float(i[7])])
    # print(xy)
    xy.sort(key=lambda x: x[0])
    x = [i[0] for i in xy]
    y = [i[1] for i in xy]
    point = (Scatter(init_opts=opts.InitOpts(width="720px", height="320px"))
             .add_xaxis(xaxis_data=x)
             .add_yaxis(series_name='', y_axis=y, label_opts=opts.LabelOpts(is_show=False))
             .set_global_opts(yaxis_opts=opts.AxisOpts(min_=8)
    )
             )
    point.render('类型-评分.html')
def timeline(data):
    d = {}
    xy = []
    for i in data:
        time = int(i[-5].replace('分钟',''))
        try:
            d[time//10] += 1
        except:
            d[time//10] = 1
    for i, j in d.items():
        xy.append([i, j])
    xy.sort(key=lambda x:int(x[0]))
    x = [str(i[0])+'0分钟' for i in xy]
    y = [i[1] for i in xy]
    line = (
        Line()
        .add_xaxis(x)
        .add_yaxis('电影数量',y)
        .set_global_opts(title_opts=opts.TitleOpts('电影时长分布'))
    )
    line.render('电影时长分布.html')
timeline(data)
catepoint(data)
date(data)
season(data)
cate(data)
la(data)
place(data)
hotmovie(data)
hotpeople(people)
datehot(data)
datesell(sell)
sellcate(sell)
sellplace(sell)

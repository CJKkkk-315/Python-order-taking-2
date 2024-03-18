import tkinter as tk
import time
from tkinter import *
from tkinter import messagebox
import string
import pickle
import random
import requests
from bs4 import BeautifulSoup
import os
import jieba
from pyecharts.charts import Bar
from pyecharts.charts import Pie
from pyecharts.charts import Funnel
from pyecharts.charts import Page, WordCloud
from pyecharts import options as opts
from pyecharts.globals import SymbolType
from pyecharts.globals import ThemeType
headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'search.dangdang.com'
}
def parseHtml(html):
    data = {}
    #print(html)
    soup = BeautifulSoup(html, 'lxml')
    conshoplist = soup.find_all('div', {'class': 'con shoplist'})[0]
    
    for each in conshoplist.find_all('li'):
        # 书名
        bookname = each.find_all('a')[0].get('title').strip(' ')
        # 书图
        img_src = each.find_all('a')[0].img.get('data-original')
        if img_src is None:
            img_src = each.find_all('a')[0].img.get('src')
        img_src = img_src.strip(' ')
        # 价格
        price = float(each.find_all('p', {'class': 'price'})[0].span.text[1:])
        # 简介
        detail = each.find_all('p', {'class': 'detail'})[0].text
        # 评分
        stars = float(each.find_all('p', {'class': 'search_star_line'})[0].span.span.get('style').split(': ')[-1].strip('%;')) / 20
        # 评论数量
        num_comments = float(each.find_all('p', {'class': 'search_star_line'})[0].a.text[:-3])
        data[bookname] = [img_src, price, detail, stars, num_comments]
    return data
def create():
    global keyword
    global num_page
    keyword = text_var.get()
    top = Toplevel()
    top.title('Python')
    #top.geometry('850x150')
    img1 = tk.PhotoImage(file="bg.gif")
    v = tk.StringVar()
    label_1 = tk.Label(top, textvariable=v, fg="red", bg="black", font=("黑体", 20))
    label_1.pack()

    url = 'http://search.dangdang.com/?key={}&act=input&page_index={}'
    results = {}
    cnt = 0
    num_page = 0
    while True:
        cnt += 1
        if cnt > 5:
            break
        num_page += 1
        v.set('[INFO]: Start to get the data of page%d...' % num_page)
        label_1.update()
        time.sleep(3)
        page_url  = url.format(keyword, num_page)
        res = requests.get(page_url, headers=headers)
        if '抱歉，没有找到与“%s”相关的商品，建议适当减少筛选条件' % keyword in res.text:
            break
        page_data = parseHtml(res.text)
        results.update(page_data)
        

    messagebox.showinfo( "Python爬虫", "爬虫已完成")
    with open('%s_%d.pkl' % (keyword, num_page-1), 'wb') as f:
        pickle.dump(results, f)

    label_image1 = tk.Label(top, image=img1)
    label_image1.pack()
    top.mainloop()
'''柱状图(2维)'''


def drawBar(title, data, savepath='./results'):
    if not os.path.exists(savepath):
        os.mkdir(savepath)
    attrs = [i for i, j in data.items()]
    values = [j for i, j in data.items()]
    c = (
        Bar(init_opts=opts.InitOpts(
            animation_opts=opts.AnimationOpts(
                animation_delay=1000, animation_easing="elasticOut"
            ), theme=ThemeType.ROMA
        ))
            .set_global_opts(title_opts=opts.TitleOpts(title=title, pos_left='35%'),
                             datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")], )
            .add_xaxis(attrs)
            .add_yaxis('', values)
    )
    c.render(os.path.join(savepath, '%s.html' % title))


'''饼图'''


def drawPie(title, data, savepath='./results'):
    if not os.path.exists(savepath):
        os.mkdir(savepath)
    attrs = [i for i, j in data.items()]
    values = [j for i, j in data.items()]
    c = (
        Pie()
            .add(
            "",
            [list(z) for z in zip(attrs, values)],
            radius=["30%", "65%"],
            center=["50%", "60%"],
            rosetype="radius",
        )
            .set_global_opts(title_opts=opts.TitleOpts(title=title, pos_left='35%'),
                             legend_opts=opts.LegendOpts(
                                 orient="vertical", pos_top="15%", pos_left="2%"
                             ))
    )
    c.render(os.path.join(savepath, '%s.html' % title))


'''漏斗图'''


def drawFunnel(title, data, savepath='./results'):
    if not os.path.exists(savepath):
        os.mkdir(savepath)
    attrs = [i for i, j in data.items()]
    values = [j for i, j in data.items()]
    c = (
        Funnel()
            .add(
            "",
            [list(z) for z in zip(attrs, values)],
            label_opts=opts.LabelOpts(position="inside"),
            sort_="none",
        )
            .set_global_opts(title_opts=opts.TitleOpts(title=title, pos_left='35%'),
                             legend_opts=opts.LegendOpts(
                                 orient="vertical", pos_top="15%", pos_left="2%"
                             ))
    )
    c.render(os.path.join(savepath, '%s.html' % title))


'''统计词频'''


def statistics(texts, stopwords):
    words_dict = {}
    for text in texts:
        temp = jieba.cut(text)
        for t in temp:
            if t in stopwords or t == 'unknow':
                continue
            if t in words_dict.keys():
                words_dict[t] += 1
            else:
                words_dict[t] = 1
    return words_dict


'''词云'''


def drawWordCloud(words, title, savepath='./results'):
    if not os.path.exists(savepath):
        os.mkdir(savepath)
    c = (
        WordCloud()
            .add("", words, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
            .set_global_opts(title_opts=opts.TitleOpts(title=title, pos_left='40%'))
    )
    c.render(os.path.join(savepath, '%s.html' % title))

def visualization(str_name, num):
    tmp = str_name + '_' + str(num) + '.pkl'
    with open(tmp, 'rb') as f:
        data = pickle.load(f)
    # 价格分布
    results = {}
    prices = []
    price_max = ['', 0]
    for key, value in data.items():
        price = value[1]
        if price_max[1] < price:
            price_max = [key, price]
        prices.append(price)
    results['小于50元'] = sum(i < 50 for i in prices)
    results['50-100元'] = sum((i < 100 and i >= 50) for i in prices)
    results['100-200元'] = sum((i < 200 and i >= 100) for i in prices)
    results['200-300元'] = sum((i < 300 and i >= 200) for i in prices)
    results['300-400元'] = sum((i < 400 and i >= 300) for i in prices)
    results['400元以上'] = sum(i >= 400 for i in prices)
    tmp = str_name + '相关图书的价格分布'
    drawPie(tmp, results)
    # 评分分布
    results = {}
    stars = []
    for key, value in data.items():
        star = value[3] if value[3] > 0 else '暂无评分'
        stars.append(str(star))
    for each in sorted(set(stars)):
        results[each] = stars.count(each)
    tmp = str_name + '相关图书评分的分布'
    drawBar(tmp, results)
    # 评论数量
    results = {}
    comments_num = []
    top20 = {}
    for key, value in data.items():
        num = int(value[-1])
        comments_num.append(num)
        top20[key.split('【')[0].split('（')[0].split('(')[0].split(' ')[0].split('：')[0]] = num
    results['0评论'] = sum(i == 0 for i in comments_num)
    results['0-100评论'] = sum((i > 0 and i <= 100) for i in comments_num)
    results['100-1000评论'] = sum((i > 100 and i <= 1000) for i in comments_num)
    results['1000-5000评论'] = sum((i > 1000 and i <= 5000) for i in comments_num)
    results['5000评论以上'] = sum(i > 5000 for i in comments_num)
    tmp = str_name + '相关图书评论数量分布'
    drawFunnel(tmp, results)
    top20 = dict(sorted(top20.items(), key=lambda item: item[1])[-20:])
    tmp = str_name + '相关图书评论数量TOP20'
    drawBar(tmp, top20)
    # 词云
    stopwords = open('./stopwords.txt', 'r', encoding='utf-8').read().split('\n')[:-1]
    texts = [j[2] for i, j in data.items()]
    words_dict = statistics(texts, stopwords)
    words_dict = list(tuple(words_dict.items()))
    tmp = str_name + '相关图书简介词云'
    drawWordCloud(words_dict, tmp, savepath='./results')

window = tk.Tk()
pic = PhotoImage(file='nyist.gif')
label1 = Label(image=pic)
label1.place(x=0, y=0)
# 设置窗口大小
winWidth = 500
winHeight = 500
# 获取屏幕分辨率
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
 
x = int((screenWidth - winWidth) / 2)
y = int((screenHeight - winHeight) / 2)
 
# 设置主窗口标题
window.title("python爬虫")
# 设置窗口初始位置在屏幕居中
window.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
# 设置窗口宽高固定
window.resizable(0, 0)
frame = tk.Frame(window)
frame.place(rely=.5, relx=0.5, x=-122.5, y=-100, width=245, height=50)

 
tk.Label(frame, text="请输入查询的商品").grid(row=0)

text_var = tk.StringVar()
tk.Entry(frame, textvariable = text_var).grid(row=0, column=1)
tk.Button(frame, text="查询", command=create, padx=20).grid(row=2, columnspan=3)
window.mainloop()

visualization(keyword, num_page-1)
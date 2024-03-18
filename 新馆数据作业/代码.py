import requests
from bs4 import BeautifulSoup
import csv
from pyecharts.charts import Bar
from pyecharts import options as opts
def bubble_sort(array):
    for i in range(1, len(array)):
        for j in range(0, len(array)-i):
            if array[j][1] < array[j+1][1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
response = requests.get('https://www.caixin.com/2022-04-11/101868555.html')
soup = BeautifulSoup(response.text)
content = soup.find(id='Main_Content_Val').find_all(name='p')[10].text
l = content.replace('\u3000\u3000截至4月8日，各国家和地区新冠疫苗情况（按接种率排序，即接种一剂疫苗的人数占总人口比例）：','').split('，')
data = []
for i in l:
    a = i.split('%')[0]
    if a[:2] != '截至':
        for j in range(len(a)):
            if a[j].isdigit():
                data.append([a[:j],float(a[j:])])
                break
print(data)
data = bubble_sort(data)
print('接种率最大值为：',data[0][1])
print('接种率最小值为：',data[-1][1])
s = [round(i[1]) for i in data]
print('接种率平均值为：',round(sum(s)/len(s),2))
with open('接种率排序.csv','w',encoding='utf-8',newline='') as f:
    f_csv = csv.writer(f)
    for i in data:
        f_csv.writerow(i)
x = [i[0] for i in data]
bar1 = (
    Bar(init_opts=opts.InitOpts(width='1440px', height='800px'))
        .add_xaxis(x)
        .add_yaxis("接种率", s, yaxis_index=0, )
        .extend_axis(yaxis=opts.AxisOpts())
        .set_global_opts(title_opts=opts.TitleOpts(title="接种率可视化"),xaxis_opts=opts.AxisOpts(
            axislabel_opts={"interval":"0","rotate":70}))
)
bar1.render('接种率可视化.html')

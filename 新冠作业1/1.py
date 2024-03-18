import requests
import csv

import json
def selection_sort(list2):
    for i in range(0, len (list2)):
        min = i
        for j in range(i + 1, len(list2)):
            if list2[j][1] > list2[min][1]:
                min = j
        list2[i], list2[min] = list2[min], list2[i]
response = requests.get('https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=VaccineSituationData')
js = json.loads(response.text)
data = []
m = []
for i in js['data']['VaccineSituationData']:
    data.append([i['country'],i['total_vaccinations_per_hundred']])
    m.append(i['total_vaccinations_per_hundred'])
selection_sort(data)
print('每百人接种数最大值为：',max(m))
print('每百人接种数最小值为：',min(m))
print('每百人接种数平均值为：',round(sum(m)/len(m),2))
with open('排序.csv','w',encoding='gbk',newline='') as f:
    f_csv = csv.writer(f)
    for i in data:
        f_csv.writerow(i)
import matplotlib.pyplot as plt
data = []
with open('排序.csv','r',encoding='gbk') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        data.append(i)
x = [i[0] for i in data[:10]]
y = [float(i[1]) for i in data[:10]]
plt.rcParams['font.sans-serif']=['SimHei']
plt.bar(x,y)
plt.show()
from tkinter import *
import tkinter as tk
import tkinter.messagebox
d = {}
with open('排序.csv','r',encoding='gbk') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        d[i[0]] = i[1]
def search(name):
    try:
        res = d[name]
        tk.messagebox.showinfo(title='结果', message='该国家的每百人疫苗接种为：' + str(res))
    except:
        tk.messagebox.showinfo(title='结果', message='没有该国家的数据')
root = Tk()
root.geometry('350x70')
root.title('疫苗接种查询')
Label(root,text='请输入国家:').place(x=20,y=20)
e = Entry(root)
e.place(x=100,y=20)
Button(root, width=7, height=1, text='查询', command=lambda:search(e.get())).place(x=250,y=15)
root.mainloop()


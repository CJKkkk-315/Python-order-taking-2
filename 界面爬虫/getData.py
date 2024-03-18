import tkinter as tk
import requests
from tkinter.messagebox import *
from bs4 import BeautifulSoup

import csv
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=100)
        r.raise_for_status() #如果连接状态不是200，则引发HTTPError异常
        r.encoding=r.apparent_encoding #使返回的编码正常
        return r.text
    except:
        return ""
def get_contents(ulist,rurl):
    soup = BeautifulSoup(rurl,'html.parser')
    trs = soup.find_all('tr')
    for tr in trs:
        ui = []
        for td in tr:
            ui.append(td.string)
        ulist.append(ui)
def save_contents(filename,urlist):
    with open(filename,'w',newline='') as f:
        writer = csv.writer(f) #创建csv的写文件对象csv_writer
        writer.writerows(urlist)
urlist = [ ]
url="http://www.gaosan.com/gaokao/241219.html"
filename = "中国大学排行榜2021.csv"
rs=['']
def do1():
    rs[0] = getHTMLText(url)
    if rs[0]!='':
        tk.messagebox.showinfo('连接状态','连接正常！')
    else:
        tk.messagebox.showinfo('连接状态','连接失败！')
def do2():
    get_contents(urlist,rs[0])
    if urlist!='':
        tk.messagebox.showinfo('获取数据状态','获取数据正常！')
    else:
        tk.messagebox.showinfo('获取数据状态','获取数据失败！')
def do3():
    save_contents(filename,urlist)
    tk.messagebox.showinfo('保存数据','保存文件成功！')
def do_scrip(root1):
    top1 = tk.Toplevel(root1) #子窗体实例名=Toplevel(根窗体),可参照根窗体进行属性设置
    top1.title('数据获取子系统')
    top1.transient(root1) # 窗口置顶root之上
    top1.geometry('500x500+500+300')
    bt1 = tk.Button(top1, text='连接服务器', command=do1)
    bt2 = tk.Button(top1, text='获取数据', command=do2)
    bt3 = tk.Button(top1, text='保存数据', command=do3)
    bt1.place(x=50, y=50, width=100, height=60)
    bt2.place(x=50, y=150, width=100, height=60)
    bt3.place(x=50, y=250, width=100, height=60)
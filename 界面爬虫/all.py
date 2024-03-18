import tkinter as tk
import requests
from tkinter.messagebox import *
from bs4 import BeautifulSoup
import csv
import getData
import csvProcessing
import visualizing
import dataView
def do1():
    getData.do_scrip(root)
def do2():
    csvProcessing.dataProcess()
def do3():
    visualizing.dataView()
def do4():
    dataView.do_dataview(root)
root = tk.Tk()
root.title('中国大学数据分析')
root.geometry('800x600+300+100')
bt1 = tk.Button(root, text='数据爬取',command=do1)
bt2 = tk.Button(root, text='读文件数据处理',command=do2)
bt3 = tk.Button(root, text='数据处理及统计',command=do3)
bt4 = tk.Button(root, text='数据统计及可视化',command=do4)
bt1.place(x=200, y=110, width=100, height=60)
bt2.place(x=450, y=110, width=100, height=60)
bt3.place(x=200, y=310, width=100, height=60)
bt4.place(x=450, y=310, width=100, height=60)
#控件及控件位置
root.mainloop()
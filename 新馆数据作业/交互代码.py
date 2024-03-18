from tkinter import *
import tkinter as tk
import tkinter.messagebox
import csv
d = {}
with open('接种率排序.csv','r',encoding='utf-8') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        d[i[0]] = i[1]
def search(name):
    try:
        res = d[name]
        tk.messagebox.showinfo(title='结果', message='该国家的疫苗接种率为：' + str(res) + '%')
    except:
        tk.messagebox.showinfo(title='结果', message='没有该国家的数据')
root = Tk()
root.geometry('400x120')
root.title('疫苗接种率查询系统')
Label(root,text='请输入要查询的国家').pack()
e = Entry(root)
e.pack()
Button(root, width=13, height=2, text='查询', command=lambda:search(e.get())).pack()
root.mainloop()
from tkinter import *
import tkinter as tk
import tkinter.messagebox
import csv
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
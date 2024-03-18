import tkinter.messagebox
import tkinter as tk
from tkinter import *
def f2(a,b):
    tk.messagebox.showinfo(title='公用分摊面积', message="公用分摊面积为：" + str(float(a) * float(b)))
def f1(root,a,b):
    root.withdraw()
    xs = round((float(a) - float(b)) / float(b),2)
    tk.messagebox.showinfo(title='分摊系数', message="分摊系数为："+str(xs))
    root = Tk()
    root.title("公摊面积计算")
    root.geometry('300x150')
    Label(root, text='套内建筑面积:').place(x=20, y=20)
    e1 = Entry(root)
    e1.place(x=100, y=20)
    Button(root, text='计算', width=15, heigh=2, command=lambda: f2(e1.get(), xs)).place(x=100, y=80)
    root.mainloop()
def main(root):
    root.destroy()
    root = Tk()
    root.title("公摊面积计算")
    root.geometry('300x150')
    Label(root,text='总面积:').place(x=20,y=20)
    e1 = Entry(root,width=8)
    e1.place(x=150,y=20)
    Label(root,text='各套内建筑面积之和:').place(x=20,y=50)
    e2 = Entry(root,width=8)
    e2.place(x=150,y=50)
    Button(root, text='计算', width=15, heigh=2, command=lambda :f1(root,e1.get(),e2.get())).place(x=100,y=80)
    root.mainloop()
root = Tk()
main(root)
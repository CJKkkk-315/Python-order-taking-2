import tkinter.messagebox
import tkinter as tk
from random import randint
from tkinter import *
from tkinter.filedialog import askopenfilename
def f2():
    root.destroy()
def f1():
    global e
    global ans
    if int(e.get()) == ans:
        tk.messagebox.showinfo(title='结果', message='回答正确！')
    else:
        tk.messagebox.showinfo(title='结果', message='回答错误！')
    e = Entry(root)
    e.place(x=270, y=60, width=40, height=30)
    a = randint(10, 99)
    b = randint(10, 99)
    ans = a * b
    l1.config(text=str(a) + ' * ' + str(b) + ' =')
root = Tk()
root.title("口算生成器")
root.geometry('450x250')
# 设置总体及各个岗位的按钮，绑定按钮函数
l1 = Label(root,text='',font=(10))
l1.place(x=160,y=60)
button1 = Button(root, text='提交', width=15, heigh=2, command=f1)
button1.place(x=80, y=100 + 50)
button2 = Button(root, text='退出程序', width=15, heigh=2, command=f2)
button2.place(x=250, y=100 + 50)
e = Entry(root)
e.place(x=270, y=60, width=40, height=30)
a = randint(10, 99)
b = randint(10, 99)
ans = a * b
l1.config(text=str(a) + ' * ' + str(b) + ' =')
root.mainloop()
# -*- coding: utf-8 -*-
import RT拟动力
import RT拟静力
import RT静力
import Sarma静力
import Sarma拟动力
import Sarma拟静力
import Bishop拟动力
import Bishop拟静力
import Bishop静力
flag = 0
res = 0
mylist = []
def choosepic1():
    global mylist
    mylist = []
    path_ = askopenfilename()
    path.set(path_)
    img_RS = e1.get()
    with open(img_RS,'r') as f:
        data = f.readlines()
    data = [list(map(float,i.replace('\n','').split(','))) for i in data]
    for i in data:
        if len(i) == 1:
            mylist.append(i[0])
        else:
            mylist.append(i)
    l1.config(text = '当前文件：' + img_RS.split("/")[-1])
def choosepic2():
    for i in range(len(mylist)):
        try:
            mylist[i] = int(mylist[i])
        except:
            pass
    print(mylist)
    if flag == 1:
        res = Sarma拟动力.tMIN(*mylist)
    elif flag == 2:
        res = Sarma拟静力.Ub(*mylist)
    elif flag == 3:
        res = Sarma静力.Ub(*mylist)
    tk.messagebox.askokcancel(title='结果', message='边坡安全系数=' + str(res))
def choosepic3():
    aw = []
    for i in mylist:
        try:
            for j in i:
                if int(j) == j:
                    aw.append(int(j))
                else:
                    aw.append(j)
        except:
            if int(i) == i:
                aw.append(int(i))
            else:
                aw.append(i)
    print(aw)
    if flag == 1:
        res = Bishop拟动力.BSDtMIN(*mylist)
    elif flag == 2:
        res = Bishop拟静力.BSD(*mylist)
    elif flag == 3:
        res = Bishop静力.BSD(*mylist)
    tk.messagebox.askokcancel(title='结果', message='边坡安全系数=' + str(res))
def choosepic4():
    for i in range(len(mylist)):
        try:
            mylist[i] = int(mylist[i])
        except:
            pass
    print(mylist)
    if flag == 1:
        res = RT拟动力.U1(*mylist)
    elif flag == 2:
        res = RT拟静力.U1(*mylist)
    elif flag == 3:
        res = RT静力.U1(*mylist)
    tk.messagebox.askokcancel(title='结果', message='边坡安全系数=' + str(res))
def funtion1():
    global flag
    flag = 1
def funtion2():
    global flag
    flag = 2
def funtion3():
    global flag
    flag = 3
if __name__ == "__main__":
    import os
    import tkinter.messagebox
    import tkinter as tk

    from tkinter import *
    from tkinter.filedialog import askopenfilename
    root = Tk()
    root.title('UI')
    root.geometry('550x300')
    path = StringVar()
    Button(root, width=12, height=1, text='选择文件', command=choosepic1).place(x=30, y=250)
    Button(root, width=12, height=1, text='Sarma法', command=choosepic2).place(x=130, y=250)
    Button(root, width=12, height=1, text='Bishop法', command=choosepic3).place(x=230, y=250)
    Button(root, width=12, height=1, text='传递系数法', command=choosepic4).place(x=330, y=250)
    ck1 = tk.Checkbutton(root, text='拟动力', command=funtion1).place(x=30, y=220)
    ck2 = tk.Checkbutton(root, text='拟静力', command=funtion2).place(x=120, y=220)
    ck3 = tk.Checkbutton(root, text='静力', command=funtion3).place(x=210, y=220)
    e1 = Entry(root, state='readonly', text=path)
    l1 = Label(root,text='当前文件：无',font=(14))
    l1.place(x=130,y=110)
    l2 = Label(root,text='根据Excel或txt中的数据\n得到边坡原始参数',font=(14))
    l2.place(x=150,y=20)
    root.mainloop()
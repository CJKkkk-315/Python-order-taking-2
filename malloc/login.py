from tkinter import *    # 引入需要的模块
from tkinter.messagebox import *
import tkinter

top = tkinter.Tk()   # 创建顶层窗体
top.title('login @  Guan  2019102001')  #在窗体标题中写上自己的姓名全拼和学号
img = tkinter.PhotoImage(file = 'kagaya.gif')   #在该顶层窗体中显示背景图片
label1 = tkinter.Label(image = img, height = 768, width = 1024)
label1.pack()

label2 = tkinter.Label(top,text='用户名:',bg='blue') #文本标签
label2.place(x=600,y=500)

label3 = tkinter.Label(top,text='密   码:',bg='blue')
label3.place(x=600,y=530)

txt1=tkinter.StringVar()  #StringVar用于实时监控字符串的变化
txt2=tkinter.StringVar()

en1=tkinter.Entry(top,textvariable=txt1)  #输入框
en1.place(x=650,y=500)

en2=tkinter.Entry(top,textvariable=txt2)
en2.place(x=650,y=530)

B = tkinter.Button(top, text ="登录")  #登录按钮
B.place(x=600,y=560)

top.mainloop()
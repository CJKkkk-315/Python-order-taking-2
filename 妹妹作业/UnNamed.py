import tkinter as tk 
import tkinter.messagebox as messagebox

from numpy import var

substance={'阿斯巴甜':(40,50),'海藻酸钠':(20,200),'安赛蜜':(0,5000),'山梨酸钾':(0,30)}
Namelist=['阿斯巴甜','海藻酸钠','安赛蜜','山梨酸钾']
#生成一个主窗体对象
win = tk.Tk()

win.geometry("250x130")#窗体大小

win.title("检查添加剂是否超标")

var_name=tk.StringVar()
var_content=tk.DoubleVar()

tk.Label(win,text='名称：').grid(column=0,row=0)
tk.Entry(win,textvariable=var_name).grid(row=0,column=1)

tk.Label(win,text='含量：').grid(column=0,row=1)
tk.Entry(win,textvariable=var_content).grid(row=1,column=1)

def Check():
    if var_name.get() in Namelist:
        try:
            SubName=var_name.get()
            SubContent=var_content.get()
            _,temp=substance[SubName]
            if SubContent>temp:
                messagebox.showinfo(message='含量超标')
            else:
                messagebox.showinfo(message='含量正常')
        except:
            messagebox.showinfo( message='请输入正常的数据')
    else:
       messagebox.showinfo( message='输入的成分不存在') 

tk.Button(win,text='确定',command=Check).grid(row=3,column=0)
win.mainloop()
import tkinter as tk
import tkinter.messagebox
import pickle
info = ['猴','鸡','狗','猪','鼠','牛','虎','兔','龙','蛇','马','羊']
de = ['猴','鸡','狗','猪','鼠','牛','虎','兔','龙','蛇','马','羊']
def function():
    year = int(u.get()) % 12
    window.destroy()
    root = tk.Tk()
    root.title('标题在这里改')
    root.geometry('450x300')
    for i in range(len(info)):
        if i == year:
            a = info[i]
    for i in range(len(de)):
        if i == year:
            b = info[i]
    tk.Label(root, text='你的生肖为：' + a).place(x=30, y=100)
    tk.Label(root, text=b).place(x=30, y=200)
    root.mainloop()
window=tk.Tk()
window.title('标题在这里改')
window.geometry('450x300')
tk.Label(window,text='请输入出生年份:').place(x=30,y=100)
u=tk.Entry(window)
u.place(x=160,y=100)
bt_login=tk.Button(window,text='开始',command=function)
bt_login.place(x=140,y=230)
window.mainloop()
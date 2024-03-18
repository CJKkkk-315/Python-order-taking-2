import tkinter.messagebox
import tkinter as tk
import csv
import xlrd
import os
ext = '.csv'
ext2 = '.csv'
files = os.listdir(os.getcwd() + '\\dataBase\\keywordDir')
data = []
res = []
ex = []
for file in files:
    with open(os.getcwd() + '\\dataBase\\keywordDir\\' + file, 'r',errors='ignore')as f:
        aw = []
        f_csv = csv.reader(f)
        for row in f_csv:
            # print(1)
            aw.append(row)
    aw = aw[1:]
    data += aw
def search():
    global res
    res = []
    key = u.get()
    for i in data:
        for j in i:
            if key in j:
                res.append(i)
                break
    lb.delete(0, 'end')
    for i in res:
        lb.insert('end', ' '.join(i))
def show(event):
    global ex
    global res
    ex = []
    object = event.widget
    indexs = object.curselection()
    # print(indexs)
    for index in indexs:
        ex.append(res[index])
    # print(ex)
window = tk.Tk()
window.title('药品查询系统')
window.geometry('760x600')
sc = tkinter.Scrollbar(window)
sc.pack(side=tkinter.RIGHT, fill=tkinter.Y)
tk.Label(window, text='请输入关键词').place(x=30, y=20)
u = tk.Entry(window)
u.place(x=110, y=20)
bt_login1 = tk.Button(window, text='开始搜索',command = search)
bt_login1.place(x=300, y=15)
lb = tk.Listbox(window,width=100,height=28,yscrollcommand=sc.set,selectmode=tkinter.MULTIPLE)
lb.bind("<<ListboxSelect>>", show)
lb.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
lb.place(x=30, y=50)
sc.config(command=lb.yview)
# for i in data:
#     lb.insert('end', ' '.join(i))
window.mainloop()
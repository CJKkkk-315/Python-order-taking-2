import tkinter as tk
from PIL import Image,ImageTk #图形显示
from tkinter.messagebox import *
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei'] # 指定默认字体：解决plot不能显示中文问题
def dv1(label_img):
    img_open = Image.open('tu1.jpg')
    img_png = ImageTk.PhotoImage(img_open)
    label_img.configure(image=img_png)
    label_img.image=img_png
def dv2(label_img):
    img_open = Image.open('tu2.jpg')
    img_png = ImageTk.PhotoImage(img_open)
    label_img.configure(image=img_png)
    label_img.image=img_png
def do_dataview(root1):
    # 以下为子窗体属性设置
    top1 = tk.Toplevel(root1)
    top1.title('数据可视化窗体')
    top1.transient(root1)  # 窗口只置顶root之上
    top1.geometry('800x600+500+200')
    #子窗体属性设置
    label_img = tk.Label(top1)
    label_img.place(x=5, y=15)
    def do_dv1():
        dv1(label_img)
    def do_dv2():
        dv2(label_img)
    but0 = tk.Button(top1, text="按地区统计", command=do_dv1)
    but0.pack()
    but1 = tk.Button(top1, text="按办学层次统计", command=do_dv2)
    but1.pack()
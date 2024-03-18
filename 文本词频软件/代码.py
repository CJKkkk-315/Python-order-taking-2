# -*- coding=utf-8 -*-
import wordcloud
import tkinter
import jieba
import tkinter.filedialog
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use('TkAgg')
from PIL import Image, ImageTk
root = tkinter.Tk()
root.title('词频分析助手')
root.geometry('900x718')
counts = {}
# 录入文件
def loading():
    filename = tkinter.filedialog.askopenfilename()
    fn = open(filename, 'r', encoding='UTF-8')  # 打开文件
    string_data = fn.read()  # 读出整个文件
    fn.close()
    if filename != '':
        l1.config(text=filename)
        t1.insert(tkinter.END, string_data)
        ## 加载停用词表
        stopwords = [line.strip() for line in open("停用词库.txt", encoding="utf-8").readlines()]
        words = jieba.lcut(string_data)
        ## 停用词去除
        for word in words:
            # 不在停用词表中
            if word not in stopwords:
                # 不统计字数为一的词
                if len(word) == 1:
                    continue
                else:
                    counts[word] = counts.get(word, 0) + 1
    else:
        l1.config(text='未选择文件')

## 输出所有频次
def count_times():
    global counts
    itemss = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    listbox1.delete(0, tkinter.END)
    for i in range(20):
        word, count = itemss[i]
        listbox1.insert(tkinter.END, "{:<10}{:>7}\n".format(word, count))
def delete():
    word = t2.get(1.0,tkinter.END).split('\n')
    for i in word:
        if i in counts:
            del counts[i]
def change():
    words = [i for i in t3.get(1.0, tkinter.END).split('\n') if i]
    for word in words:
        a,b = word.split('-->')
        if a in counts:
            at = counts[a]
            del counts[a]
            if b in counts:
                counts[b] += at
            else:
                counts[b] = at
def draw_word():
    wc = wordcloud.WordCloud(
        font_path='C:/Windows/Fonts/simfang.ttf',
        background_color='white',
        max_words=500,
        max_font_size=120
    )
    wc.generate_from_frequencies(counts)
    fig = Figure(figsize=(5, 3),facecolor='#F0F0F0',edgecolor='#F0F0F0')
    a = fig.add_subplot(111)
    a.imshow(wc,interpolation='bilinear')
    a.axis('off')
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().place(x=0, y=400)
    canvas.draw()
def draw_count():
    itemss = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    x = [i[0] for i in itemss][:10]
    y = [i[1] for i in itemss][:10]
    fig = Figure(figsize=(4, 3), facecolor='#F0F0F0', edgecolor='#F0F0F0')
    a = fig.add_subplot(111)
    a.bar(x,y)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().place(x=500, y=400)
    canvas.draw()
b1 = tkinter.Button(root, text="选择文件目录：", command=loading)
b1.grid(row=0, column=0, sticky='w')
t1 = tkinter.Text(root, height=24, width=50)
t1.place(x=0,y=30)
l1 = tkinter.Label(root, text="未选择文件")
l1.place(x=100, y=0)



## 图形界面
### 标签
l2 = tkinter.Label(root, text="词频统计结果")
l2.place(x=400,y=0)
l3 = tkinter.Label(root, text="需要删除的词组")
l3.place(x=650,y=0)
l4 = tkinter.Label(root, text="需要替换的词组")
l4.place(x=650,y=187)
### 列表框
listbox1 = tkinter.Listbox(root, height=17, width=30, relief=tkinter.RAISED)  # 词频统计
listbox1.place(x=400,y=30)
### 文本框
t2 = tkinter.Text(root, height=10, width=27)  # 删除词组
t2.place(x=650,y=25)
### 输入框
t3 = tkinter.Text(root, height=10, width=27)  # 替换词组
t3.place(x=650,y=210)
def f():
    pass

### 按钮
b2 = tkinter.Button(root, text="保存结果", command=f)
b2.place(x=550,y=0)
b3 = tkinter.Button(root, text="删除词组", command=delete)
b3.place(x=780,y=160)
b4 = tkinter.Button(root, text="替换词组", command=change)
b4.place(x=780,y=350)
b5 = tkinter.Button(root, text="重新统计", command=count_times)
b5.place(x=550,y=340)
b7 = tkinter.Button(root, text="词频统计", command=count_times)
b7.place(x=200,y=350)
b8 = tkinter.Button(root, text="生成词云", command=draw_word)
b8.place(x=280,y=350)
b9 = tkinter.Button(root, text="生成统计图", command=draw_count)
b9.place(x=450,y=340)

root.mainloop()

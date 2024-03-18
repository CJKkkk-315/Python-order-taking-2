
import tkinter
import jieba
import tkinter.filedialog
import matplotlib.pyplot as plt
import matplotlib
root = tkinter.Tk()
root.title('词频分析助手')
root.geometry('1000x618')


# 录入文件
def loading():
    fn = open('threekingdoms.txt','r', encoding='UTF-8')  # 打开文件
    string_data = fn.read()  # 读出整个文件
    fn.close()
    filename = tkinter.filedialog.askopenfilename()
    if filename != '':
        l1.config(text=filename)
        t1.insert(tkinter.END, string_data)
    else:
        l1.config(text='未选择文件')


b1 = tkinter.Button(root, text="选择文件目录：", command=loading)
b1.grid(row=0, column=0, sticky='w')
t1 = tkinter.Text(root, height=40, width=50)
t1.grid(row=1, column=0, columnspan=2, rowspan=4)
l1 = tkinter.Label(root, text="未选择文件")
l1.grid(row=0, column=1)


## 输出所有频次
def savee():
    listbox1.delete(0, tkinter.END)
    for i in range(1, 20):
        word, count = itemss[i]
        listbox1.insert(tkinter.END, "{:<10}{:>7}\n".format(word, count))

#
#########################################################
# def seg_word(line,output_words,result_dict):#语句解析
#     seg = jieba.cut(line.strip())
#     for word in seg:
#         if word in output_words:
#             result_dict[word] = result_dict.get(word,0) + 1#统计每个词出现的次数
#
# def output(inputfilename, outputfilename,output_words,result_dict):#解析并输出
#     inputfile = open(inputfilename, encoding='UTF-8', mode='r')
#     outputfile = open(outputfilename, encoding='UTF-8', mode='w')
#     for line in inputfile.readlines():
#         seg_word(line,output_words,result_dict)
#     middict = {}
#     for (key,value) in sorted(result_dict.items(),key=lambda x:x[1],reverse=True):
#         middict[key] = value
#     result_dict = middict
#     for i in result_dict:
#         outputfile.write(i+":"+str(result_dict[i])+"\n")
#     inputfile.close()
#     outputfile.close()
#     return result_dict
###################################################################
#
## 修改词组
def change():
    if e2.get() != '' and listbox1.curselection() != ():
        selected = listbox1.curselection()[0]
        ss1 = str(listbox1.curselection()[0])
        sss = eval(ss1)
        ssss = itemss[sss+1]
        ss2 = e2.get() + '            ' + str(ssss[1])
        listbox1.delete(selected)
        listbox1.insert(selected, ss2)


## 删除词组
def delete1():
    if listbox1.curselection() != ():
        listbox1.delete(listbox1.curselection())
        t2.insert(tkinter.END, listbox1.curselection())


## 图形界面
### 标签
l2 = tkinter.Label(root, text="词频统计结果")
l2.grid(row=0, column=2, sticky='w')
l3 = tkinter.Label(root, text="需要删除的词组")
l3.grid(row=0, column=4, sticky='w')
l4 = tkinter.Label(root, text="需要替换的词组")
l4.grid(row=3, column=4, sticky='w')
### 列表框
listbox1 = tkinter.Listbox(root, height=29, width=50, relief=tkinter.RAISED)  # 词频统计
listbox1.grid(row=1, column=2, columnspan=2, rowspan=4)
### 文本框
t2 = tkinter.Text(root, height=17, width=27)  # 删除词组
t2.grid(row=1, column=4, columnspan=2)
### 输入框
e2 = tkinter.Entry(root)  # 替换词组
e2.grid(row=4, column=4)


### 按钮
b2 = tkinter.Button(root, text="保存结果", command=savee)
b2.grid(row=0, column=3, sticky='e')
b3 = tkinter.Button(root, text="删除词组", command=delete1)
b3.grid(row=5, column=2, sticky='w')
b4 = tkinter.Button(root, text="替换词组", command=change)
b4.grid(row=5, column=3, sticky='w')
b5 = tkinter.Button(root, text="重新统计", command=savee)
b5.grid(row=2, column=5, sticky='e')
b6 = tkinter.Button(root, text="重新统计", command=savee)
b6.grid(row=5, column=5, sticky='e')
b7 = tkinter.Button(root, text="词频统计", command=savee)
b7.grid(row=5, column=0, sticky='e')
b8 = tkinter.Button(root, text="生成词云", command=loading)
b8.grid(row=5, column=1, sticky='e')
b9 = tkinter.Button(root, text="生成统计图", command=loading)
b9.grid(row=5, column=4, sticky='w')
## 载入
txt = open("threekingdoms.txt ", encoding="utf-8").read()
## 加载停用词表
stopwords = [line.strip() for line in open("停用词库.txt", encoding="utf-8").readlines()]
words = jieba.lcut(txt)
counts = {}
## 停用词去除
for word in words:
    # 不在停用词表中
    if word not in stopwords:
        # 不统计字数为一的词
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
## 相同情况归并
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":  # 列举排除相同情况
        rword = "孔明"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "孟德曰" or word == "丞相":
        rword = "曹操"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "张翼德" or word == "翼德":
        rword = "张飞"
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1  # 若字典中没有则创建键值对，有则在原有值上加1


itemss = sorted(counts.items(), key=lambda x: x[1], reverse=True)

root.mainloop()

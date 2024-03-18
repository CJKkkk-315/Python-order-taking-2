import tkinter as tk
import numpy
import pylab
import pickle
import tkinter.messagebox
from tkinter import *
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
informationList=[]
# 打开文件,从data.csv中读取数据
with open('data.csv',encoding='utf-8') as f:
    for i in f.readlines():
        t = i.replace('\n','').split(',')
        t[2] = int(t[2])
        informationList.append(t)
def get_data():
    def insert():
        informationList.append([e1.get(), e2.get(), int(e3.get()), e4.get(), e5.get()])
        window_info = tk.Toplevel(window_new)
        window_info.geometry('300x200')
        window_info.title('结果')
        la = Label(window_info, text=f'提交成功！', font=("微软雅⿊", 14))
        la.pack(expand='yes')
    window_new = tk.Toplevel(window)
    window_new.geometry('600x600')
    window_new.title('记账系统')
    Label(window_new,text="日期（例2021-5-9）：").pack()                   #日期
    e1 = Entry(window_new)
    e1.pack()
    Label(window_new,text="姓名：").pack()
    e2 = Entry(window_new)
    e2.pack()
    Label(window_new,text="金额：").pack()
    e3 = Entry(window_new)
    e3.pack()
    Label(window_new,text="收支分类（收入or支出)：").pack()
    e4 = Entry(window_new)
    e4.pack()
    Label(window_new,text="类型：").pack()
    e5 = Entry(window_new)
    e5.pack()
    Label(window_new, text="").pack()
    Button(window_new,text='提交',command=insert).pack()
def change():
    def modify():
        num = int(e0.get())
        informationList[num-1][0]=e1.get()
        informationList[num-1][1]=e2.get()
        informationList[num - 1][2] =int(e3.get())
        informationList[num - 1][3] =e4.get()
        informationList[num - 1][4] = e5.get()
        window_info = tk.Toplevel(window_new)
        window_info.geometry('300x200')
        window_info.title('结果')
        la = Label(window_info, text=f'提交成功！', font=("微软雅⿊", 14))
        la.pack(expand='yes')
    window_new = tk.Toplevel(window)
    window_new.geometry('600x600')
    window_new.title('记账系统')
    i=0
    for data in informationList:
        i+=1
        Label(window_new,text='序号'+str(i)+'  '+' '.join(list(map(str,data)))).pack()
    Label(window_new, text='选择修改数据的序数').pack()
    e0 = Entry(window_new)
    e0.pack()
    Label(window_new, text="日期（例2021-5-9）：").pack()  # 日期
    e1 = Entry(window_new)
    e1.pack()
    Label(window_new, text="姓名：").pack()
    e2 = Entry(window_new)
    e2.pack()
    Label(window_new, text="金额：").pack()
    e3 = Entry(window_new)
    e3.pack()
    Label(window_new, text="收支分类（收入or支出)：").pack()
    e4 = Entry(window_new)
    e4.pack()
    Label(window_new, text="类型：").pack()
    e5 = Entry(window_new)
    e5.pack()
    Label(window_new, text="").pack()
    Button(window_new, text='提交', command=modify).pack()
def remove():
    def dele():
        num = int(e0.get())
        del informationList[num - 1]
        window_info = tk.Toplevel(window_new)
        window_info.geometry('300x200')
        window_info.title('结果')
        la = Label(window_info, text=f'提交成功！', font=("微软雅⿊", 14))
        la.pack(expand='yes')
    # show
    window_new = tk.Toplevel(window)
    window_new.geometry('600x600')
    window_new.title('记账系统')
    i = 0
    for data in informationList:
        i += 1
        Label(window_new, text='序号' + str(i) + '  ' + ' '.join(list(map(str, data)))).pack()
    Label(window_new, text='选择修改数据的序数').pack()
    e0 = Entry(window_new)
    e0.pack()
    Label(window_new, text="").pack()
    Button(window_new, text='提交', command=dele).pack()
def search():
    def sear():
        window_info = tk.Toplevel(window_new)
        window_info.geometry('600x400')
        window_info.title('结果')
        date2 = e1.get()
        name2 = e2.get()
        date2_list = []
        for data in informationList:
            if date2 == data[0]:
                date2_list.append(data)
        for i in date2_list:
            if i[1] == name2:
                Label(window_info, text=' '.join(list(map(str, i)))).pack()
    window_new = tk.Toplevel(window)
    window_new.geometry('600x600')
    window_new.title('记账系统')
    Label(window_new, text='请输入日期：').pack()
    e1 = Entry(window_new)
    e1.pack()
    Label(window_new, text='请输入姓名：').pack()
    e2 = Entry(window_new)
    e2.pack()
    Label(window_new, text="").pack()
    Button(window_new, text='提交', command=sear).pack()
def rank():
    window_new = tk.Toplevel(window)
    window_new.geometry('600x600')
    window_new.title('记账系统')
    income_data=[]
    pay_data=[]

    for data in informationList:
        if data[3]=="收入":
            income_data.append(data)
    income_data.sort(key=lambda x: x[2])       #
    Label(window_new, text="按照第三维数据升序排序(收入)：").pack()
    for data in income_data:
        Label(window_new, text= ' '.join(list(map(str, data)))).pack()

    for data in informationList:
        if data[3] == "支出":
            pay_data.append(data)
    pay_data.sort(key=lambda x: x[2])
    Label(window_new, text="按照第三维数据升序排序(支出)：").pack()
    for data in pay_data:
        Label(window_new, text=' '.join(list(map(str, data)))).pack()
def analyse():
    print(informationList)
    informationList1 = informationList[::]
    informationList1.sort(key=lambda x:int(x[0].replace('-','')))
    #收入分析
    income_date = []
    income_data = []
    for data in informationList1:
        if data[3] == "收入":
            income_date.append(data[0])
            income_data.append(data[2])
    plt.plot(income_date, income_data, linewidth=4)      #分隔
    plt.title("Square Number", fontsize=14)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    plt.tick_params(axis='x', labelsize=10)
    plt.show()
    #支出分析
    zhichu_date=[]
    zhichu_data=[]
    for data in informationList1:
        if data[3] == "支出":
            zhichu_date.append(data[0])
            zhichu_data.append(data[2])
    plt.plot(zhichu_date, zhichu_data, linewidth=4)
    plt.title("Square Number", fontsize=14)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    plt.tick_params(axis='x', labelsize=10)
    plt.show()
    print('分析完成---------------')
def predict():
    def zuixiaoerchen(arrayY, picTitle):
        print(f"arrayY: {arrayY}")
        print(f"picTitle: {picTitle}")
        if len(arrayY) == 0:
            return [0, 0, 0]
        # 取得收入，作为纵坐标的峰值标准
        maxValue = max(arrayY)
        print(maxValue)
        # 设置横坐标和纵坐标的值
        # def arange(start=None, stop=None, step=None, dtype=None)
        x = numpy.arange(1, len(arrayY) + 1, 1)
        # def array(p_object, dtype=None, copy=True, order='K', subok=False, ndmin=0)
        y = numpy.array(arrayY)
        # 第1個拟合，设置自由度為1 : (y = ax + b)
        print(x)
        print(y)
        z = numpy.polyfit(x, y, 1)
        # z: [  0.46428571  13.35238095],就相当于的到a,b
        print(f"z: {z}")
        # 生成的多項式對象(y = ax + b)
        p = numpy.poly1d(z)  # 得导函数y
        # p: -0.1448x + 13.23
        print(f"p: {p}")
        if z[0] > 0:
            # 绘制原曲线及 拟合后的曲线
            # 原曲线 , 设置颜色(蓝色)和标签
            pylab.plot(x, y, 'b^-', label='original sales growth')
            # 自由度为1的趋势曲线, 设置颜色(蓝色)和标签
            pylab.plot(x, p(x), 'gv--', label=f'y = {z[0]}x + {z[1]}')
            # 设置图表的title
            pylab.title(f"picTitle: {picTitle}")
            # 设置横坐标，纵坐标的范围
            pylab.axis([0, len(arrayY) + 1, 0, maxValue + 1])
            pylab.legend()
            # 保存成图片
            pylab.show()
            # 清除图表设置
            pylab.clf()
        return [z[0], z[1], maxValue]

    # 用最小二乘法，生成趋势
    income_data = []
    informationList1 = informationList[::]
    informationList1.sort(key=lambda x: int(x[0].replace('-', '')))
    for data in informationList1:
        if data[3] == "收入":
            income_data.append(int(data[2]))
    zhichu_data = []
    for data in informationList1:
        if data[3] == "支出":
            zhichu_data.append(int(data[2]))
    # sales = [2.444, 2.730, 3.319, 3.948, 4.877, 4.909, 6.000, 5.354, 4.642, 6.518, 6.484]
    a, b, maxIncom = zuixiaoerchen(income_data, "income Growth")
    c, d, maxzichu = zuixiaoerchen(zhichu_data, "zhichu Growth")
    growth = a
    income = maxIncom
    growth2 = c
    zhichucome = maxzichu
    print(f"growth = {growth}, maxIcome = {income}")
    print(f"growth = {growth2}, maxIcome = {zhichucome}")
# 定义主界面
window = tk.Tk()
window.title('记账系统')
window.geometry('500x600')
# 定义各个按钮以及绑定函数
Button(window, text='录入数据',width=10,command=get_data).place(x=200, y=50)
Button(window, text='查找数据',width=10,command=search).place(x=200, y=130)
Button(window, text='修改数据',width=10,command=change).place(x=200, y=210)
Button(window, text='删除数据',width=10,command=remove).place(x=200, y=290)
Button(window, text='分析',width=10,command=analyse).place(x=200, y=370)
Button(window, text='排序',width=10,command=rank).place(x=200, y=450)
Button(window, text='预测',width=10,command=predict).place(x=200, y=530)
window.mainloop()
# 程序结束以后将新的数据写入data.csv中
with open('data.csv','w',newline='',encoding='utf-8') as f:
    for i in informationList:
        f.write(','.join(list(map(str,i)))+'\n')

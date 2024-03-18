import tkinter as tk
import pickle
import tkinter.messagebox
from tkinter import *
import matplotlib.pyplot as plt
window = tk.Tk()
window.title('数据管家')
window.geometry('900x600')

canvas = tk.Canvas(window, height=1200, width=900)


canvas.pack(side='top')

tk.Label(window, text='用户：', font=('Arial', 15)).place(x=400, y=400)
tk.Label(window, text='密码：', font=('Arial', 15)).place(x=400, y=450)

var_usr_name = tk.StringVar()
var_usr_name.set('ID昵称')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name, font=('Arial', 15))
entry_usr_name.place(x=500, y=400)

var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, font=('Arial', 15), show="*")
entry_usr_pwd.place(x=500, y=450)


def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'123': '456'}
            pickle.dump(usrs_info, usr_file)
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(message=usr_name + '欢迎来到数据管家')
            window_new = tk.Toplevel(window)
            window_new.geometry('1920x1000')
            window_new.title('数据管家')
            window_new['bg'] = '#333333'

            def mea_command_score():
                window_mea = tk.Toplevel(window_new)
                window_mea.geometry('900x600')
                window_mea.title('数据输入')
                l = Label(window_mea, text='请输入近10天的成绩')
                l.pack()
                l1 = Label(window_mea,text='请输入成绩1：')
                l1.pack()
                e1 = Entry(window_mea)
                e1.pack()
                l2 = Label(window_mea, text='请输入成绩2：')
                l2.pack()
                e2 = Entry(window_mea)
                e2.pack()
                l3 = Label(window_mea, text='请输入成绩3：')
                l3.pack()
                e3 = Entry(window_mea)
                e3.pack()
                l4 = Label(window_mea, text='请输入成绩4：')
                l4.pack()
                e4 = Entry(window_mea)
                e4.pack()
                l5 = Label(window_mea, text='请输入成绩5：')
                l5.pack()
                e5 = Entry(window_mea)
                e5.pack()
                l6 = Label(window_mea, text='请输入成绩6：')
                l6.pack()
                e6 = Entry(window_mea)
                e6.pack()
                l7 = Label(window_mea, text='请输入成绩7：')
                l7.pack()
                e7 = Entry(window_mea)
                e7.pack()
                l8 = Label(window_mea, text='请输入成绩8：')
                l8.pack()
                e8 = Entry(window_mea)
                e8.pack()
                l9 = Label(window_mea, text='请输入成绩9：')
                l9.pack()
                e9 = Entry(window_mea)
                e9.pack()
                l10 = Label(window_mea, text='请输入成绩10：')
                l10.pack()
                e10 = Entry(window_mea)
                e10.pack()
                l = Label(window_mea, text='请输入预期成绩：')
                l.pack()
                e = Entry(window_mea)
                e.pack()
                awl = Label(window_mea, text='')
                awl.pack()

                def show_score(l, target):

                    step = (l[9]-l[0])/10
                    if step == 0:
                        s = []
                        for i in range(len(l)):
                            s.append([i, l[i]])
                        x = [i[0] for i in s]

                        def partition(arr, low, high):
                            i = (low - 1)  # 最小元素索引
                            pivot = arr[high]

                            for j in range(low, high):

                                # 当前元素小于或等于 pivot
                                if arr[j] <= pivot:
                                    i = i + 1
                                    arr[i], arr[j] = arr[j], arr[i]

                            arr[i + 1], arr[high] = arr[high], arr[i + 1]
                            return (i + 1)

                            # arr[] --> 排序数组

                        # low  --> 起始索引
                        # high  --> 结束索引

                        # 快速排序函数
                        def quickSort(arr, low, high):
                            if low < high:
                                pi = partition(arr, low, high)

                                quickSort(arr, low, pi - 1)
                                quickSort(arr, pi + 1, high)

                        n = len(x)
                        quickSort(x, 0, n - 1)
                        y = [i[1] for i in s]
                        window_info = tk.Toplevel(window_mea)
                        window_info.geometry('300x200')
                        window_info.title('预测结果')
                        la = Label(window_info, text=f'无法到达预期成绩\n建议：XXXXXXXXXXXXXXXXXXXX', font=("微软雅⿊", 14))
                        la.pack(expand='yes')
                        plt.rcParams['font.sans-serif'] = ['SimHei']
                        plt.subplot(1, 1, 1)
                        plt.title('成绩趋势')
                        plt.scatter(x=x, y=y)
                        plt.ylabel('成绩')
                        plt.xlabel('天数')
                        plt.show()
                        return
                    day = (target - l[9])/step
                    print(day)
                    day = int(day)
                    if day > 0:
                        s = []
                        for i in range(len(l)):
                            s.append([i, l[i]])
                        x = [i[0] for i in s]

                        def partition(arr, low, high):
                            i = (low - 1)  # 最小元素索引
                            pivot = arr[high]

                            for j in range(low, high):

                                # 当前元素小于或等于 pivot
                                if arr[j] <= pivot:
                                    i = i + 1
                                    arr[i], arr[j] = arr[j], arr[i]

                            arr[i + 1], arr[high] = arr[high], arr[i + 1]
                            return (i + 1)

                            # arr[] --> 排序数组

                        # low  --> 起始索引
                        # high  --> 结束索引

                        # 快速排序函数
                        def quickSort(arr, low, high):
                            if low < high:
                                pi = partition(arr, low, high)

                                quickSort(arr, low, pi - 1)
                                quickSort(arr, pi + 1, high)

                        n = len(x)
                        quickSort(x, 0, n - 1)
                        y = [i[1] for i in s]
                        window_info = tk.Toplevel(window_mea)
                        window_info.geometry('300x200')
                        window_info.title('预测结果')
                        la = Label(window_info,text=f'达到预期成绩大概需要{str(day)}天',font=("微软雅⿊",14))
                        la.pack(expand='yes')
                        plt.rcParams['font.sans-serif'] = ['SimHei']
                        plt.subplot(1, 1, 1)
                        plt.title('成绩趋势')
                        plt.scatter(x=x,y=y)
                        plt.ylabel('成绩')
                        plt.xlabel('天数')
                        plt.show()
                    else:
                        s = []
                        for i in range(len(l)):
                            s.append([i, l[i]])
                        x = [i[0] for i in s]

                        def partition(arr, low, high):
                            i = (low - 1)  # 最小元素索引
                            pivot = arr[high]

                            for j in range(low, high):

                                # 当前元素小于或等于 pivot
                                if arr[j] <= pivot:
                                    i = i + 1
                                    arr[i], arr[j] = arr[j], arr[i]

                            arr[i + 1], arr[high] = arr[high], arr[i + 1]
                            return (i + 1)

                            # arr[] --> 排序数组

                        # low  --> 起始索引
                        # high  --> 结束索引

                        # 快速排序函数
                        def quickSort(arr, low, high):
                            if low < high:
                                pi = partition(arr, low, high)

                                quickSort(arr, low, pi - 1)
                                quickSort(arr, pi + 1, high)

                        n = len(x)
                        quickSort(x, 0, n - 1)


                        y = [i[1] for i in s]
                        window_info = tk.Toplevel(window_mea)
                        window_info.geometry('300x200')
                        window_info.title('预测结果')
                        la = Label(window_info, text=f'无法到达预期成绩\n建议：XXXXXXXXXXXXXXXXXXXX',font=("微软雅⿊",14))
                        la.pack(expand='yes')
                        plt.rcParams['font.sans-serif'] = ['SimHei']
                        plt.subplot(1, 1, 1)
                        plt.title('成绩趋势')
                        plt.scatter(x=x,y=y)
                        plt.ylabel('成绩')
                        plt.xlabel('天数')
                        plt.show()
                b = Button(window_mea, text='开始分析预测',command = lambda:show_score([
                    float(e1.get()),
                    float(e2.get()),
                    float(e3.get()),
                    float(e4.get()),
                    float(e5.get()),
                    float(e6.get()),
                    float(e7.get()),
                    float(e8.get()),
                    float(e9.get()),
                    float(e10.get()),

                ],
                float(e.get())))
                b.pack()



            def mea_command_heath():
                window_mea = tk.Toplevel(window_new)
                window_mea.geometry('900x600')
                window_mea.title('数据输入')
                l = Label(window_mea, text='请输入近10天的体重')
                l.pack()
                l1 = Label(window_mea,text='请输入体重1：')
                l1.pack()
                e1 = Entry(window_mea)
                e1.pack()
                l2 = Label(window_mea, text='请输入体重2：')
                l2.pack()
                e2 = Entry(window_mea)
                e2.pack()
                l3 = Label(window_mea, text='请输入体重3：')
                l3.pack()
                e3 = Entry(window_mea)
                e3.pack()
                l4 = Label(window_mea, text='请输入体重4：')
                l4.pack()
                e4 = Entry(window_mea)
                e4.pack()
                l5 = Label(window_mea, text='请输入体重5：')
                l5.pack()
                e5 = Entry(window_mea)
                e5.pack()
                l6 = Label(window_mea, text='请输入体重6：')
                l6.pack()
                e6 = Entry(window_mea)
                e6.pack()
                l7 = Label(window_mea, text='请输入体重7：')
                l7.pack()
                e7 = Entry(window_mea)
                e7.pack()
                l8 = Label(window_mea, text='请输入体重8：')
                l8.pack()
                e8 = Entry(window_mea)
                e8.pack()
                l9 = Label(window_mea, text='请输入体重9：')
                l9.pack()
                e9 = Entry(window_mea)
                e9.pack()
                l10 = Label(window_mea, text='请输入体重10：')
                l10.pack()
                e10 = Entry(window_mea)
                e10.pack()
                l = Label(window_mea, text='请输入预期体重：')
                l.pack()
                e = Entry(window_mea)
                e.pack()
                awl = Label(window_mea, text='')
                awl.pack()

                def show_heath(l, target):

                    step = (l[9]-l[0])/10
                    if step == 0:
                        s = []
                        for i in range(len(l)):
                            s.append([i, l[i]])
                        x = [i[0] for i in s]

                        def partition(arr, low, high):
                            i = (low - 1)  # 最小元素索引
                            pivot = arr[high]

                            for j in range(low, high):

                                # 当前元素小于或等于 pivot
                                if arr[j] <= pivot:
                                    i = i + 1
                                    arr[i], arr[j] = arr[j], arr[i]

                            arr[i + 1], arr[high] = arr[high], arr[i + 1]
                            return (i + 1)

                            # arr[] --> 排序数组

                        # low  --> 起始索引
                        # high  --> 结束索引

                        # 快速排序函数
                        def quickSort(arr, low, high):
                            if low < high:
                                pi = partition(arr, low, high)

                                quickSort(arr, low, pi - 1)
                                quickSort(arr, pi + 1, high)

                        n = len(x)
                        quickSort(x, 0, n - 1)


                        y = [i[1] for i in s]
                        window_info = tk.Toplevel(window_mea)
                        window_info.geometry('300x200')
                        window_info.title('预测结果')
                        la = Label(window_info, text=f'无法到达预期体重\n建议：XXXXXXXXXXXXXXXXXXXX', font=("微软雅⿊", 14))
                        la.pack(expand='yes')
                        plt.rcParams['font.sans-serif'] = ['SimHei']
                        plt.subplot(1, 1, 1)
                        plt.title('体重趋势')
                        plt.scatter(x=x, y=y)
                        plt.ylabel('体重')
                        plt.xlabel('天数')
                        plt.show()
                        return
                    day = (target - l[9])/step
                    print(day)
                    day = int(day)
                    if day >= 0:
                        s = []
                        for i in range(len(l)):
                            s.append([i, l[i]])
                        x = [i[0] for i in s]

                        def partition(arr, low, high):
                            i = (low - 1)  # 最小元素索引
                            pivot = arr[high]

                            for j in range(low, high):

                                # 当前元素小于或等于 pivot
                                if arr[j] <= pivot:
                                    i = i + 1
                                    arr[i], arr[j] = arr[j], arr[i]

                            arr[i + 1], arr[high] = arr[high], arr[i + 1]
                            return (i + 1)

                            # arr[] --> 排序数组

                        # low  --> 起始索引
                        # high  --> 结束索引

                        # 快速排序函数
                        def quickSort(arr, low, high):
                            if low < high:
                                pi = partition(arr, low, high)

                                quickSort(arr, low, pi - 1)
                                quickSort(arr, pi + 1, high)

                        n = len(x)
                        quickSort(x, 0, n - 1)



                        y = [i[1] for i in s]
                        window_info = tk.Toplevel(window_mea)
                        window_info.geometry('300x200')
                        window_info.title('预测结果')
                        la = Label(window_info,text=f'达到预期体重大概需要{str(day)}天',font=("微软雅⿊",14))
                        la.pack(expand='yes')
                        plt.rcParams['font.sans-serif'] = ['SimHei']
                        plt.subplot(1, 1, 1)
                        plt.title('体重趋势')
                        plt.scatter(x=x,y=y)
                        plt.ylabel('体重')
                        plt.xlabel('天数')
                        plt.show()
                    else:
                        s = []
                        for i in range(len(l)):
                            s.append([i, l[i]])
                        x = [i[0] for i in s]

                        def partition(arr, low, high):
                            i = (low - 1)  # 最小元素索引
                            pivot = arr[high]

                            for j in range(low, high):

                                # 当前元素小于或等于 pivot
                                if arr[j] <= pivot:
                                    i = i + 1
                                    arr[i], arr[j] = arr[j], arr[i]

                            arr[i + 1], arr[high] = arr[high], arr[i + 1]
                            return (i + 1)

                            # arr[] --> 排序数组

                        # low  --> 起始索引
                        # high  --> 结束索引

                        # 快速排序函数
                        def quickSort(arr, low, high):
                            if low < high:
                                pi = partition(arr, low, high)

                                quickSort(arr, low, pi - 1)
                                quickSort(arr, pi + 1, high)

                        n = len(x)
                        quickSort(x, 0, n - 1)



                        y = [i[1] for i in s]
                        window_info = tk.Toplevel(window_mea)
                        window_info.geometry('300x200')
                        window_info.title('预测结果')
                        la = Label(window_info, text=f'无法到达预期体重\n建议：XXXXXXXXXXXXXXXXXXXX',font=("微软雅⿊",14))
                        la.pack(expand='yes')
                        plt.rcParams['font.sans-serif'] = ['SimHei']
                        plt.subplot(1, 1, 1)
                        plt.title('体重趋势')
                        plt.scatter(x=x,y=y)
                        plt.ylabel('体重')
                        plt.xlabel('天数')
                        plt.show()
                b = Button(window_mea, text='开始分析预测',command = lambda:show_heath([
                    float(e1.get()),
                    float(e2.get()),
                    float(e3.get()),
                    float(e4.get()),
                    float(e5.get()),
                    float(e6.get()),
                    float(e7.get()),
                    float(e8.get()),
                    float(e9.get()),
                    float(e10.get()),

                ],
                float(e.get())))
                b.pack()


            def person_info():
                with open('usrs_detail.pickle', 'rb') as f:
                    d = pickle.load(f)
                print(d)
                window_mea = tk.Toplevel(window_new)
                window_mea.geometry('900x600')
                window_mea.title('个人信息')
                l1 = Label(window_mea, text='用户姓名：')
                l1.pack()
                e1 = Entry(window_mea)
                e1.insert(0,d[usr_name]['name'])
                e1.pack()

                l2 = Label(window_mea, text='用户性别：')
                l2.pack()
                e2 = Entry(window_mea)
                e2.insert(0, d[usr_name]['sex'])
                e2.pack()

                l3 = Label(window_mea, text='用户年龄：')
                l3.pack()
                e3 = Entry(window_mea)
                e3.insert(0, d[usr_name]['age'])
                e3.pack()

                l4 = Label(window_mea, text='用户职业：')
                l4.pack()
                e4 = Entry(window_mea)
                e4.insert(0, d[usr_name]['work'])
                e4.pack()
                def save(name,sex,age,work):
                    with open('usrs_detail.pickle','wb') as f:
                        d[usr_name] = {'name':name,'sex':sex,'age':age,'work':work}
                        pickle.dump(d, f)
                    window_mea.destroy()
                b = Button(window_mea,text='保存',command=lambda :save(e1.get(),
                                                             e2.get(),
                                                             e3.get(),
                                                             e4.get()))
                b.pack()

            b = tk.Button(window_new, text='成绩分析', width=10, height=3, font=('Arial', 35), cursor='hand2',
                          command=mea_command_score)
            b.place(x=200, y=200)

            b = tk.Button(window_new, text='身体健康分析', width=10, height=3, font=('Arial', 35), cursor='hand2',
                          command=mea_command_heath)
            b.place(x=600, y=200)

            b = tk.Button(window_new, text='个人信息', width=10, height=3, font=('Arial', 35), cursor='hand2',
                          command=person_info)
            b.place(x=1000, y=200)

        else:
            tk.messagebox.showinfo(message='对不起，您的密码错误！', title='警告')
    else:
        is_sign_up = tk.messagebox.askyesno(message='您还未注册，是否注册？', title='警告')
        if is_sign_up:
            def sign_to_gather():
                nn = new_name.get()
                np = new_pwd.get()
                npf = new_pwd_confirm.get()
                with open('usrs_info.pickle', 'rb') as usr_file:
                    exist_usr_info = pickle.load(usr_file)
                with open('usrs_detail.pickle', 'rb') as usr_file:
                    exist_usr_detail = pickle.load(usr_file)
                if np != npf:
                    tk.messagebox.showerror('错误', '请确认密码一致!')
                    pass
                else:
                    if (nn in exist_usr_info):
                        tk.messagebox.showerror('错误', '此ID已被注册！')
                    else:
                        exist_usr_info[nn] = np
                        exist_usr_detail[nn] = {}
                        exist_usr_detail[nn]['name'] = ''
                        exist_usr_detail[nn]['sex'] = ''
                        exist_usr_detail[nn]['age'] = ''
                        exist_usr_detail[nn]['work'] = ''
                        with open('usrs_info.pickle', 'wb') as usr_file:
                            pickle.dump(exist_usr_info, usr_file)
                        with open('usrs_detail.pickle', 'wb') as usr_file:
                            pickle.dump(exist_usr_detail, usr_file)
                        tk.messagebox.showinfo('欢迎', '你已经成功注册！')
                        window_sign_up.destroy()

            window_sign_up = tk.Toplevel(window)
            window_sign_up.geometry('500x500')
            window_sign_up.title('注册账号')

            new_name = tk.StringVar()
            new_name.set('')
            tk.Label(window_sign_up, text='ID：').place(x=10, y=10)
            entry_usr_name = tk.Entry(window_sign_up, textvariable=new_name)
            entry_usr_name.place(x=150, y=10)

            new_pwd = tk.StringVar()
            new_name.set('')
            tk.Label(window_sign_up, text='密码：').place(x=10, y=50)
            entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show="*")
            entry_usr_pwd.place(x=150, y=50)

            new_pwd_confirm = tk.StringVar()
            new_pwd_confirm.set('')
            tk.Label(window_sign_up, text='确认密码：').place(x=10, y=100)
            entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show="*")
            entry_usr_pwd_confirm.place(x=150, y=100)

            btn_comfirm_sign_up = tk.Button(window_sign_up, text='注册', command=sign_to_gather)
            btn_comfirm_sign_up.place(x=150, y=130)


def usr_sign_up():
    def sign_to_gather():
        nn = new_name.get()
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        with open('usrs_detail.pickle', 'rb') as usr_file:
            exist_usr_detail = pickle.load(usr_file)
        if np != npf:
            tk.messagebox.showerror('错误', '请确认密码一致!')
            pass
        else:
            if (nn in exist_usr_info):
                tk.messagebox.showerror('错误', '此ID已被注册！')
            else:
                exist_usr_info[nn] = np
                exist_usr_detail[nn] = {}
                exist_usr_detail[nn]['name'] = ''
                exist_usr_detail[nn]['sex'] = ''
                exist_usr_detail[nn]['age'] = ''
                exist_usr_detail[nn]['work'] = ''
                with open('usrs_info.pickle', 'wb') as usr_file:
                    pickle.dump(exist_usr_info, usr_file)
                with open('usrs_detail.pickle', 'wb') as usr_file:
                    pickle.dump(exist_usr_detail, usr_file)
                tk.messagebox.showinfo('欢迎', '你已经成功注册！')
                window_sign_up.destroy()

    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('500x500')
    window_sign_up.title('注册账号')

    new_name = tk.StringVar()
    new_name.set('')
    tk.Label(window_sign_up, text='ID：').place(x=10, y=10)
    entry_usr_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_usr_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    new_name.set('')
    tk.Label(window_sign_up, text='密码：').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show="*")
    entry_usr_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    new_pwd_confirm.set('')
    tk.Label(window_sign_up, text='确认密码：').place(x=10, y=100)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show="*")
    entry_usr_pwd_confirm.place(x=150, y=100)

    btn_comfirm_sign_up = tk.Button(window_sign_up, text='注册', command=sign_to_gather)
    btn_comfirm_sign_up.place(x=150, y=130)


btn_login = tk.Button(window, text='登录', font=('Arial', 13), cursor='hand2', command=usr_login)
btn_login.place(x=480, y=500)
btn_sign_up = tk.Button(window, text='注册', font=('Arial', 13), cursor='hand2', command=usr_sign_up)
btn_sign_up.place(x=580, y=500)


def do_job():
    pass

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='用户管理', menu=filemenu)
filemenu.add_separator()
filemenu.add_command(label='退出', command=window.quit)
window.config(menu=menubar)
window.mainloop()

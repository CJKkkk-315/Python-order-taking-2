from file import *
from order import *
from tkinter import *
import tkinter as tk
import tkinter.messagebox
def menu_order1(root):
    """查询菜单"""
    root.destroy()
    root = Tk()
    root.geometry('400x820')
    return_list = readFile()[0]  # 调用读取food_list.txt的方法,0元素位位返回的列表
    text = ("                 %-16s%-16s%-16s%-16s" % ("菜品ID", "菜品名称", "菜品描述", "菜品价格"))
    Label(root,text=text).pack()
    for i in return_list:
        text2 = ("                 %-16s%-16s%-16s%-16s" % (i[0], i[1], i[2], i[3]))
        Label(root,text=text2).pack()
    Button(root, width=13, height=2, text='返回上级菜单', command=lambda: menu_order(root)).pack()
    root.mainloop()
def menu_order211(root,food_name,food_num,all_price):
    root.destroy()
    root = Tk()
    root.geometry('0x0')
    root.withdraw()
    with open('uncommitted_order.txt', 'a+') as unor:
        # 调试时报错:TypeError: can only concatenate str (not "int") to str
        # unor.write(food_name+','+food_num+','+all_price+'\n')
        # 则将all_price转化为str
        unor.write(food_name + ',' + food_num + ',' + str(all_price) + '\n')
    tk.messagebox.showinfo(title='结果', message='保存订单成功!')
    root.deiconify()
    menu_order(root)
def menu_order21211(root,food_name,food_num,all_price,food_id2,food_num2):
    root.destroy()
    root = Tk()
    root.geometry('0x0')
    root.withdraw()
    return_dic = readFile()[1]  # 调用读取food_list.txt的方法,1元素位位返回的字典
    food_tuple2 = return_dic[food_id2]
    food_name2 = food_tuple2[0]
    food_price2 = food_tuple2[1]
    all_price2 = int(food_num2) * int(food_price2)
    sum_price = all_price + all_price2
    food_numsum = eval(food_num) + eval(food_num2)
    if sum_price > 30:
        sum_price = sum_price - 5
    else:
        pass
    tk.messagebox.showinfo(title='结果', message="您订了 %s 份-%s-和 %s 份-%s-,总价为: %d元\n提交订单成功!\n点餐结束！" % (food_num, food_name, food_num2, food_name2, sum_price))
    with open('submit_order.txt', 'a+') as submit:
        submit.write(food_name + food_name2 + ',' + str(food_numsum) + ',' + str(sum_price) + '\n')
        # 调试时报错: TypeError: can only concatenate str(not "int") to str，故将food_numsum改为str(food_numsum)
    root.deiconify()
    menu_order(root)
def menu_order2121(root,food_name,food_num,all_price):
    root.destroy()
    root = Tk()
    root.geometry('400x820')
    return_list = readFile()[0]  # 调用读取food_list.txt的方法,0元素位位返回的列表
    text = ("                 %-16s%-16s%-16s%-16s" % ("菜品ID", "菜品名称", "菜品描述", "菜品价格"))
    Label(root, text=text).pack()
    for i in return_list:
        text2 = ("                 %-16s%-16s%-16s%-16s" % (i[0], i[1], i[2], i[3]))
        Label(root, text=text2).pack()
    Label(root, text="请输入您要订的菜品ID：").pack()
    e1 = tk.Entry(root)
    e1.pack()
    Label(root, text="请输入您要订的菜品份数：").pack()
    e2 = tk.Entry(root)
    e2.pack()
    Button(root, width=7, height=2, text='提交', command=lambda: menu_order21211(root,food_name,food_num,all_price,e1.get(), e2.get())).place(x=300,y=750)
    root.mainloop()
def menu_order212(root,food_name,food_num,all_price):
    root.destroy()
    root = Tk()
    root.geometry('0x0')
    root.withdraw()
    with open('submit_order.txt', 'a+') as submit:
        submit.write(food_name + ',' + food_num + ',' + str(all_price) + '\n')
    tk.messagebox.showinfo(title='结果', message='提交订单成功!')
    root.deiconify()
    root.geometry('400x100')
    Label(root,text='是否需要继续点餐？').pack()
    Button(root,text='是',command=lambda :menu_order2121(root,food_name,food_num,all_price)).pack()
    Button(root,text='否',command=lambda :new_main(root)).pack()
    root.mainloop()
def menu_order21(root,e1,e2):
    return_dic = readFile()[1]
    root.destroy()
    root = Tk()
    root.geometry('400x820')
    food_id = e1
    food_num = e2
    food_tuple = return_dic[food_id]
    food_name = food_tuple[0]
    food_price = food_tuple[1]
    all_price = int(food_num) * int(food_price)
    # all_price = food_num * food_price       # 定义此次订单的总价格计算公式,
    # 调试时发现报错:TypeError: can't multiply sequence by non-int of type 'str',所以把str转化为了int
    # 判断是否符合优惠条件
    if all_price > 30:
        all_price = all_price - 5
        Label(root, text="符合优惠活动,给您减5元!").pack()
    else:
        Label(root, text="不符合优惠活动,您要不再订点?").pack()
    Label(root, text="您订了 %s 份-%s-,总价为: %d元,请选择对订单的操作(1-2):" % (food_num, food_name, all_price)).pack()
    # 把订单结果写入订单库内
    Button(root, width=15, height=2, text='保存订单（未支付）', command=lambda: menu_order211(root,food_name,food_num,all_price)).pack()
    Button(root, width=15, height=2, text='提交订单（支付）', command=lambda: menu_order212(root,food_name,food_num,all_price)).pack()
    root.mainloop()
def menu_order2(root):
    """添加订单"""
    root.destroy()
    root = Tk()
    root.geometry('400x820')
    return_list = readFile()[0]  # 调用读取food_list.txt的方法,0元素位位返回的列表
    text = ("                 %-16s%-16s%-16s%-16s" % ("菜品ID", "菜品名称", "菜品描述", "菜品价格"))
    Label(root, text=text).pack()
    for i in return_list:
        text2 = ("                 %-16s%-16s%-16s%-16s" % (i[0], i[1], i[2], i[3]))
        Label(root, text=text2).pack()
    Label(root, text="请输入您要订的菜品ID：").pack()
    e1 = tk.Entry(root)
    e1.pack()
    Label(root, text="请输入您要订的菜品份数：").pack()
    e2 = tk.Entry(root)
    e2.pack()
    Button(root, width=7, height=2, text='提交', command=lambda: menu_order21(root,e1.get(),e2.get())).place(x=300,y=750)
    root.mainloop()
def menu_order311(root,change_name,change_num,all_price):
    root.destroy()
    root = Tk()
    root.geometry('0x0')
    root.withdraw()
    with open('submit_order.txt', 'a+') as submit:
        submit.write(change_name + ',' + change_num + ',' + str(all_price) + '\n')
    tk.messagebox.showinfo(title='结果', message='提交订单成功！')
    root.deiconify()
    menu_order(root)
def menu_order31(root,change_name,change_num,return_dic):
    root.destroy()
    root = Tk()
    root.geometry('400x820')

    food_price = return_dic[change_name]
    all_price = int(change_num) * int(food_price)
    if all_price > 30:
        all_price = all_price - 5
        Label(root, text="符合优惠活动,给您减5元!").pack()
    else:
        Label(root, text="不符合优惠活动,您要不再订点?").pack()
    with open('uncommitted_order.txt', 'r') as r_w:
        lines1 = r_w.readlines()  # 获取行数
        with open('uncommitted_order.txt', 'w') as rr_w:
            for line1 in lines1:
                if change_name in line1:
                    rr_w.write(change_name + ',' + change_num + ',' + str(all_price) + '\n')
                    continue
                rr_w.write(line1)
    Label(root, text="您订了 %s 份-%s-,总价为: %d元,请选择对订单的操作(1.提交订单 2.不提交订单)" % (change_num, change_name, all_price)).pack()
    Button(root, width=15, height=2, text='提交订单',command=lambda: menu_order311(root, change_name, change_num, all_price)).pack()
    Button(root, width=15, height=2, text='不提交订单',command=lambda: menu_order(root)).pack()
def menu_order3(root):
    root.destroy()
    root = Tk()
    root.geometry('400x820')
    return_dic = readfile()[1]
    OrderList = []
    try:
        with open('uncommitted_order.txt', 'r') as file:
            for line in file.readlines():
                if line != "":
                    food = line.rstrip('\n').split(',')
                    foodname, describe, price = food[0], food[1], food[2]
                    oneFood = (foodname, describe, price)
                    OrderList.append(oneFood)
            text = ("                 %-16s%-16s%-16s" % ("订单名", "菜品份数", "总价格"))
            Label(root,text=text).pack()
            for i in OrderList:
                text2 = ("                 %-16s%-16s%-16s" % (i[0], i[1], i[2]))
                Label(root, text=text2).pack()
    except FileNotFoundError:
        print("数据文件不存在！")  # 若打开失败，输入提示信息

    Label(root, text="请输入您要修改的订单菜名:").pack()
    e1 = tk.Entry(root)
    e1.pack()
    Label(root, text="请输入您要修改的菜品份数:").pack()
    e2 = tk.Entry(root)
    e2.pack()
    Button(root, width=7, height=2, text='提交', command=lambda: menu_order31(root, e1.get(), e2.get(),return_dic)).place(x=300,y=750)
    root.mainloop()
def menu_order41(root,del_name):
    root.destroy()
    root = Tk()
    root.geometry('0x0')
    root.withdraw()
    with open('uncommitted_order.txt', 'r') as f:
        lines = f.readlines()
        with open('uncommitted_order.txt', 'w') as f_w:
            for line in lines:
                if del_name in line:
                    continue
                f_w.write(line)
    tk.messagebox.showinfo(title='结果', message='删除订单成功！')
    root.deiconify()
    menu_order(root)
def menu_order4(root):
    root.destroy()
    root = Tk()
    root.geometry('400x820')
    return_dic = readfile()[1]
    OrderList = []
    try:
        with open('uncommitted_order.txt', 'r') as file:
            for line in file.readlines():
                if line != "":
                    food = line.rstrip('\n').split(',')
                    foodname, describe, price = food[0], food[1], food[2]
                    oneFood = (foodname, describe, price)
                    OrderList.append(oneFood)
            text = ("                 %-16s%-16s%-16s" % ("订单名", "菜品份数", "总价格"))
            Label(root,text=text).pack()
            for i in OrderList:
                text2 = ("                 %-16s%-16s%-16s" % (i[0], i[1], i[2]))
                Label(root, text=text2).pack()
    except FileNotFoundError:
        print("数据文件不存在！")  # 若打开失败，输入提示信息

    Label(root, text="请输入您要删除的订单菜名:").pack()
    e1 = tk.Entry(root)
    e1.pack()
    Button(root, width=7, height=2, text='提交', command=lambda: menu_order41(root, e1.get())).place(x=300,y=750)
    root.mainloop()
def menu_order(root):
    root.destroy()
    root = Tk()
    root.geometry('400x320')
    Button(root, width=13, height=2, text='查询食堂菜单', command=lambda :menu_order1(root)).pack()
    Button(root, width=13, height=2, text='添加新订单', command=lambda :menu_order2(root)).pack()
    Button(root, width=13, height=2, text='修改未支付订单', command=lambda :menu_order3(root)).pack()
    Button(root, width=13, height=2, text='删除未支付订单', command=lambda :menu_order4(root)).pack()
    Button(root, width=13, height=2, text='返回上级菜单', command=lambda :new_main(root)).pack()
    root.mainloop()
def query_old(root):
    root.destroy()
    root = Tk()
    root.geometry('400x820')
    return_dic = readfile()[1]
    OrderList = []
    try:
        with open('submit_order.txt', 'r') as file:
            for line in file.readlines():
                if line != "":
                    food = line.rstrip('\n').split(',')
                    foodname, describe, price = food[0], food[1], food[2]
                    oneFood = (foodname, describe, price)
                    OrderList.append(oneFood)
            text = ("                 %-16s%-16s%-16s" % ("订单名", "菜品份数", "总价格"))
            Label(root, text=text).pack()
            for i in OrderList:
                text2 = ("                 %-16s%-16s%-16s" % (i[0], i[1], i[2]))
                Label(root, text=text2).pack()
    except FileNotFoundError:
        print("数据文件不存在！")  # 若打开失败，输入提示信息
    Button(root, width=13, height=2, text='返回上级菜单', command=lambda: new_main(root)).pack()
    root.mainloop()
def del_old1(root,del_name):
    root.destroy()
    root = Tk()
    root.geometry('0x0')
    root.withdraw()
    with open('submit_order.txt', 'r') as f:
        lines = f.readlines()
        with open('submit_order.txt', 'w') as f_w:
            for line in lines:
                if del_name in line:
                    continue
                f_w.write(line)
    tk.messagebox.showinfo(title='结果', message='删除订单成功！')
    root.deiconify()
    new_main(root)
def del_old(root):
    root.destroy()
    root = Tk()
    root.geometry('400x820')
    return_dic = readfile()[1]
    OrderList = []
    try:
        with open('submit_order.txt', 'r') as file:
            for line in file.readlines():
                if line != "":
                    food = line.rstrip('\n').split(',')
                    foodname, describe, price = food[0], food[1], food[2]
                    oneFood = (foodname, describe, price)
                    OrderList.append(oneFood)
            text = ("                 %-16s%-16s%-16s" % ("订单名", "菜品份数", "总价格"))
            Label(root, text=text).pack()
            for i in OrderList:
                text2 = ("                 %-16s%-16s%-16s" % (i[0], i[1], i[2]))
                Label(root, text=text2).pack()
    except FileNotFoundError:
        print("数据文件不存在！")  # 若打开失败，输入提示信息
    Label(root, text="请输入您要删除的订单菜名:").pack()
    e1 = tk.Entry(root)
    e1.pack()
    Button(root, width=7, height=2, text='提交', command=lambda: del_old1(root, e1.get())).place(x=300, y=750)
    Button(root, width=13, height=2, text='返回上级菜单', command=lambda: new_main(root)).pack()
    root.mainloop()
def f1():
    sys.exit(0)
def new_main(root):
    root.destroy()
    root = Tk()
    root.geometry('400x320')
    Label(root,text='"   今日优惠活动:订餐满30减5元!"').pack()
    Button(root, width=13, height=2, text='下单', command=lambda:menu_order(root)).pack()
    Button(root, width=13, height=2, text='查询历史订单', command=lambda:query_old(root)).pack()
    Button(root, width=13, height=2, text='删除历史订单', command=lambda:del_old(root)).pack()
    Button(root, width=13, height=2, text='退出', command=f1).pack()
    root.mainloop()
root = Tk()
new_main(root)
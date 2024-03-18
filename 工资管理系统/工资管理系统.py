import tkinter as tk
from tkinter import messagebox

def old():
    # 员工信息列表
    data_list = []

    # 定义员工类
    class Staff(object):
        def __init__(self, num, name, gender, post):
            self.num = num  # 工号
            self.name = name  # 姓名
            self.gender = gender  # 性别
            self.post = post  # 岗位
            self.wages = []  # 工资
            self.total = 0  # 总工资

    # 定义修改密码函数
    def change_pw():
        # ur为用户输入的账号
        ur = input('请输入账号:')
        # pw为用户输入的旧密码
        pw = input('请输入旧密码:')
        # npw为用户输入的新密码
        npw = input('请输入新密码:')
        # 遍历用户账号列表
        for i in users:
            # 若存在账号与密码匹配的元素
            if ur == i[0] and pw == i[1]:
                # 则将旧的账号密码移除
                users.remove(i)
                # 加入新的账号密码
                users.append([ur, npw])
                # 提示修改成功
                print('修改成功！')
                input('按回车继续....')
                return 0
        # 若不存在 则提示用户名或密码错误
        print('用户名或密码错误！')

    # 定义添加员工函数
    def add_staff():
        # num存储要添加的员工工号
        num = input('请输入要添加的员工工号:')
        # 遍历员工列表
        for i in data_list:
            # 检查该工号是否已经存在
            if i.num == num:
                # 若以存在，则输出，并结束函数
                print('该工号已经存在！')
                input('按回车继续....')
                return 0
        # 若不存在，则继续输入name，存储员工姓名
        name = input('请输入要添加的员工姓名:')
        # gender 存储员工性别
        gender = input('请输入要添加的员工性别:')
        # post 存储员工岗位
        post = input('请输入要添加的员工岗位:')
        # 在员工列表中添加新的Staff员工类对象
        data_list.append(Staff(num, name, gender, post))
        print('插入成功！')

    # 定义删除员工函数
    def dele_staff():
        # num存储要删除的员工工号
        num = input('请输入要删除的员工工号:')
        # 遍历员工列表
        for i in data_list:
            # 查看要删除的员工工号是否存在
            if i.num == num:
                # 若存在 则删除，并提示删除成功
                data_list.remove(i)
                print('删除成功！')
                input('按回车继续....')
                return 0
        # 若不存在 则提示没有找到该员工工号
        print('没有找到该员工工号！')

    # 定义修改员工函数
    def change_staff():
        # num存储用户输入的要修改的员工号
        num = input('请输入要修改的员工工号:')
        # 遍历员工列表，查看该员工号是否存在
        for i in data_list:
            # 如果该员工号存在
            if i.num == num:
                # name存储需要更新的员工姓名
                name = input('请输入新的员工姓名:')
                # gender 存储性别
                gender = input('请输入新的员工性别:')
                # post 存储岗位
                post = input('请输入新的员工岗位:')
                # 将该员工的对应信息修改为输入后的新信息
                i.name = name
                i.gender = gender
                i.post = post
                # 提示修改成功
                print('修改成功！')
                return 0
        # 若不存在 则提示没有找到该员工号
        print('没有找到该员工工号！')

    # 定义添加工资函数
    def add_wage():
        # num存储用户输入的添加工资的员工号
        num = input('请输入要添加的员工工号:')
        # 遍历员工列表
        for i in data_list:
            # 若该员工号存在
            if i.num == num:
                # wage存储需要添加的工资信息
                wage = int(input('请输入要添加的工资:'))
                # 将该员工的工资列表中添加新工资
                i.wages.append(wage)
                # 更新员工的总工资信息
                i.total = sum(i.wages)
                print('插入成功！')
                return 0
        # 若员工号不存在，则提示错误
        print('没有找到该员工工号！')

    # 定义删除员工工资函数
    def dele_wage():
        # num存储用户输入的删除工资的员工号
        num = input('请输入要删除的员工工号:')
        # 遍历员工列表
        for i in data_list:
            # 若该员工号存在
            if i.num == num:
                print('该员工工资有以下组成:')
                # 遍历该员工的工资列表
                for wage in i.wages:
                    # 输出每一项工资
                    print(wage, end=' ')
                # wage存储用户输入的需要删除的工资
                wage = int(input('请输入要删除的工资:'))
                # 尝试删除该工资
                try:
                    # 若顺利删除，则提示删除成功
                    i.wages.remove(wage)
                    print('删除成功！')
                    # 更新总工资属性
                    i.total = sum(i.wages)
                except:
                    # 若错误删除，则说明该员工没有该项工资
                    print('该员工没有该项工资')
                return 0
        # 若不存在 则提示没有找到该员工号
        print('没有找到该员工工号！')

    # 定义修改员工工资函数
    def change_wage():
        # num存储用户输入的修改工资的员工号
        num = input('请输入要修改的员工工号:')
        # 遍历员工列表
        for i in data_list:
            # 若该员工号存在
            if i.num == num:
                print('该员工工资有以下组成:')
                # 遍历该员工的工资列表
                for wage in i.wages:
                    # 输出每一项工资
                    print(wage, end=' ')
                wage = int(input('请输入要修改的工资:'))
                # 尝试删除该工资
                try:
                    # 若删除成功
                    i.wages.remove(wage)
                    wage = int(input('请输入修改后的工资:'))
                    # 则添加入新输入的工资
                    i.wages.append(wage)
                    print('修改成功！')
                    # 更新总工资属性
                    i.total = sum(i.wages)
                except:
                    # 若错误删除，则说明该员工没有该项工资
                    print('该员工没有该项工资')
                return 0
        # 若不存在 则提示没有找到该员工号
        print('没有找到该员工工号！')

    # 定义输出单个员工信息函数
    def show_one():
        # num存储用户输入的删除工资的员工号
        num = input('请输入要查询的员工工号:')
        # 遍历员工列表
        for i in data_list:
            # 若该员工号存在
            if i.num == num:
                print('     工号', end='  ')
                print('    姓名', end='  ')
                print('    性别', end='  ')
                print('    岗位', end='  ')
                print('    总薪资', end='  ')
                print('    薪资列表：', end=' ')
                print('\n')
                print('{:>8}'.format(i.num), end=' ')
                print('{:>8}'.format(i.name), end=' ')
                print('{:>8}'.format(i.gender), end=' ')
                print('{:>8}'.format(i.post), end=' ')
                print('{:>8}'.format(i.total), end=' ')
                print('     ', end=' ')
                for wage in i.wages:
                    print(wage, end=' ')
                print('', end='\n')
                return 0
        # 若不存在 则提示没有找到该员工号
        print('没有找到该员工工号！')

    def show():
        info1 = '''

                        1、按照工资升序显示
                        2、按照工资降序显示

                        '''
        print(info1)
        print('请输入选项:')
        c1 = int(input())
        if c1 == 1:
            show_up()
        elif c1 == 2:
            show_down()
        else:
            print('输入有误，请重新输入')

    # 定义升序输出所有员工信息函数
    def show_up():
        # 将员工列表按照员工工资升序排序，形成新列表l
        l = sorted(data_list, key=lambda x: x.total)
        # 遍历新列表l
        print('     工号', end='  ')
        print('    姓名', end='  ')
        print('    性别', end='  ')
        print('    岗位', end='  ')
        print('    总薪资', end='  ')
        print('    薪资列表：', end=' ')
        print('\n')
        for i in l:
            # 依次输出每名员工所有信息
            # 则输出该名员工的全部信息
            print('{:>8}'.format(i.num), end=' ')
            print('{:>8}'.format(i.name), end=' ')
            print('{:>8}'.format(i.gender), end=' ')
            print('{:>8}'.format(i.post), end=' ')
            print('{:>8}'.format(i.total), end=' ')
            print('     ', end=' ')
            for wage in i.wages:
                print(wage, end=',')
            print('', end='\n')

    # 定义降序输出所有员工信息函数
    def show_down():
        # 将员工列表按照员工工资降序排序，形成新列表l
        l = sorted(data_list, key=lambda x: x.total, reverse=True)
        # 遍历新列表l
        print('     工号', end='  ')
        print('    姓名', end='  ')
        print('    性别', end='  ')
        print('    岗位', end='  ')
        print('    总薪资', end='  ')
        print('    薪资列表：', end=' ')
        print('\n')
        for i in l:
            # 依次输出每名员工所有信息
            # 则输出该名员工的全部信息
            print('{:>8}'.format(i.num), end=' ')
            print('{:>8}'.format(i.name), end=' ')
            print('{:>8}'.format(i.gender), end=' ')
            print('{:>8}'.format(i.post), end=' ')
            print('{:>8}'.format(i.total), end=' ')
            print('     ', end=' ')
            for wage in i.wages:
                print(wage, end=',')
            print('', end='\n')

    # 定义显示某岗位所有员工信息函数
    def show_post():
        # post存储用户输入的岗位名称
        post = input('请输入岗位名称：')
        print('该岗位有以下员工：')
        # 遍历员工列表
        print('     工号', end='  ')
        print('    姓名', end='  ')
        print('    性别', end='  ')
        print('    岗位', end='  ')
        print('    总薪资', end='  ')
        print('    薪资列表：', end=' ')
        print('\n')
        for i in data_list:
            # 匹配所有该岗位员工
            if i.post == post:
                # 输出该员工所有信息
                # 依次输出每名员工所有信息
                print('{:>8}'.format(i.num), end=' ')
                print('{:>8}'.format(i.name), end=' ')
                print('{:>8}'.format(i.gender), end=' ')
                print('{:>8}'.format(i.post), end=' ')
                print('{:>8}'.format(i.total), end=' ')
                print('     ', end=' ')
                for wage in i.wages:
                    print(wage, end=',')
                print('', end='\n')

    # 定义显示某岗位薪资水平函数
    def search_post():
        # post存储用户输入的岗位名称
        post = input('请输入岗位名称：')
        # 定义l存储所有该岗位员工的总薪资
        l = []
        # 遍历员工列表
        for i in data_list:
            # 匹配所有该岗位员工
            if i.post == post:
                # 将该员工的总薪资加入到列表l中
                l.append(i.total)
        # 若没有该岗位员工，则输出提示
        if not l:
            print('没有该岗位的员工数据!')
            input('按回车继续....')
        # sumwage存储所有员工总薪资综合
        sumwage = sum(l)
        # lenwage存储员工个数
        lenwage = len(l)
        # avgwage计算平均薪资
        avgwage = sumwage / lenwage
        # maxwage存储最高薪资
        maxwage = max(l)
        # minwage存储最低薪资
        minwage = min(l)
        # 输出平均薪资，最高薪资，最低薪资
        print('该岗位平均薪资为：', end=' ')
        print(avgwage)
        print('该岗位最高薪资为：', end=' ')
        print(maxwage)
        print('该岗位最低薪资为：', end=' ')
        print(minwage)

    # 定义保存文件函数
    def save():
        # f指针存储文件指针，打开文件save.txt
        f = open('data.txt', 'w', encoding='utf-8')
        # data存储文件数据列表
        data = []
        # 遍历员工信息列表
        for i in data_list:
            # 定义row 存储文件每一行的数据
            row = []
            # row中依次添加单名员工的各个信息
            row.append(i.num)
            row.append(i.name)
            row.append(i.gender)
            row.append(i.post)
            for wage in i.wages:
                row.append(str(wage))
            row.append(str(i.total))
            # 将一行数据添加到data列表中
            data.append(row)
        # 遍历data列表
        for i in data:
            # 将data列表的每个元素以逗号连接成字符串
            s = ','.join(i)
            # 写入文件f中
            f.write(s + '\n')
        # 提示保存成功
        f.close()
        f = open('user.txt', 'w', encoding='utf-8')
        data = []
        # 遍历员工信息列表
        for i in users:
            # 定义row 存储文件每一行的数据
            row = []
            # row中依次添加单名员工的各个信息
            row.append(i[0])
            row.append(i[1])
            data.append(row)
        # 遍历data列表
        for i in data:
            # 将data列表的每个元素以逗号连接成字符串
            s = ','.join(i)
            # 写入文件f中
            f.write(s + '\n')
        print('保存成功！')

    def load():
        with open('data.txt', 'r', encoding='utf-8') as f:
            data = f.readlines()
        for i in data:
            try:
                l = i.replace('\n', '').split(',')
                one = Staff(l[0], l[1], l[2], l[3])
                one.wages = [int(wage) for wage in l[4:len(l)-1]]
                one.total = int(l[-1])
                data_list.append(one)
            except:
                continue

    # 定义菜单函数
    def stuff_menu():
        info = '''
                ==========员工信息表==========

                1、增加员工信息
                2、删除员工信息
                3、修改员工信息

                =============================
                '''
        # 打印菜单
        print(info)

    def run_stuff_menu():
        stuff_menu()
        print('请输入选项:')
        c = int(input())
        # 根据用户输入的不同选项调用不同的函数
        if c == 1:
            add_staff()
        elif c == 2:
            dele_staff()
        elif c == 3:
            change_staff()
        else:
            print('输入有误，请重新输入')

    def wage_menu():
        info = '''
                ==========员工信息表==========

                1、增加工资信息
                2、删除工资信息
                3、修改工资信息

                =============================
                '''
        # 打印菜单
        print(info)

    def run_wage_menu():
        wage_menu()
        print('请输入选项:')
        c = int(input())
        # 根据用户输入的不同选项调用不同的函数
        if c == 1:
            add_wage()
        elif c == 2:
            dele_wage()
        elif c == 3:
            change_wage()
        else:
            print('输入有误，请重新输入')

    def search_menu():
        # 定义菜单信息
        info = '''
               ==========员工信息表==========

               1、查询单个员工信息
               2、查询所有员工信息
               3、查询单个岗位所有员工信息
               4、查询单个岗位薪资信息

               =============================
               '''
        # 打印菜单
        print(info)

    def run_search_menu():
        search_menu()
        print('请输入选项:')
        c = int(input())
        # 根据用户输入的不同选项调用不同的函数
        if c == 1:
            show_one()
        elif c == 2:
            show()
        elif c == 3:
            show_post()
        elif c == 4:
            search_post()
        else:
            print('输入有误，请重新输入')

    def menu():
        # 定义菜单信息
        info = '''
            ==========员工信息表==========

            1、员工信息维护
            2、工资信息维护
            3、信息查询统计
            4、保存信息
            5、修改账号密码
            6、注册新账号
            7、退出

            =============================
            '''
        # 打印菜单
        print(info)
    def setup():
        user = input('请输入账号：')
        pw = input('请输入密码：')
        print('注册成功！')
        users.append([user,pw])
    def run_menu(c):

        # 根据用户输入的不同选项调用不同的函数
        if c == 1:
            run_stuff_menu()
        elif c == 2:
            run_wage_menu()
        elif c == 3:
            run_search_menu()
        elif c == 4:
            save()
        elif c == 5:
            change_pw()
        elif c == 6:
            setup()
        else:
            print('输入有误，请重新输入')

    # 程序主循环
    # login()
    load()
    while True:
        # 打印菜单
        menu()
        # c存储用户输入的选项
        print('请输入选项:')
        c = int(input())
        # 根据用户输入的不同选项调用不同的函数
        if c == 7:
            break
        run_menu(c)
        input('按回车继续...')
class LoginPage:
#创建登录页面
    def __init__(self,master):
        self.top=master
        self.top.title("登录页")
        self.top.geometry("500x300+300+300")
        self.page=tk.Frame(top)
        self.page.pack()
        self.username=tk.StringVar()
        self.password=tk.StringVar()
        tk.Label(self.page).grid(row=0,column=0)
        tk.Label(self.page,text="账户:").grid(row=1,column=1,pady=20)       #账户框
        tk.Entry(self.page,textvariable=self.username).grid(row=1,column=2)
        tk.Label(self.page,text="密码:").grid(row=2,column=1,pady=20)       #密码框
        tk.Entry(self.page,show="*",textvariable=self.password).grid(row=2,column=2)
        tk.Button(self.page,text="登录",command=self.login).grid(row=3,column=1,pady=20)   #登录按钮
        # tk.Button(self.page, text="注册", command=self.setup).grid(row=3, column=2, pady=20)  # 登录按钮
        tk.Button(self.page,text="退出",command=self.page.quit).grid(row=3,column=3,pady=20) #退出按钮
    def login(self):
    #判断账户密码是否正确
            flag = 0
            name=self.username.get()
            pwd=self.password.get()
            for i in users:
                if name==i[0]:
                    flag = 1
                    if pwd==i[1]:
                        self.page.destroy()
                        self.top.destroy()
                        old()
                    else:
                        messagebox.showwarning(title="警告",message="登录失败，密码错误")
            if not flag:
                messagebox.showwarning(title="警告",message="登录失败，账户不存在")

with open('user.txt','r') as f:
    filedata = f.readlines()
users = []
for i in filedata:
    users.append([i.replace('\n','').split(',')[0],i.replace('\n','').split(',')[1]])
top=tk.Tk()
LoginPage(master=top)
top.mainloop()






from tkinter import *
import tkinter as tk
import tkinter.messagebox
# 面向对象技术
# 类与对象的创建
class Admin:
    def __init__(self,username,password):
        self.username = username
        self.password = password
# 继承的使用
class User(Admin):
    def __init__(self,username,password,uid,phone,add):
        # 私有属性或方法的使用
        Admin.__init__(self,username,password)
        self.uid = uid
        self.phone = phone
        self.add = add
# 数据的存储读取
with open('user.txt',encoding='utf8') as f:
    userlist = [User(*i.replace('\n','').split(';')) for i in f.readlines()]
with open('check.txt',encoding='utf8') as f:
    checklist = [i.replace('\n','').split(';') for i in f.readlines()]
with open('vaccine.txt',encoding='utf8') as f:
    vaccinelist = [i.replace('\n', '').split(';') for i in f.readlines()]
with open('info.txt',encoding='utf8') as f:
    infolist = {i.replace('\n','').split(';')[0]:i.replace('\n','').split(';')[1:] for i in f.readlines()}
def login_check():
    def login(us):
        # 整合各个功能模块
        def f1():
            # 数据的增删改查
            def f11():
                def insert():
                    userlist.append(User(*e.get().split(';')))
                    tk.messagebox.showinfo(message='插入成功')
                root3 = Toplevel(root2)
                root3.title('疫情防控系统')
                root3.geometry("600x600")
                Label(root3, text='请输入用户的以下信息，以;分隔：').pack()
                Label(root3, text='账号 密码 身份证号 电话号码 家庭住址').pack()
                e = Entry(root3,width=70)
                e.pack()
                Button(root3, text='提交', command=insert).pack()
            def f12():
                def delete():
                    userlist.remove(userlist[int(e.get()) - 1])
                    tk.messagebox.showinfo(message='删除成功')
                root3 = Toplevel(root2)
                root3.title('疫情防控系统')
                root3.geometry("600x600")
                # 序列数据的操作
                for i in range(len(userlist)):
                    Label(root3,text=' '.join([str(i+1),userlist[i].uid,userlist[i].phone,userlist[i].add])).pack()
                Label(root3, text='请输入要删除的序号').pack()
                e = Entry(root3)
                e.pack()
                Button(root3, text='提交', command=delete).pack()
            def f13():
                def change():
                    userlist.remove(userlist[int(e0.get()) - 1])
                    userlist.append(User(*e.get().split(';')))
                    tk.messagebox.showinfo(message='修改成功')
                root3 = Toplevel(root2)
                root3.title('疫情防控系统')
                root3.geometry("600x600")
                for i in range(len(userlist)):
                    Label(root3,text=' '.join([str(i+1),userlist[i].uid,userlist[i].phone,userlist[i].add])).pack()
                Label(root3, text='请输入要修改用户的序号：').pack()
                e0 = Entry(root3)
                e0.pack()
                Label(root3, text='请输入修改用户的以下信息，以;分隔：').pack()
                Label(root3, text='账号 密码 身份证号 电话号码 家庭住址').pack()
                e = Entry(root3,width=70)
                e.pack()
                Button(root3, text='提交', command=change).pack()
            def f14():
                root3 = Toplevel(root2)
                root3.title('疫情防控系统')
                root3.geometry("600x600")
                for i in range(len(userlist)):
                    Label(root3, text=' '.join([str(i + 1), userlist[i].uid, userlist[i].phone, userlist[i].add])).pack()
            root2 = Toplevel(root1)
            root2.title('疫情防控系统')
            root2.geometry("300x150")
            Button(root2, text='增加用户信息', command=f11).pack()
            Button(root2, text='删除用户信息', command=f12).pack()
            Button(root2, text='修改用户信息', command=f13).pack()
            Button(root2, text='查询用户信息', command=f14).pack()
        def f2():
            def f21():
                def search():
                    t.delete('0.0',END)
                    for i in checklist:
                        if not e0.get() or i[0] == e0.get():
                            if not e1.get() or i[1] == e1.get():
                                t.insert('0.0',' '.join(i)+'\n')
                root3 = Toplevel(root2)
                root3.title('疫情防控系统')
                root3.geometry("600x600")
                Label(root3, text='请输入以下筛选信息，若为空则为不限制').pack()
                Label(root3, text='身份证号：').pack()
                e0 = Entry(root3, width=70)
                e0.pack()
                Label(root3, text='日期（例2022-6-18）：').pack()
                e1 = Entry(root3, width=70)
                e1.pack()
                Button(root3, text='提交', command=search).pack()
                # Text组件的使用
                t = Text(root3)
                t.pack()
            def f11():
                def insert():
                    checklist.append(e.get().split(';'))
                    tk.messagebox.showinfo(message='插入成功')

                root3 = Toplevel(root2)
                root3.title('疫情防控系统')
                root3.geometry("600x600")
                Label(root3, text='请输入用户的以下信息，以;分隔：').pack()
                Label(root3, text='身份证号 检测日期 检测结果').pack()
                e = Entry(root3, width=70)
                e.pack()
                Button(root3, text='提交', command=insert).pack()
            def f12():
                def delete():
                    checklist.remove(checklist[int(e.get()) - 1])
                    tk.messagebox.showinfo(message='删除成功')

                root3 = Toplevel(root2)
                root3.title('疫情防控系统')
                root3.geometry("600x600")
                for i in range(len(checklist)):
                    Label(root3, text=' '.join([str(i + 1), checklist[i][0], checklist[i][1], checklist[i][2]])).pack()
                Label(root3, text='请输入要删除的序号').pack()
                e = Entry(root3)
                e.pack()
                Button(root3, text='提交', command=delete).pack()
            def f13():
                def change():
                    checklist.remove(checklist[int(e0.get()) - 1])
                    checklist.append(e.get().split(';'))
                    tk.messagebox.showinfo(message='修改成功')

                root3 = Toplevel(root2)
                root3.title('疫情防控系统')
                root3.geometry("600x600")
                for i in range(len(checklist)):
                    Label(root3, text=' '.join([str(i + 1), checklist[i][0], checklist[i][1], checklist[i][2]])).pack()
                Label(root3, text='请输入要修改用户的序号：').pack()
                e0 = Entry(root3)
                e0.pack()
                Label(root3, text='请输入修改用户的以下信息，以;分隔：').pack()
                Label(root3, text='身份证号 检测日期 检测结果').pack()
                e = Entry(root3, width=70)
                e.pack()
                Button(root3, text='提交', command=change).pack()
            root2 = Toplevel(root1)
            root2.title('疫情防控系统')
            root2.geometry("300x150")
            if us != 'admin':
                Button(root2, text='搜索核酸检测信息', command=f21).pack()
            else:
                Button(root2, text='增加核酸检测信息', command=f11).pack()
                Button(root2, text='删除核酸检测信息', command=f12).pack()
                Button(root2, text='修改核酸检测信息', command=f13).pack()
        def f3():
            def f21():
                def search():
                    t.delete('0.0',END)
                    for i in vaccinelist:
                        if not e0.get() or i[0] == e0.get():
                            if not e1.get() or i[1] == e1.get():
                                t.insert('0.0',' '.join(i)+'\n')
                root3 = Toplevel(root2)
                root3.title('疫情防控系统')
                root3.geometry("600x600")
                Label(root3, text='请输入以下筛选信息，若为空则为不限制').pack()
                Label(root3, text='身份证号：').pack()
                e0 = Entry(root3, width=70)
                e0.pack()
                Label(root3, text='日期（例2022-6-18）：').pack()
                e1 = Entry(root3, width=70)
                e1.pack()
                Button(root3, text='提交', command=search).pack()
                t = Text(root3)
                t.pack()
            def f11():
                def insert():
                    vaccinelist.append(e.get().split(';'))
                    tk.messagebox.showinfo(message='插入成功')
                root3 = Toplevel(root2)
                root3.title('疫情防控系统')
                root3.geometry("600x600")
                Label(root3, text='请输入用户的以下信息，以;分隔：').pack()
                Label(root3, text='身份证号 检测日期 检测结果').pack()
                e = Entry(root3, width=70)
                e.pack()
                Button(root3, text='提交', command=insert).pack()
            def f12():
                def delete():
                    vaccinelist.remove(vaccinelist[int(e.get()) - 1])
                    tk.messagebox.showinfo(message='删除成功')

                root3 = Toplevel(root2)
                root3.title('疫情防控系统')
                root3.geometry("600x600")
                for i in range(len(vaccinelist)):
                    Label(root3, text=' '.join([str(i + 1), vaccinelist[i][0], vaccinelist[i][1], vaccinelist[i][2]])).pack()
                Label(root3, text='请输入要删除的序号').pack()
                e = Entry(root3)
                e.pack()
                Button(root3, text='提交', command=delete).pack()
            def f13():
                def change():
                    checklist.remove(vaccinelist[int(e0.get()) - 1])
                    checklist.append(e.get().split(';'))
                    tk.messagebox.showinfo(message='修改成功')

                root3 = Toplevel(root2)
                root3.title('疫情防控系统')
                root3.geometry("600x600")
                for i in range(len(vaccinelist)):
                    Label(root3, text=' '.join([str(i + 1), vaccinelist[i][0], vaccinelist[i][1], vaccinelist[i][2]])).pack()
                Label(root3, text='请输入要修改用户的序号：').pack()
                e0 = Entry(root3)
                e0.pack()
                Label(root3, text='请输入修改用户的以下信息，以;分隔：').pack()
                Label(root3, text='身份证号 检测日期 第几针').pack()
                e = Entry(root3, width=70)
                e.pack()
                Button(root3, text='提交', command=change).pack()
            root2 = Toplevel(root1)
            root2.title('疫情防控系统')
            root2.geometry("300x150")
            if us != 'admin':
                Button(root2, text='搜索疫苗接种信息', command=f21).pack()
            else:
                Button(root2, text='增加疫苗接种信息', command=f11).pack()
                Button(root2, text='删除疫苗接种信息', command=f12).pack()
                Button(root2, text='修改疫苗接种信息', command=f13).pack()
        def f4():
            def insert():
                infolist[us] = [e.get(),e1.get()]
                tk.messagebox.showinfo(message='填报成功')
            root2 = Toplevel(root1)
            root2.title('疫情防控系统')
            root2.geometry("300x150")
            Label(root2, text='请输入解封时间：').pack()
            e = Entry(root2,)
            e.pack()
            Label(root2, text='请输入具体困难：').pack()
            e1 = Entry(root2, width=70)
            e1.pack()
            Button(root2, text='提交', command=insert).pack()
        def f5():
            # Toplevel组件的使用
            root2 = Toplevel(root1)
            root2.title('疫情防控系统')
            root2.geometry("600x600")
            for i in infolist.keys():
                Label(root2, text=f'身份证：{i} 解封时间：{infolist[i][0]} 具体困难：{infolist[i][1]}').pack()
            Label(root2, text=f'当前共计{len(infolist)}人处于隔离中').pack()
        root.destroy()
        root1 = Tk()
        root1.title('疫情防控系统')
        root1.geometry("300x150")
        if us == 'admin':
            Button(root1, text='用户信息管理', command=f1).pack()
        Button(root1, text='核酸检测信息', command=f2).pack()
        Button(root1, text='疫苗接种信息', command=f3).pack()
        if us == 'admin':
            Button(root1, text='疫情实时情况', command=f5).pack()
        else:
            Button(root1, text='疫情实时情况', command=f4).pack()
    flag = 1

    for i in userlist:
        if e1.get() == 'admin' and e2.get() == 'admin':
            login(e1.get())
            flag = 0
            break
        if e1.get() == i.username and e2.get() == i.password:
            login(i.uid)
            flag = 0
            break
    if flag:
        tk.messagebox.showinfo(message='用户名密码错误！')
# 图形界面设计
root = Tk()
root.title('疫情防控系统')
root.geometry("300x130")
Label(root, text='账号：').pack()
e1 = Entry(root)
e1.pack()
# Label组件使用
Label(root, text='密码：').pack()
# Entry组件使用
e2 = Entry(root, show="*")
e2.pack()
# Button组件使用
Button(root, text='登录', command=login_check).pack()
root.mainloop()
with open('user.txt','w',encoding='utf8') as f:
    for i in userlist:
        f.write(';'.join([i.username,i.password,i.uid,i.phone,i.add])+'\n')
with open('check.txt','w',encoding='utf8') as f:
    for i in checklist:
        f.write(';'.join(i)+'\n')
with open('vaccine.txt','w',encoding='utf8') as f:
    for i in vaccinelist:
        f.write(';'.join(i) + '\n')
with open('info.txt','w',encoding='utf8') as f:
    for i in infolist.keys():
        f.write(';'.join([i]+infolist[i])+'\n')

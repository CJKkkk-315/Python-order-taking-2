import csv
flog = open('error.log','a+')
class People(object):
    def __init__(self, pid, name, department, level,state):
        self.pid = pid
        self.name = name
        self.department = department
        self.level = level
        self.state = state
    def show(self):
        print('工号：{} 姓名：{} 部门：{} 等级：{} 状态：{}'.format(self.pid,self.name,self.department,self.level,self.state))
class Item(object):
    def __init__(self, iid, name, price, num):
        self.iid = iid
        self.name = name
        self.price = price
        self.num = num
    def show(self):
        print('产品编号：{} 产品名：{} 指导价格：{} 库存：{}'.format(self.iid,self.name,self.price,self.num))
class Sell(object):
    def __init__(self, sid, date, pid,iid,price,num):
        self.sid = sid
        self.date = date
        self.pid = pid
        self.iid = iid
        self.price = price
        self.num = num
    def show(self):
        print('订单号：{} 日期：{} 员工工号：{} 产品编号：{} 价格：{} 数量：{}'.format(self.sid,self.date,self.pid,self.iid,self.price,self.num))
peoples = []
sells = []
items = []
def add_people():
    pid = input('请输入要添加的员工工号:')
    for i in peoples:
        if i.pid == pid:
            print('该工号已经存在！')
            input('按回车继续....')
            return 0
    name = input('请输入要添加的员工姓名:')
    department = input('请输入要添加的员工部门:')
    level = input('请输入要添加的员工等级:')
    state = input('请输入要添加的员工状态:')
    peoples.append(People(pid, name, department, level,state))
    print('插入成功！')
def dele_people():
    pid = input('请输入要删除的员工工号:')
    for i in peoples:
        if i.pid == pid:
            if pid in [i.pid for i in sells]:
                peoples[[i.pid for i in peoples].index(pid)].state = '离职'
                print('错误！仍有销售记录，将员工设置为离职')
                flog.write('错误！仍有销售记录，将员工设置为离职\n')
                return 0
            peoples.remove(i)
            print('删除成功！')
            input('按回车继续....')
            return 0
    print('没有找到该员工工号！')
def change_people():
    pid = input('请输入要修改的员工工号:')
    for i in peoples:
        if i.pid == pid:
            peoples.remove(i)
            name = input('请输入要修改的员工姓名:')
            department = input('请输入要修改的员工部门:')
            level = input('请输入要修改的员工等级:')
            state = input('请输入要修改的员工状态:')
            peoples.append(People(pid, name, department, level, state))
            print('修改成功！')
    print('没有找到该员工工号！')
def add_item():
    iid = input('请输入要添加的产品编号:')
    for i in items:
        if i.iid == iid:
            print('该产品已经存在！')
            input('按回车继续....')
            return 0
    name = input('请输入要添加的产品名:')
    price = input('请输入要添加的产品指导价格:')
    num = input('请输入要添加的产品库存:')
    items.append(Item(iid, name, price, num))
    print('插入成功！')
def dele_item():
    iid = input('请输入要删除的产品编号:')
    for i in items:
        if i.iid == iid:
            if iid in [i.iid for i in sells]:
                items[[i.iid for i in items].index(iid)].num = '0'
                print('错误！仍有销售记录，已经库存清零')
                flog.write('错误！仍有销售记录，已经库存清零\n')
                return 0
            items.remove(i)
            print('删除成功！')
            input('按回车继续....')
            return 0
    print('没有找到该产品编号')
def change_item():
    iid = input('请输入修改的产品编号:')
    for i in peoples:
        if i.iid == iid:
            items.remove(i)
            name = input('请输入要修改的新产品名:')
            price = input('请输入要修改的新产品指导价格:')
            num = input('请输入要修改的新产品库存:')
            items.append(Item(iid, name, price, num))
            print('修改成功！')
    print('没有找到该产品编号！')
def change_item_num():
    iid = input('请输入修改的产品编号:')
    for i in peoples:
        if i.iid == iid:
            num = input('请输入要更新的产品库存:')
            i.num = num
            print('修改成功！')
    print('没有找到该产品编号！')
def add_sell():
    sid = input('请输入要添加的订单号:')
    for i in sells:
        if i.sid == sid:
            print('该订单号已经存在！')
            input('按回车继续....')
            return 0
    date = input('请输入日期,月日形式:')
    pid = input('请输入销售员工工号:')
    if pid not in [i.pid for i in peoples] or peoples[[i.pid for i in peoples].index(pid)].state == '离职':
        print('错误！该员工不存在或已离职！')
        flog.write('错误！该员工不存在或已离职！\n')
        return 0
    iid = input('请输入产品编号:')
    if iid not in [i.iid for i in items] or items[[i.iid for i in items].index(iid)].num == '0':
        print('错误！该商品不存在或没有库存！')
        flog.write('错误！该商品不存在或没有库存！\n')
        return 0
    price = input('请输入价格:')
    if float(items[[i.iid for i in items].index(iid)].price) > float(price):
        print('错误！价格不可低于指导价格！')
        flog.write('错误！价格不可低于指导价格！\n')
        return 0
    num = input('请输入数量:')
    if float(items[[i.iid for i in items].index(iid)].num) < float(num):
        print('错误！数量不可高于库存！')
        flog.write('错误！数量不可高于库存！\n')
        return 0
    sells.append(Sell(sid, date, pid, iid,price,num))
    items[[i.iid for i in items].index(iid)].num = str(int(items[[i.iid for i in items].index(iid)].num) - int(num))
    print('插入成功！')
def dele_sell():
    sid = input('请输入要删除的订单号:')
    for i in sells:
        if i.sid == sid:
            sells.remove(i)
            print('删除成功！')
            input('按回车继续....')
            return 0
    print('没有找到该订单号')
def change_sell():
    sid = input('请输入修改的订单号:')
    for i in sells:
        if i.sid == sid:
            items.remove(i)
            date = input('请输入要修改的新日期:')
            pid = input('请输入要修改的新员工号:')
            iid = input('请输入要修改的新产品编号:')
            price = input('请输入要修改的新价格:')
            num = input('请输入要修改的新数量:')
            sells.append(Sell(sid, date, pid, iid,price,num))
            print('修改成功！')
    print('没有找到该订单号！')
def search_people():
    key = input('请输入员工姓名或者工号：')
    for i in peoples:
        if i.pid == key or i.name == key:
            i.show()
def show_people():
    for i in range(len(peoples)):
        peoples[i].show()
        if i % 5 == 0 and i:
            while True:
                c = input('输入1跳转到下一页，0返回')
                if c == '1':
                    break
                elif c == '0':
                    return 0
                else:
                    print('输入错误!')
def search_item():
    key = input('请输入产品名或者产品编号：')
    for i in items:
        if i.iid == key or key in i.name:
            i.show()
def show_item():
    for i in range(len(items)):
        items[i].show()
        if i % 5 == 0 and i:
            while True:
                c = input('输入1跳转到下一页，0返回')
                if c == '1':
                    break
                elif c == '0':
                    return 0
                else:
                    print('输入错误!')
def search_sell():
    date = input('请输入日期,月日形式(若不需要此条件则不输入):')
    pid = input('请输入员工工号(若不需要此条件则不输入):')
    iid = input('请输入产品编号(若不需要此条件则不输入):')
    res = []
    for i in sells:
        if (not date or i.date == date) and (not pid or i.pid == pid) and (not iid or i.iid == iid):
            res.append(i)
    for i in res:
        i.show()
    print('共有{}条数据结果。'.format(len(res)))
def rank_people():
    ls = [[i.pid,i.name,0] for i in peoples]
    for i in sells:
        for j in ls:
            if j[0] == i.pid:
                j[2] += float(i.num)*float(i.price)
                break
    ls.sort(key=lambda x:x[2],reverse=True)
    print('销售额排名：')
    for i in ls:
        print(i[1],i[2])
def rank_item():
    ls = [[i.iid,i.name,0] for i in items]
    for i in sells:
        for j in ls:
            if j[0] == i.iid:
                j[2] += float(i.num)*float(i.price)
                break
    ls.sort(key=lambda x:x[2],reverse=True)
    print('销售额排名：')
    for i in ls:
        print(i[1],i[2])
def load():
    with open('people.csv','r') as f:
        fcsv = csv.reader(f)
        for i in fcsv:
            if i:
                peoples.append(People(i[0],i[1],i[2],i[3],i[4]))
    with open('item.csv','r') as f:
        fcsv = csv.reader(f)
        for i in fcsv:
            if i:
                items.append(Item(i[0],i[1],i[2],i[3]))
    with open('sell.csv','r') as f:
        fcsv = csv.reader(f)
        for i in fcsv:
            if i:
                sells.append(Sell(i[0],i[1],i[2],i[3],i[4],i[5]))
def save():
    with open('people.csv','w',newline='') as f:
        fcsv = csv.writer(f)
        for i in peoples:
            fcsv.writerow([i.pid,i.name,i.department,i.level,i.state])
    with open('item.csv','w',newline='') as f:
        fcsv = csv.writer(f)
        for i in items:
            fcsv.writerow([i.iid,i.name,i.price,i.num])
    with open('sell.csv','w',newline='') as f:
        fcsv = csv.writer(f)
        for i in sells:
            fcsv.writerow([i.sid,i.date,i.pid,i.iid,i.price,i.num])
def main_people():
    info = """

        1.添加业务员信息
        2.删除业务员信息
        3.修改业务员信息
        4.查询业务员信息
        5.显示所有业务员信息
        6.业务员销售排序
        7.返回

        """
    while True:
        print(info)
        c = input('请输入选项：')
        if c == '1':
            add_people()
        elif c == '2':
            dele_people()
        elif c == '3':
            change_people()
        elif c == '4':
            search_people()
        elif c == '5':
            show_people()
        elif c == '6':
            rank_people()
        elif c == '7':
            return 0
        else:
            print('非法输入！')
def main_item():
    info = """

        1.添加产品信息
        2.删除产品信息
        3.修改产品信息
        4.修改产品库存
        5.查询产品信息
        6.显示所有产品信息
        7.产品销售排序
        8.返回

        """
    while True:
        print(info)
        c = input('请输入选项：')
        if c == '1':
            add_item()
        elif c == '2':
            dele_item()
        elif c == '3':
            change_item()
        elif c == '4':
            change_item_num()
        elif c == '5':
            search_item()
        elif c == '6':
            show_item()
        elif c == '7':
            rank_item()
        elif c == '8':
            return 0
        else:
            print('非法输入！')
def main_sell():
    info = """

        1.添加销售信息
        2.删除销售信息
        3.修改销售信息
        4.组合查询产品信息
        5.返回

        """
    while True:
        print(info)
        c = input('请输入选项：')
        if c == '1':
            add_sell()
        elif c == '2':
            dele_sell()
        elif c == '3':
            change_sell()
        elif c == '4':
            search_sell()
        elif c == '5':
            return 0
        else:
            print('非法输入！')
if __name__ == '__main__':
    load()
    info = """
    
    1.业务员信息管理
    2.产品信息管理
    3.订单信息管理
    4.退出系统
    
    """
    while True:
        print(info)
        c = input('请输入选项：')
        if c == '1':
            main_people()
        elif c == '2':
            main_item()
        elif c == '3':
            main_sell()
        elif c == '4':
            save()
            break
        else:
            print('非法输入！')

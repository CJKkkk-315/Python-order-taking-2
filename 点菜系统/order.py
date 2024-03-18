
def readfile():  # 将文件的内容读出置于对象列表FoodList中
    """由于main调用了读文件的方法,order再次调用报错:NameError: name 'file' is not defined,
    所以重新定义一个读文件的方法"""
    FoodList = []
    Fooddic = {}    # 定义一个空字典 用来储存key为菜品,value为价格的键值对
    try:
        with open('food_list.txt', 'r',encoding='utf-8',errors='ignore') as file:
            for line in file.readlines():
                if line != "":
                    food = line.rstrip('\n').split(',')
                    foodname, describe, price = food[0], food[1], food[2]
                    oneFood = (foodname, describe, price)
                    # print(oneFood)        # 调试时：用于输出结果分析用
                    FoodList.append(oneFood)
                    key = food[1]
                    value = food[3]
                    Fooddic.setdefault(key, value)

            # print(FoodList)       # 调试时用于分析最终Foodlist结果用
            # print(Fooddic)      # 调试时用于分析最终Fooddic结果用
            return FoodList, Fooddic  # 返回记录条数

    except FileNotFoundError:
        print("数据文件不存在！")  # 若打开失败，输入提示信息
        return 0  # 因为数据文件不存在，返回0，表示无菜品数据


def show_order():
    """为了方便用户操作,定义一个展示订单列表的方法,方便每次操作的时候看"""
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
            print(text)
            for i in OrderList:
                text2 = ("                 %-16s%-16s%-16s" % (i[0], i[1], i[2]))
                print(text2)
    except FileNotFoundError:
        print("数据文件不存在！")  # 若打开失败，输入提示信息


def change_order():
    """定义一个修改订单的方法"""
    return_dic = readfile()[1]  # 调用读取food_list.txt的方法,1元素位位返回的字典,即获取菜品价格
    show_order()        # 先展示未支付的订单
    change_name = input("请输入您要修改的订单菜名:")
    change_num = input("请输入您要修改的菜品份数:")
    food_price = return_dic[change_name]
    all_price = int(change_num) * int(food_price)
    if all_price > 30:
        all_price = all_price - 5
        print("符合优惠活动,给您减5元!")
    else:
        print("不符合优惠活动,您要不再订点?")
    with open('uncommitted_order.txt', 'r') as r_w:
        lines1 = r_w.readlines()        # 获取行数
        with open('uncommitted_order.txt', 'w') as rr_w:
            for line1 in lines1:
                if change_name in line1:
                    rr_w.write(change_name + ',' + change_num + ',' + str(all_price) + '\n')
                    continue
                rr_w.write(line1)
    submit = input("您订了 %s 份-%s-,总价为: %d元,请选择对订单的操作(1.提交订单 2.不提交订单)" % (change_num, change_name, all_price))
    # 定义一个是否修改完提交订单的功能
    if submit == '1':
        with open('submit_order.txt', 'a+') as submit:
            submit.write(change_name + ',' + change_num + ',' + str(all_price) + '\n')
            print(">>>>提交订单成功!>>>>")
    else:
        pass


def del_order():
    """定义一个删除订单的方法"""
    show_order()  # 先展示未支付的订单
    del_name = input("请输入您要删除的订单菜名:")
    with open('uncommitted_order.txt', 'r') as f:
        lines = f.readlines()
        with open('uncommitted_order.txt', 'w') as f_w:
            for line in lines:
                if del_name in line:
                    continue
                f_w.write(line)


def query_old():
    """查询历史订单"""
    OdlList = []
    try:
        with open('submit_order.txt', 'r') as file:
            for line in file.readlines():
                if line != "":
                    food = line.rstrip('\n').split(',')
                    foodname, describe, price = food[0], food[1], food[2]
                    oneFood = (foodname, describe, price)
                    OdlList.append(oneFood)
            text = ("                 %-16s%-16s%-16s" % ("订单名", "菜品份数", "总价格"))
            print(text)
            for i in OdlList:
                text2 = ("                 %-16s%-16s%-16s" % (i[0], i[1], i[2]))
                print(text2)
    except FileNotFoundError:
        print("数据文件不存在！")  # 若打开失败，输入提示信息


def del_old():
    """删除历史订单的方法"""
    query_old()     # 先展示历史订单
    del_name = input("请输入您要删除的订单菜名:")
    with open('submit_order.txt', 'r') as f:
        lines = f.readlines()
        with open('submit_order.txt', 'w') as f_w:
            for line in lines:
                if del_name in line:
                    continue
                f_w.write(line)

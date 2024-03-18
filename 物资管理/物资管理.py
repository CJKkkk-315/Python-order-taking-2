# imports

# data
ITEM_INFO = {
    # item_name: {"unit": unit, "price": price}
    "大米": {"price": 3},
}

ITEM_STOCK = {
    # item_name: item_number
    "大米": 1000,
}
USER_INFO = {
    1:{"name":"jay","address":"house1"},
}
INBOUND_RECORDS = [

    {"item": "大米", "number": 400, "uid": 1, "record_date": "2022-01-04", "status": "未满足"},
]

# 加入物品信息
def input_item_info(name, price):
    ITEM_INFO[name] = {"price":price}
    print("input item info DONE")
# 加入用户记录
def input_user_record(uid,name,address):
    USER_INFO[uid] = {"name":name,"address":address}
    print("input user info DONE")
# 加入物资需求记录
def input_inbound_record(record_date, uid, item, number, status):
    INBOUND_RECORDS.append({"item":item,"uid":uid,"number":number,"status":status,"record_date":record_date})
    if item in ITEM_STOCK:
        ITEM_STOCK[item] += number
    else:
        ITEM_STOCK[item] = number
    print("input inbound record DONE")
# 改变一条物资需求状态
def chang_status(uid,item):
    for i in INBOUND_RECORDS:
        if i['item'] == item and i['uid'] == uid:
            i['status'] = "已满足"
            ITEM_STOCK[item] -= i['number']
    print("change status DONE")
# 打印所有物资需求信息
def print_item_need():
    for i in sorted(INBOUND_RECORDS,key=lambda x:x['item']):
        print(i['item'],i['number'],i['status'])
# 打印所有用户需求信息
def print_user_need():
    for i in INBOUND_RECORDS:
        print(USER_INFO[i['uid']]['name'],i['item'],i['number'],i['status'])
# 菜单主循环
def run_in_loop():
    do_exit = False
    info = """
    commands
    A: 录入物资种类信息
    B: 录入居民信息
    C: 记录物资需求
    D: 更改物资需求状态
    E: 输出物资需求
    F: 输出居民需求
    G: 退出
    """
    while not do_exit:
        print(info)
        command_str = input("请输入你的命令: ")
        if command_str not in ["A", "B", "C", "D", "E", "F"]:
            print("系统支持命令{}，请重新输入".format(command_str))
            continue
        if command_str == "G":
            do_exit = True
        elif command_str == "A":
            input_str = input("请输入物品信息(名称,价格):")
            name, price= input_str.split(",")
            price = float(price)
            input_item_info(name,price)
        elif command_str == "B":
            input_str = input("请输入用户信息(ID,姓名,住址):")
            uid,name,address = input_str.split(",")
            uid = float(uid)
            input_user_record(uid,name,address)
        elif command_str == "C":
            input_str = input("请输入记录信息(ID,物资名,数量,时间):")
            uid, item, number, date = input_str.split(",")
            uid = int(uid)
            number = int(number)
            input_inbound_record(date, uid, item, number, "未满足")
        elif command_str == "D":
            input_str = input("请输入记录信息(ID,物资名):")
            uid, item = input_str.split(",")
            uid = int(uid)
            chang_status(uid,item)
        elif command_str == "E":
            print_item_need()
        elif command_str == "F":
            print_user_need()


# entry point
def main():
    run_in_loop()


if __name__ == "__main__":
    main()
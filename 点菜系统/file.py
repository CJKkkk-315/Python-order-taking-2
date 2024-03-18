from order import *


def readFile():  # 将文件的内容读出置于对象列表FoodList中
    """由于后续需要对订单价格进行计算, 使用列表打印菜单是十分方便的,但是要用列表去查找一个菜品在获取它的价格是不容易的
    所以想到使用字典的键值对去方便查询菜品的价格再计算订单总价格"""
    FoodList = []
    Fooddic = {}    # 定义一个空字典 用来储存key为菜品,value为价格的键值对
    try:
        with open('food_list.txt', 'r',encoding='utf-8',errors='ignore') as file:
            for line in file.readlines():
                if line != "":
                    food = line.rstrip('\n').split(',')
                    foodid, foodname, describe, price = food[0], food[1], food[2], food[3]
                    oneFood = (foodid, foodname, describe, price)
                    # print(oneFood)        # 调试时：用于输出结果分析用
                    FoodList.append(oneFood)
                    key = food[0]
                    value = food[1], food[3]
                    Fooddic.setdefault(key, value)

            # print(FoodList)       # 调试时用于分析最终Foodlist结果用
            # print(Fooddic)      # 调试时用于分析最终Fooddic结果用
            return FoodList, Fooddic  # 返回记录条数

    except FileNotFoundError:
        print("数据文件不存在！")  # 若打开失败，输入提示信息
        return FoodList, Fooddic  # 因为数据文件不存在，返回空的列表和字典

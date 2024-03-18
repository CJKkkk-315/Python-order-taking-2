from file import *
from order import *





def show_food():
    """为了方便用户操作,定义一个展示菜品列表的方法,方便每次操作的时候看"""
    return_list = readFile()[0]  # 调用读取food_list.txt的方法,0元素位位返回的列表
    if return_list == 0:
        print("没有找到food_list.txt文件！")
    else:
        text = ("                 %-16s%-16s%-16s%-16s" % ("菜品ID", "菜品名称", "菜品描述", "菜品价格"))
        print(text)
        for i in return_list:
            text2 = ("                 %-16s%-16s%-16s%-16s" % (i[0], i[1], i[2], i[3]))
            print(text2)


def menu_main():
    print('-' * 30)
    print("   今日优惠活动:订餐满30减5元!")
    print('-' * 30)
    print('1.下单')
    print('2.查询历史订单')
    print('3.删除历史订单')
    print('0.退出        ')
    print('-' * 30)


def menu_order():
    """下单菜单列表的展示"""
    print('-' * 30)
    print('1.查询食堂菜单')
    print('2.添加新订单')
    print('3.修改未支付订单')
    print('4.删除未支付订单')
    print('0.返回上级菜单')
    print('-' * 30)


def place_order():
    """定义一个下单的方法"""
    menu_order()
    while True:
        place1 = input("请输入您的选择(0-4)：")
        if place1 == '1':
            """查询菜单"""
            return_list = readFile()[0]     # 调用读取food_list.txt的方法,0元素位位返回的列表
            if len(return_list) == 0:
                print("没有找到food_list.txt文件！")
            else:
                text = ("                 %-16s%-16s%-16s%-16s" % ("菜品ID", "菜品名称", "菜品描述", "菜品价格"))
                print(text)
                for i in return_list:
                    text2 = ("                 %-16s%-16s%-16s%-16s" % (i[0], i[1], i[2], i[3]))
                    print(text2)
            menu_order()
        elif place1 == '2':
            """添加订单"""
            show_food()
            while True:
                return_dic = readFile()[1]      # 调用读取food_list.txt的方法,1元素位位返回的字典
                food_id = input("请输入您要订的菜品ID：")
                food_num = input("请输入您要订的菜品份数：")
                food_tuple = return_dic[food_id]
                food_name = food_tuple[0]
                food_price = food_tuple[1]

                all_price = int(food_num) * int(food_price)
                # all_price = food_num * food_price       # 定义此次订单的总价格计算公式,
                # 调试时发现报错:TypeError: can't multiply sequence by non-int of type 'str',所以把str转化为了int
                # 判断是否符合优惠条件
                if all_price > 30:
                    all_price = all_price - 5
                    print("符合优惠活动,给您减5元!")
                else:
                    print("不符合优惠活动,您要不再订点?")

                # print(all_price)
                # 把订单结果写入订单库内
                print('-' * 30)
                print('1.保存订单（未支付）')
                print('2.提交订单（支付）')
                print('-' * 30)
                select = input("您订了 %s 份-%s-,总价为: %d元,请选择对订单的操作(1-2):" % (food_num, food_name, all_price))

                if select == '1':
                    """执行保存到未支付订单库操作"""
                    with open('uncommitted_order.txt', 'a+') as unor:
                        # 调试时报错:TypeError: can only concatenate str (not "int") to str
                        # unor.write(food_name+','+food_num+','+all_price+'\n')
                        # 则将all_price转化为str
                        unor.write(food_name + ',' + food_num + ',' + str(all_price) + '\n')
                        print(">>>>保存订单成功!>>>>")
                menu_order()

                if select == '2':
                    """如果选择提交订单,保存到submit_order.txt中去"""
                    with open('submit_order.txt', 'a+') as submit:
                        submit.write(food_name + ',' + food_num + ',' + str(all_price) + '\n')
                        print(">>>>提交订单成功!>>>>")
                menu_order()
                again = input("您是否需要继续点餐？(1.继续 2.结束点餐):")
                if again == '1':
                    return_dic = readFile()[1]      # 调用读取food_list.txt的方法,1元素位位返回的字典
                    food_id2= input("请输入您要订的菜品ID：")
                    food_num2= input("请输入您要订的菜品份数：")
                    food_tuple2= return_dic[food_id2]
                    food_name2= food_tuple2[0]
                    food_price2 = food_tuple2[1]
                    all_price2 = int(food_num2) * int(food_price2)
                    sum_price = all_price+all_price2
                    food_numsum=eval(food_num)+eval(food_num2)
                    if sum_price > 30:
                        sum_price = sum_price - 5
                        print("符合优惠活动,给您减5元!")
                        print('-' * 30)
                    else:
                        print("没有点到30元，不能参加优惠活动！")
                    print("您订了 %s 份-%s-和 %s 份-%s-,总价为: %d元" % (food_num, food_name,food_num2,food_name2,sum_price))
                    with open('submit_order.txt', 'a+') as submit:
                        submit.write(food_name + food_name2 + ',' +str(food_numsum) + ',' + str(sum_price) + '\n')
                        #调试时报错: TypeError: can only concatenate str(not "int") to str，故将food_numsum改为str(food_numsum)
                        print(">>>>提交订单成功!>>>>")
                        print("点餐结束！")
                        menu_order()
                        break
               

                    
                elif again == '2':
                    print("点餐结束！")
                    break
                else:
                    print("输入有误,点餐结束!")
                    break

        elif place1 == '3':
            """修改未支付订单"""
            change_order()
            print(">>>>修改操作执行成功!>>>>")
            menu_order()

        elif place1 == '4':
            """删除未支付订单"""
            del_order()
            print(">>>>删除操作执行成功!>>>>")
            menu_order()
        elif place1 == '0':
            print(">>>>正在退出!!!>>>>")
            break
        else:
            print(">>>>输入功能序号有误!!!>>>>")
            menu_order()




if __name__ == "__main__":
    menu_main()     # 展示主菜单
    while True:
        select = input("请输入您的选择(0-3):")
        if select == '1':
            place_order()
            menu_main()
        elif select == '2':
            query_old()
            menu_main()
        elif select == '3':
            del_old()
            print(">>>>删除历史订单成功!>>>>")
            menu_main()
        elif select == '0':
            print(">>>>正在退出订餐管理系统>>>>")
            break
        else:
            print("请输入正确功能序号!!")
            menu_main()

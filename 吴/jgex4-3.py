temps=input('请输入带符号的温度值:')
while temps[-1] not in ['N','n']:
    if temps[-1] in ['F','f']:
        c = (eval(temps[0:-1]) - 32)/1.8
        print('转换后的温度为')
temps=input("请输入带符号的温度值:")
while temps[-1] not in ["N","n"]:
    if temps[-1] in ['F','f']:
        c=(eval(temps[0:-1]) - 32)/1.8
        print("转换后的温度为:.2f}C".format(c))
    elif temps[-1] in ['C','c']:
        f=1.8*eval(temps[0:-1])+32
        print("转换后的温度为{:.2fF".format(f))
    else:
        print("输入格式错误!")
    temps=input("请输入带符号的温度值:")
print("结束程序")

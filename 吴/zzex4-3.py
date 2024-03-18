mouth = int(input('请输入月份：'))
if mouth == 1 or mouth == 2:
    print('一共有一只兔子')
else:
    a = 1
    b = 1
    c = 0
    for i in range(3,mouth+1):
        c = a + b
        a = b
        b = c
    print(c)
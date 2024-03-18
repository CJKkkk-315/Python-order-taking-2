import random

def generate_redpocket(money, n):
    '''对于给定的money和n，生成n个红包，每个红包至少1分钱。
    其中n为不小于1的正整数；money不少于n(以分为单位)
    '''
    assert type(n) == int and n>=1, '红包的个数不少于1'
    assert money >= n, '红包金额应不少于红包的个数'
    # todo:在下面补写代码
    pockets = []
    old_money = money
    for i in range(n-1):
        pockets.append(random.randint(1,money-(n-i-1)))
        money -= pockets[-1]
    pockets.append(old_money-sum(pockets))
    return pockets

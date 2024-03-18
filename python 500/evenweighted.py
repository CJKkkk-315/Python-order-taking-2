'''把序列
编写一个函数，该函数接受一个序列对象lst并返回一个新列表，该列表仅保留lst的偶数索引元素并将
它们乘以相应的索引，且索引值从0开始。
序列对象包括列表、元组和range对象；序列对象中的每个元素只能是bool、int、float和complex。
'''


def evenweighted(lst):
    # todo 1 编写assert代码
    assert (isinstance(lst,range) or isinstance(lst,tuple) or isinstance(lst,list)),'参数lst不是序列'
    for i in lst:
        assert isinstance(i,int) or isinstance(i,float) or isinstance(i,complex) or isinstance(i,bool),'参数lst包含非数值元素'
    # todo 2 编写函数功能代码
    lstt = []
    for i in range(len(lst)):
        if i % 2 == 0:
            lstt.append(lst[i]*i)
    if isinstance(lstt,range):
        lst = range(lstt)
    elif isinstance(lstt,tuple):
        lst = tuple(lstt)
    else:
        lst = lstt
    return lst

'''
>>> from evenweighted import evenweighted
>>> evenweighted('hello') 
Traceback (most recent call last):   
...
AssertionError: 参数lst不是序列
>>> evenweighted(['a',10,'b',10]) 
Traceback (most recent call last):
...
AssertionError: 参数lst包含非数值元素
>>> evenweighted([1,2,3,4])
[0, 6]
>>> evenweighted((1,2,3,4,5,6))
[0, 6, 20]
>>> evenweighted(range(10))
[0, 4, 16, 36, 64]
>>> evenweighted([1j, 10, 3j, 4+5j, 99, 10]) 
[0j, 6j, 396]
>>> evenweighted([False, 1.0, True, 1.5, 6.7])   
[0, 2, 26.8]
'''
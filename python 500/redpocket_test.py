'''
>>> from redpocket import generate_redpocket
>>> generate_redpocket(100,0)
Traceback (most recent call last):
...
AssertionError: 红包的个数不少于1
>>> generate_redpocket(100,1)
[100]
>>> generate_redpocket(5,6)
Traceback (most recent call last):
...
AssertionError: 红包金额应不少于红包的个数
>>> pockets = generate_redpocket(10,3)
>>> all(pockets) and len(pockets)==3 and sum(pockets)==10
True
>>> pockets = generate_redpocket(20,6)
>>> all(pockets) and len(pockets)==6 and sum(pockets)==20
True
'''
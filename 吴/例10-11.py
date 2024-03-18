x = int(input())
xmax = x
while x!=0:
    if x > xmax:
         xmax = x
    x = int(input())
print('最高分是：',xmax)
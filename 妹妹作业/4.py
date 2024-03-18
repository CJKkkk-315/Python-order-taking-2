import random
num = []
for i in range(20):
    num.append(random.randint(1000000000,9999999999))
print(num)
num=[c for c in num if c%2==0]
num.append(2010411104)
for i in range(len(num)):
   for j in range(len(num)-i-1):
    if num[j]>num[j+1]:
        num[j],num[j+1]=num[j+1],num[j]
else:
    print(num)



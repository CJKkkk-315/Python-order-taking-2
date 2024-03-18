import csv
import matplotlib.pyplot as plt
data = []
with open('排序.csv','r',encoding='gbk') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        data.append(i)
data = data[::-1]
x = [i[0] for i in data[:20]]
y = [float(i[1]) for i in data[:20]]
plt.rcParams['font.sans-serif']=['SimHei']
print(x)
print(y)
plt.pie(x=y,labels=x)
plt.show()

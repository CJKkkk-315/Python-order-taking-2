import csv
import matplotlib.pyplot as plt
data = []
with open('排序.csv','r',encoding='gbk') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        data.append(i)
x = [i[0] for i in data[:10]]
y = [float(i[1]) for i in data[:10]]
plt.rcParams['font.sans-serif']=['SimHei']
plt.bar(x,y)
plt.show()

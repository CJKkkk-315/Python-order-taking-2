import matplotlib.pyplot as plt
import csv
x = []
y = []

with open('13-1.csv') as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        x.append(row[0])
        y.append(row[1])
plt.xticks([]) # 不显示x轴
plt.yticks([]) # 不显示y轴
plt.plot(x,y)
plt.show()
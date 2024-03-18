import csv
import matplotlib.pyplot as plt
from collections import Counter
# 读取文件，存入data列表中
with open('Spotify.csv','r') as f:
    # 去掉表头
    data = [i for i in csv.reader(f)][1:]
# 提取每一行的artist信息
data1 = [i[1] for i in data]
# 统计所有artist出现次数
data1 = Counter(data1)
# 转为列表排序，并按照出现次数降序，提取TOP10
data1 = sorted(data1.items(),key=lambda x:x[1],reverse=True)[:10]
# 将artist和对应出现次数分别设置为xy轴
x = [i[0] for i in data1]
y = [i[1] for i in data1]
# 画出出现次数最多的artistTOP10柱状图
plt.bar(x,y)
plt.show()
# 提取每一行的artist type信息
data1 = [i[-1] for i in data]
# 统计所有artist type出现次数
data1 = Counter(data1)
# 将字典键值对转换为二元组列表
data1 = list(data1.items())
# 将artist type和对应出现次数分别设置为xy轴
x = [i[0] for i in data1]
y = [i[1] for i in data1]
# 画出artist type占比饼图
plt.pie(labels=x,x=y)
plt.show()
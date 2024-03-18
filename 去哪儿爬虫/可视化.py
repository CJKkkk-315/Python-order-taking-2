import matplotlib.pyplot as plt
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
import csv
data = []
# 读取csv文件，写入data列表中
with open('res.csv','r',encoding='utf-8') as f:
    fcsv = csv.reader(f)
    for i in fcsv:
        data.append(i)
# 对data列表按照销量排序
data1 = sorted(data,key=lambda x:int(x[5]),reverse=True)
# 提取前15的景点名和销量
x = [i[0] for i in data1][:15]
y = [int(i[5]) for i in data1][:15]
# 柱状图
plt.bar(x,y)
plt.xticks(rotation=30)
plt.title('景点销量排行')
plt.xlabel('景点名')
plt.ylabel('销量')
plt.show()

# 按照销售额排序
data1 = sorted(data,key=lambda x:int(x[5])*float(x[4]),reverse=True)
# 提取前15的景点名和销售额
x = [i[0] for i in data1][:15]
y = [int(i[5])*float(i[4]) for i in data1][:15]
# 柱状图
plt.bar(x,y)
plt.xticks(rotation=30)
plt.title('景点销售额排行')
plt.xlabel('景点名')
plt.ylabel('销售额')
plt.show()

# 定义字典
d = {}
for i in data:
    # 尝试提取景点地址中的城市数据
    try:
        # 在词典中统计每个城市的出现次数
        t = i[1].index('市')
        if i[1][t-2:t+1] in d:
            d[i[1][t-2:t+1]] += 1
        else:
            d[i[1][t-2:t+1]] = 1
    except:
        continue
# 按照出现次数排序
d = sorted(d.items(),key=lambda x:x[1],reverse=True)
# 提取前15的城市名和景点个数
x = [i[0] for i in d][:15]
y = [i[1] for i in d][:15]
# 柱状图
plt.bar(x,y)
plt.title('城市景点数量排行')
plt.xlabel('城市')
plt.ylabel('景点数量')
plt.show()

# 同上 定义字典，提取城市
d = {}
for i in data:
    try:
        t = i[1].index('市')
        # 将每个景点热度按照城市聚类
        if i[1][t-2:t+1] in d:
            d[i[1][t-2:t+1]] += float(i[3])
        else:
            d[i[1][t-2:t+1]] = float(i[3])
    except:
        continue
# 按照热度排序
d = sorted(d.items(),key=lambda x:x[1],reverse=True)
# 提取前15的城市名和总热度
x = [i[0] for i in d][:15]
y = [i[1] for i in d][:15]
# 柱状图
plt.bar(x,y)
plt.title('城市热度排行')
plt.xlabel('城市名')
plt.ylabel('热度')
plt.show()

# 对所有数据按照热度高，营业额低的算法进行排序
data1 = sorted(data,key=lambda x:float(x[3])/(float(x[4])*float(x[5]))*1000,reverse=True)
# 同样提取前15名
x = [i[0] for i in data1][:15]
y = [float(i[3])/(float(i[4])*float(i[5]))*1000 for i in data1][:15]
# 柱状图
plt.bar(x,y)
plt.xticks(rotation=30)
plt.title('景点推荐')
plt.xlabel('景点名')
plt.ylabel('推荐值')
plt.show()
# 引入pandas数据分析包和plt画图包
import pandas as pd
import matplotlib.pyplot as plt
# 读取爬取好的数据存入df中
df = pd.read_csv('data.csv')
# 将需要的各个列转为列表方便后续处理
price = df['totalprice'].values.tolist()
house = df['houseinfo'].values.tolist()
follow = df['followinfo'].values.tolist()
uprice = []
# 对房屋信息列处理，提取出面积信息
house = list(map(lambda x:float(x.split(' | ')[1].replace('平米','')),house))
# 对粉丝信息列处理，提取出关注度人数信息
follow = list(map(lambda x:int(x.split(' / ')[0].replace('人关注','')),follow))
# 将每一个总价除以面积获得单价信息
for i,j in zip(house,price):
    uprice.append(j/i)
# 绘制总价与关注度的散点图
plt.scatter(follow,price)
plt.xlabel('fans')
plt.ylabel('total price')
plt.show()
# 绘制单价与关注度的散点图
plt.scatter(follow,uprice)
plt.xlabel('fans')
plt.ylabel('unit price')
plt.show()
print('关注度最高为：',max(follow))
print('其单价为：',uprice[follow.index(max(follow))])
print('其总价为：',price[follow.index(max(follow))])
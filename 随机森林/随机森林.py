import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
# 读入csv文件
df = pd.read_csv('BeijingPM.csv')
# 删除掉大部分为NA 或者0 即对训练没有意义的列
df = df.drop(['No','PM_Dongsi','PM_Dongsihuan','PM_Nongzhanguan','cbwd','precipitation','Iprec'],axis=1)
# 清洗数据，去掉有空值的行
df = df.dropna()
# 将非2015年的数据划分为训练集
train = df.loc[(df.year != 2015)]
# 获取X训练集
trainx = train.drop(['PM_US Post'],axis=1)
# 将X训练集去除掉年份数据
trainx = trainx.drop(['year'],axis=1)
# 获取Y训练集
trainy = pd.DataFrame(train['PM_US Post'])
# 将2015年提取出来作为测试集
test = df.loc[(df.year == 2015)]
# 获取X测试集
testX = test.drop(['PM_US Post'],axis=1)
testX = testX.drop(['year'],axis=1)
# 获取Y测试集
testY = pd.DataFrame(test['PM_US Post'])
# 构建随机森林模型
RFC = RandomForestRegressor()
# 利用划分好的训练集训练拟合模型
RFC.fit(trainx,trainy)
# 用X测试集进行预测，获得Y预测集
predictY = RFC.predict(testX)
# 将Y预测集和Y测试集传入R方函数，计算模型评分
print(r2_score(testY,predictY))
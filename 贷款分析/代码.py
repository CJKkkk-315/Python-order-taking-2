import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from imblearn.metrics import geometric_mean_score
from sklearn.model_selection import train_test_split
from sklearn import metrics
# 读取数据集
df = pd.read_csv('附件1：贷款违约数据集.csv')
# 清楚无相关性变量
df = df.drop('issueDate',axis=1)
# 清洗数据，去掉有空值的行
df = df.dropna()
# 将类型转为列表
data = df.values.tolist()
x = []
y = []
# 将label和变量各自提取出来
for i in data:
    y.append(i[1])
    x.append(i[2:])
y = pd.DataFrame(y)
# 对变量做处理，将等级ABCD转为1234，同时提取年份中的int型年份
for i in range(len(x)):
    x[i][4] = ord(x[i][4])-64
    x[i][5] = int(x[i][5][-1])
    num = ''
    for j in x[i][7]:
        if j.isdigit():
            num += j
    x[i][7] = int(num)
x = pd.DataFrame(x)
# 将数据分隔成训练集和测试集 8比2分割
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
# 利用MLP模型 拟合训练集训练
MLP = DecisionTreeClassifier()
MLP.fit(x_train,y_train)
# 用测试集做出测试，得出预测值
y_pred = MLP.predict(x_test)
# 通过预测值和真实值评估测试集
print('Accuracy:', metrics.accuracy_score(y_test, y_pred))
print('G-mean:', geometric_mean_score(y_test, y_pred))

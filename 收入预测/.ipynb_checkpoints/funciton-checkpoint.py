import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import sklearn.preprocessing as sp
import numpy as np
df = pd.read_csv('Train.csv')
print(df)
df.drop_duplicates(keep='first', ignore_index=False, inplace=True)
print(df.isnull().any())
cols = df.columns
print(cols)
labels = df['Y'].tolist()
plt.rcParams['font.sans-serif'] = ['SimHei']
for col in list(cols):
    d = defaultdict(list)
    data = df[col].tolist()
    for i,j in zip(data,labels):
        d[i].append(j)
    xy = sorted([[i,sum(j)/len(j)] for i,j in d.items()])
    x = [i[0] for i in xy]
    y = [i[1] for i in xy]
    if df[col].dtype != 'int64':
        plt.bar(x,y)
    else:
        plt.plot(x,y)
    plt.title(col)
    # plt.show()
spl = sp.LabelEncoder()
for col in list(df.columns):
    if df[col].dtype != 'int64':
        df[col] = spl.fit_transform(df[col])
# print(df)
x_train = df.drop(['Y'], axis=1)
y_train = df['Y']
DTC = RandomForestClassifier()
DTC.fit(x_train,y_train)
x_test = pd.read_csv('Test.csv')
for col in list(x_test.columns):
    if x_test[col].dtype != 'int64':
        x_test[col] = spl.fit_transform(x_test[col])
predictY = DTC.predict(x_test)
print('随机森林结果完成')
predictY = pd.DataFrame(predictY) # 产生随机数
predictY.to_csv('Results_1.csv', encoding = 'utf-8', index=False , header=False)



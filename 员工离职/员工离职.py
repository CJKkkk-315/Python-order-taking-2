import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import sklearn.preprocessing as sp
from sklearn import metrics
df = pd.read_csv('train.csv')
# print(df)
df.drop_duplicates(keep='first', ignore_index=False, inplace=True)
# print(df.isnull().any())
cols = df.columns
labels = df['Label'].tolist()
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
#     plt.show()
drop_list = 'ID DistanceFromHome EmployeeNumber Gender NumCompaniesWorked Over18 StandardHours YearsInCurrentRole YearsSinceLastPromotion'.split()
df = df.drop(drop_list, axis=1)
# print(df)
spl = sp.LabelEncoder()
for col in list(df.columns):
    if df[col].dtype != 'int64':
        df[col] = spl.fit_transform(df[col])
# print(df)
x = df.drop(['Label'], axis=1)
y = df['Label']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
DTC = RandomForestClassifier()
DTC.fit(x_train,y_train)
y_pred = DTC.predict(x_test)
print('随机森林结果:')
print('Accuracy:', metrics.accuracy_score(y_test, y_pred))
print('F1:', metrics.f1_score(y_test, y_pred))
df = pd.read_csv('test_noLabel.csv')
drop_list = 'ID DistanceFromHome EmployeeNumber Gender NumCompaniesWorked Over18 StandardHours YearsInCurrentRole YearsSinceLastPromotion'.split()
df = df.drop(drop_list, axis=1)
spl = sp.LabelEncoder()
for col in list(df.columns):
    if df[col].dtype != 'int64':
        df[col] = spl.fit_transform(df[col])
y_pred = DTC.predict(df)
head = ['ID','Label']
import csv
with open('res.csv','w',newline='') as f:
    fcsv = csv.writer(f)
    fcsv.writerow(head)
    for i in range(len(y_pred)):
        fcsv.writerow([str(1100+i),str(y_pred[i])])
DTC = LogisticRegression(solver='saga')
DTC.fit(x_train,y_train)
y_pred = DTC.predict(x_test)
print('逻辑回归结果:')
print('Accuracy:', metrics.accuracy_score(y_test, y_pred))
print('F1:', metrics.f1_score(y_test, y_pred))


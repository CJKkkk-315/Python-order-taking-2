from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import datetime

email_file_name = 'all_email.txt'
label_file_name = 'label.txt'
vectoring = TfidfVectorizer(input='content', tokenizer=lambda line: [li for li in line.split() if li],analyzer='word')
content = open(email_file_name, 'r', encoding='utf8').readlines()
x = vectoring.fit_transform(content)
y = open(label_file_name, 'r', encoding='utf8').readlines()
y = np.array(y)

# 随机打乱所有样本
index = np.arange(len(y))
np.random.shuffle(index)
x = x[index]
y = y[index]

# 划分训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

startTime = datetime.datetime.now()
bayes = MultinomialNB()
bayes.fit(x_train, y_train)
y_pred = bayes.predict(x_test)
print('朴素贝叶斯准确度:', metrics.accuracy_score(y_test, y_pred))
print('朴素贝叶斯召回率:', metrics.recall_score(y_test, y_pred,pos_label='1\n'))
endTime = datetime.datetime.now()
durTime = 'funtion time use:%dms' % ((endTime -startTime ).seconds * 1000 + (endTime -startTime ).microseconds / 1000)
print('朴素贝叶斯用时:', durTime)

startTime = datetime.datetime.now()
LR = LogisticRegression()
LR.fit(x_train, y_train)
y_pred = LR.predict(x_test)
print('线性回归准确度:', metrics.accuracy_score(y_test, y_pred))
print('线性回归召回率:', metrics.recall_score(y_test, y_pred,pos_label='1\n'))
endTime = datetime.datetime.now()
durTime = 'funtion time use:%dms' % ((endTime -startTime ).seconds * 1000 + (endTime -startTime ).microseconds / 1000)
print('线性回归用时:', durTime)


startTime = datetime.datetime.now()
RF = RandomForestClassifier()
RF.fit(x_train, y_train)
y_pred = RF.predict(x_test)
print('随机森林准确度:', metrics.accuracy_score(y_test, y_pred))
print('随机森林召回率:', metrics.recall_score(y_test, y_pred,pos_label='1\n'))
endTime = datetime.datetime.now()
durTime = 'funtion time use:%dms' % ((endTime -startTime ).seconds * 1000 + (endTime -startTime ).microseconds / 1000)
print('随机森林用时:', durTime)


startTime = datetime.datetime.now()
DT = DecisionTreeClassifier()
DT.fit(x_train, y_train)
y_pred = DT.predict(x_test)
print('决策树准确度:', metrics.accuracy_score(y_test, y_pred))
print('决策树召回率:', metrics.recall_score(y_test, y_pred,pos_label='1\n'))
endTime = datetime.datetime.now()
durTime = 'funtion time use:%dms' % ((endTime -startTime ).seconds * 1000 + (endTime -startTime ).microseconds / 1000)
print('决策树用时:', durTime)
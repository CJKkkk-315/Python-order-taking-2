import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib as mpl
from sklearn.ensemble import BaggingRegressor
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
data = pd.read_excel('完整版.xlsx')
data['time'] = data.time.apply(lambda x:x.replace('min',''))
model = LinearRegression()
y = data.S
x = data.drop('S',axis=1)
x_train = x[:157]
x_test = x[157:187]
y_train = y[:157]
y_test = y[157:187]
model = LinearRegression()
model.fit(x_train,y_train)
y1 = model.predict(x_test)
print(metrics.mean_squared_error(y_test, y1))
model = DecisionTreeRegressor()
model.fit(x_train,y_train)
y2 = model.predict(x_test)
print(metrics.mean_squared_error(y_test, y2))
model = BaggingRegressor()
model.fit(x_train,y_train)
y3 = model.predict(x_test)
print(metrics.mean_squared_error(y_test, y3))
mpl.rcParams['font.sans-serif'] = [u'simHei']
mpl.rcParams['axes.unicode_minus'] = False
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(12,10))
print(y1)
print(y2)
print(y3)
# k代表颜色，marker标记
line1 = axes.plot(list(y_test), markeredgecolor='black',marker='o',label='真实值')
line2 = axes.plot(list(y2), markeredgecolor='blue', marker='*', markersize=9,label='决策树回归')
line3 = axes.plot(list(y3),  markeredgecolor='red', marker='*', markersize=9,label='Bagging回归')
line4 = axes.plot(list(y1),  markeredgecolor='yellow', marker='*', markersize=9,label='线性回归')
axes.legend()
axes.set_title('多元回归')

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Subsetting the dataset
# Index 11856 marks the end of year 2013
df = pd.read_csv('jetrail.csv', nrows=11856)

# Creating train and test set
# Index 10392 marks the end of October 2013
train = df[0:10392]
test = df[10392:]


train['Timestamp'] = pd.to_datetime(train['Datetime'], format='%d-%m-%Y %H:%M')
train.index = train['Timestamp']
print(train['Count'])

df = pd.read_csv('7.csv', nrows=240)
train = df[0:230]

train.index = train['T']
print(train['S'])

import statsmodels.api as sm

sm.tsa.seasonal_decompose(train['S'],model = 'additive', period = int(len(train)/2)).plot()
result = sm.tsa.stattools.adfuller(train['S'])
plt.show()
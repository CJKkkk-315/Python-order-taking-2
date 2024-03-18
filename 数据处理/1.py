#时间戳转化成年月日，这个pd.to_datetime按照时间排序
#
import pandas as pd
data = pd.read_csv(r'D:\pythonProject\event_to_2019-01-05.csv')
data['T1'] = pd.to_datetime(data['T1'], unit='s') #需要转化的列名T1
data['T2'] = pd.to_datetime(data['T2'], unit='s')
data.to_csv(r'D:\pythonProject\event_to_2019-01-05_transfer.csv',encoding='utf-8')

#
#


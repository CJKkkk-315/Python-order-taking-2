import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
from random import randint
df = pd.read_csv('data.csv',encoding='gbk')
data = df['生日'].tolist()
data = list(map(lambda x:x.replace('月',''),data))
data = Counter(data)
xy = [[i,j] for i,j in data.items()]
x = [i[0] for i in xy]
y = [i[1] for i in xy]
plt.pie(x=y,labels=x)
plt.show()
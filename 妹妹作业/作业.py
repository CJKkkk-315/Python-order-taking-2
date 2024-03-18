import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from collections import defaultdict
df = pd.read_csv('data.csv',encoding='gbk')
n = df['姓名'].values.tolist()
d = []
for i in n:
    d.append(i[0])
d = Counter(d)
data = [[i,d[i]] for i in d.keys()]
for i in data:
    if i[0] == '严':
        data.remove(i)
        data.insert(0,i)
a = [i[0] for i in data]
b = [i[1] for i in data]
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.bar(a,b)
plt.show()



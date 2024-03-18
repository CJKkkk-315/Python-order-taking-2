import csv
import pandas as pd
df = pd.read_csv('data.csv',encoding='gbk')
a = df['姓名'].values.tolist()
b = df['学号'].values.tolist()
d = [[i,j] for i,j in zip(a,b)]
r = ['严桂英','孙圆','朱文静']
for i in d:
    if i[0] in r:
        d.remove(i)
        d.insert(0,i)
with open('sort.csv','w',newline='') as f:
    for i in range(len(d)):
        csv.writer(f).writerow([i+1]+d[i])

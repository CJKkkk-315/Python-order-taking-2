from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
data = defaultdict(list)
df = pd.read_csv('googleplaystore.csv')
head = list(df.columns)
df = df.values.tolist()
for i in df:
    data[i[0]].append(i[1:])
for i in data.keys():
    data[i].sort(key=lambda x:int(x[2]))
    data[i] = data[i][-1]
res = []
for i in data:
    res.append([i]+data[i])
df = {}
for i in range(len(head)):
    df[head[i]] = [j[i] for j in res]
df = pd.DataFrame(df)
df.to_csv('clear.csv',index=None)
d = [i[1] for i in res]
d = Counter(d)
data = []
for i,j in d.items():
    data.append([i,j])
data.sort(key=lambda x:x[1])
data = data[::-1]
x = [i[1] for i in data]
labels = [i[0] for i in data]
plt.pie(x=x,labels=labels)
plt.show()
print(labels[:3])


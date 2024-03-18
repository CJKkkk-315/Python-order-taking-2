import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
df = pd.read_excel('单科成绩单.xlsx')
data = df.values.tolist()
data = data[5:]
dataf = []
for i in data:
    aw = []
    for j in i:
        if str(j) != 'nan':
            try:
                aw.append(int(j))
            except:
                aw.append(j)
    dataf.append(aw)
dataf.sort(key=lambda x:x[6],reverse=True)
y = [i[6] for i in dataf][:10]
x = [i[2] for i in dataf][:10]
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.bar(x,y)
plt.title('总分排名前10')
plt.show()
pinci = Counter([i[6] for i in dataf])
xy = sorted(pinci.items())
x = [i[0] for i in xy]
y = [i[1] for i in xy]
plt.plot(x,y)
plt.show()
qujian = [str(i[6])[0] for i in dataf]
qujian = Counter(qujian)
print(qujian)
x = [i[0]+'0' for i in qujian.items()]
y = [i[1] for i in qujian.items()]
plt.pie(labels=x,x=y)
plt.show()
print(*dataf,sep='\n')
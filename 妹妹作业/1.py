import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
s1 = pd.read_excel("名单.xlsx")
last_name = []
for row in s1.itertuples():
    try:
        name = getattr(row, "姓名")
        last_name.append(name[:1])
    except:
        continue
last_name_num = {}
a = last_name_num
for i in last_name:
    try:
        a[i] += 1
    except:
        a[i] = 1
x = a.values
y = a.keys()
plt.bar(range(len(a)), list(a.values()), align='center')
plt.xticks(range(len(a)), list(a.keys()))
plt.show()

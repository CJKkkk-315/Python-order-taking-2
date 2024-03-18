import pandas as pd
import csv
data = []
with open('shuju.csv','r',encoding='utf-8') as f:
    fcsv = csv.reader(f)
    for i in fcsv:
        data.append(i)
data = data[1:]
d = {}
for i in data:
    try:
        try:
            d[str(i[0])[:8]].append(list(map(float,i[2:6])))
        except:
            d[str(i[0])[:8]] = [list(map(float,i[2:6]))]
    except:
        print(i)
res = []
for i in d.keys():
    s = [0,0,0,0]
    for j in d[i]:
        # print(j)
        s[0] += j[0]
        s[1] += j[1]
        s[2] += j[2]
        s[3] += j[3]
    s = list(map(lambda x:round(x/len(d[i]),2),s))
    if s:
        s.insert(0,i)
        res.append(s)
print(res)
head = ['时间','支出内容','A','B','C','D']
with open('res.csv','w',newline='') as f:
    fcsv = csv.writer(f)
    fcsv.writerow(head)
    for i in res:
        i.insert(1,'Q')
        fcsv.writerow(i)

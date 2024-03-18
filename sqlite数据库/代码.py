import sqlite3
import os
from collections import Counter
import csv
ext = 'db3'
files = os.listdir(os.getcwd())
ress = []
files = [i for i in files if i.split('.')[-1] == ext]
for file in files:
    data = []
    cx = sqlite3.connect(file)
    cur = cx.cursor()
    cur.execute('SELECT * FROM Image')
    res = cur.fetchall()
    for i in res:
        data.append(i[6])
    d = dict(Counter(data))
    ress.append([file,d['Content'],d['Do Not Key']])
head = ['db3 name','content','do not key']
with open('res.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(head)
    for i in ress:
        f_csv.writerow(i)


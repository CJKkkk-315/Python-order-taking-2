import csv
import requests
from bs4 import BeautifulSoup
import _thread
with open('clean.txt','r') as f:
    res2 = [i.replace('\n','') for i in f.readlines()]
aw = []
for url in res2:
    if url[:len('https://')] != 'https://' and url[:len('http://')] != 'http://':
        url = 'https://' + url
    aw.append(url)
res2 = aw[::]
print(len(res2))
res = []
flag = 0
def function(no,res2):
    n = 0
    global flag
    for url in res2:
        n += 1
        if url[:len('https://')] != 'https://' and url[:len('http://')] != 'http://':
            url = 'https://' + url
        try:
            title = BeautifulSoup(requests.get(url,timeout=(5, 20)).text).find(name='title').text
            res.append([url,title])
        except:
            title = '网址错误'
            res.append([url,title])
        if n%50 == 0:
            print(no,n)
    flag += 1
rr = [[] for i in range(30)]
for i in range(len(res2)):
    rr[i%30].append(res2[i])
for i in range(30):
    _thread.start_new_thread(function, (i,rr[i],))
while 1:
   if flag == 30:
       break
with open('res.csv','w',encoding='utf-8') as f:
    for i in res:
        try:
            f.write(','.join(i)+'\n')
        except:
            print('-----------')

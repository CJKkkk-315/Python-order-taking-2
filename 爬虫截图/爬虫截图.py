import csv
import requests
from bs4 import BeautifulSoup
import _thread
with open('url.txt','r') as f:
    res2 = [i.replace('\n','') for i in f.readlines()]
aw = []
for url in res2:
    tt = url.replace('https://','').split('.')
    if tt[0].isdigit() and tt[1].isdigit() and tt[2].isdigit():
        aw.append(url)
    else:
        if tt[0] != 'www':
            url.replace(tt[0]+'.','')
        aw .append(url)
res2 = aw[::]
aw = []
for url in res2:
    if url[:len('https://')] != 'https://' and url[:len('http://')] != 'http://':
        url = 'http://' + url
    aw.append(url)
res2 = aw[::]
res2 = list(set(res2))
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
        if n%10 == 0:
            print(no,n)
    flag += 1
xcn = 30
rr = [[] for i in range(xcn)]
for i in range(len(res2)):
    rr[i%xcn].append(res2[i])
for i in range(xcn):
    _thread.start_new_thread(function, (i,rr[i],))
while 1:
   if flag == xcn:
       break
with open('ans.csv','w',encoding='utf-8',newline='') as f:
    fcsv = csv.writer(f)
    for i in res:
        try:
            fcsv.writerow(i)
        except:
            print('-----------')

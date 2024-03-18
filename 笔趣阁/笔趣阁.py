import requests
from bs4 import BeautifulSoup
import _thread
import csv
flag = 0
data = []
qc = []
dataf = []
f = open('数据.csv','a+',newline='')
f_csv = csv.writer(f)
nid = 0
# 爬取10页数据
for i in range(0,10):
    url = 'https://www.xbiquge.la/fenlei/1_' + str(i) + '.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    flag = 0
    # 解析以后遍历每一页数据的所有小说选项
    for i in soup.find(class_='l').find(name='ul').find_all(name='li'):
        a = i.find(name='a').text
        if a not in qc:
            nid += 1
            qc.append(a)
            # 将需要的内容做成列表添加到data中
            data.append([nid,a,i.find(name='a')['href']])
print(len(data))
jdata = [[] for _ in range(10)]
for i in range(len(data)):
    jdata[i%10].append(data[i])
# 开启多线程爬取 加快速度
def function(name,data):
    global flag
    for i in data:
        response = requests.get(i[2])
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text)
        i.append(soup.find(id='info').find(name='p').text.split('：')[-1])
        i.append(soup.find(id='intro').find_all(name='p')[-1].text)
        i.append(soup.find(id='fmimg').find(name='img')['src'])
        f_csv.writerow(i)
        print(i)
    flag += 1
try:
   _thread.start_new_thread(function, ("Thread-1", jdata[0],))
   _thread.start_new_thread(function, ("Thread-2", jdata[1],))
   _thread.start_new_thread(function, ("Thread-3", jdata[2],))
   _thread.start_new_thread(function, ("Thread-4", jdata[3],))
   _thread.start_new_thread(function, ("Thread-5", jdata[4],))
   _thread.start_new_thread(function, ("Thread-1", jdata[5],))
   _thread.start_new_thread(function, ("Thread-2", jdata[6],))
   _thread.start_new_thread(function, ("Thread-3", jdata[7],))
   _thread.start_new_thread(function, ("Thread-4", jdata[8],))
   _thread.start_new_thread(function, ("Thread-5", jdata[9],))
except:
   print ("Error: 无法启动线程")
while 1:
   if flag == 10:
       break
f.close()
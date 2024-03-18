import requests
from bs4 import BeautifulSoup
import pymysql
import _thread
import os
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='cjk123',
    passwd='123456',
    db='接单',
    charset='utf8mb4'
)
cursor = connect.cursor()
for ye in range(10):
    url = 'https://www.xbiquge.la/fenlei/1_' + str(ye) + '.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    data = []
    flag = 0
    for i in soup.find(class_='l').find(name='ul').find_all(name='li'):
        data.append([i.find(name='a').text,i.find(name='a')['href']])
    for i in data:
        response = requests.get(i[1])
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text)
        i.append(soup.find(id='info').find(name='p').text.split('：')[-1])
        i.append(soup.find(id='intro').find_all(name='p')[-1].text)
        i.append(soup.find(id='fmimg').find(name='img')['src'])
        i.append('玄幻')
        x = []
        for j in soup.find(id='list').find_all(name='dd'):
            x.append('https://www.xbiquge.la' + j.find(name='a')['href'])
            if len(x) == 10:
                break
        i.append(x)
        try:
            sql = "INSERT INTO 小说简要信息 (书名, 网址,作者, 简介,封面,类型) VALUES ( '%s', '%s', '%s', '%s' , '%s','%s')"
            d = (i[0], i[1], i[2], i[3],i[4],i[5])
            cursor.execute(sql % d)
            connect.commit()
            print('成功插入', cursor.rowcount, '条数据')
        except:
            continue
    def function(name,data):
        global flag
        for i in data:
            try:
                os.makedirs(i[0])
                for j in range(len(i[5])):
                    response = requests.get(i[5][j])
                    response.encoding = 'utf-8'
                    soup = BeautifulSoup(response.text)
                    name = soup.find(class_='bookname').find(name='h1').text
                    content = soup.find(id='content').text.replace('&nbsp;', '')
                    with open(i[0] + '/' + '章节' + str(j+1) + '   ' + name + '.txt','w',encoding='utf-8') as f:
                        f.write(content)
            except:
                pass
        flag += 1
    jdata = [[] for i in range(10)]
    for i in range(len(data)):
        jdata[i % 10].append(data[i])
    print(jdata)
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
import requests
import pymysql
from bs4 import BeautifulSoup
import _thread
import os
import csv
zuozhe = []
with open('data.csv','r') as f:
    fcsv = csv.reader(f)
    for i in fcsv:
        try:
            zuozhe.append(i[0])
        except:
            break
zuozhe = zuozhe[1:]
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='cjk123',
    passwd='123456',
    db='接单',
    charset='utf8mb4'
)
cursor = connect.cursor()
for zz in zuozhe:
    url = "https://www.xbiquge.la/modules/article/waps.php"

    payload = 'searchkey='+zz
    payload = payload.encode('utf-8')
    headers = {
      'Connection': 'keep-alive',
      'Cache-Control': 'max-age=0',
      'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Opera";v="85"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'Upgrade-Insecure-Requests': '1',
      'Origin': 'https://www.xbiquge.la',
      'Content-Type': 'application/x-www-form-urlencoded',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.75',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'Sec-Fetch-Site': 'same-origin',
      'Sec-Fetch-Mode': 'navigate',
      'Sec-Fetch-User': '?1',
      'Sec-Fetch-Dest': 'document',
      'Referer': 'https://www.xbiquge.la/modules/article/waps.php',
      'Accept-Language': 'zh-CN,zh;q=0.9',
      'Cookie': 'Hm_lvt_8744b58bc1913cae0d8c4dc68f187d61=1647785408; UM_distinctid=17fa7a9f6aae2a-0b86448c195e53-405d486d-144000-17fa7a9f6abd99; Hm_lvt_b48494e860b198c9c71009978cfc755e=1647785408; BAIDU_SSP_lcr=https://www.baidu.com/link?url=66BIG_Q_yJG0rRoaCY2AEpeVGqpUqZiKbXqnQmuSl_0mUr1IWNiNBgKpQclL5-ESx6nuzX5bnLxX5Q82pGV4-q&wd=&eqid=d0f6752700083d9e00000005623735bb; CNZZDATA1280572003=1820377410-1647785119-https%253A%252F%252Fwww.xbiquge.la%252F%7C1647785119; Hm_lvt_2d2ceac9af7f7f1a8dbdd51db6dbf36c=1647785414; Hm_lvt_dd3a5d36b1adfd567e4b8290c0760ba3=1647785416; 5531_2334_112.49.166.197=1; 5531_2444_112.49.166.197=1; Hm_lvt_4ad6b1a6d9755b262a181c469db16477=1647785574; 5531_2603_112.49.166.197=1; CNZZDATA1280572006=1474380178-1647774785-https%253A%252F%252Fwww.xbiquge.la%252F%7C1647785585; 5531_2334_27.159.92.242=1; 5531_2578_27.159.92.242=1; 5531_2403_27.159.92.242=1; CNZZDATA1280572013=1570929261-1647778234-https%253A%252F%252Fwww.xbiquge.la%252F%7C1647784017; Hm_lpvt_2d2ceac9af7f7f1a8dbdd51db6dbf36c=1647788061; Hm_lpvt_4ad6b1a6d9755b262a181c469db16477=1647788205; Hm_lpvt_dd3a5d36b1adfd567e4b8290c0760ba3=1647788205; CNZZDATA1280571925=1483976069-1647776817-https%253A%252F%252Fwww.baidu.com%252F%7C1647825833; CNZZDATA1280571999=578702682-1647782083-https%253A%252F%252Fwww.baidu.com%252F%7C1647828911; Hm_lpvt_8744b58bc1913cae0d8c4dc68f187d61=1647834580; Hm_lpvt_b48494e860b198c9c71009978cfc755e=1647834580; Hm_lvt_169609146ffe5972484b0957bd1b46d6=1650626854; _abcde_qweasd=0; Hm_lpvt_169609146ffe5972484b0957bd1b46d6=1652576745'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    response.encoding = 'UTF-8'
    soup = BeautifulSoup(response.text)
    # print(soup)
    data = []
    flag = 0
    for i in soup.find(name='table').find_all(name='tr')[1:11]:
        data.append([i.find(name='a').text,i.find(name='a')['href']])
    for i in data:
        response = requests.get(i[1])
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text)
        i.append(soup.find(id='info').find(name='p').text.split('：')[-1])
        i.append(soup.find(id='intro').find_all(name='p')[-1].text)
        i.append(soup.find(id='fmimg').find(name='img')['src'])
        i.append(soup.find(class_='con_top').find_all(name='a')[-1].text)
        x = []
        for j in soup.find(id='list').find_all(name='dd'):
            x.append('https://www.xbiquge.la' + j.find(name='a')['href'])
            if len(x) == 10:
                break
        i.append(x)
        print(i)
        try:
            sql = "INSERT INTO 小说简要信息 (书名, 网址,作者, 简介,封面,类型) VALUES ( '%s', '%s', '%s', '%s' , '%s','%s')"
            d = (i[0], i[1], i[2], i[3], i[4],i[5])
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
                for j in range(len(i[6])):
                    response = requests.get(i[6][j])
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

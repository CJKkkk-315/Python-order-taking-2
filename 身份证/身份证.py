def doVerify(id):
    if len(id) != 18:
        return False
    sum = 0
    wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    for i in range(17):
        sum += int(id[i]) * wi[i]
    j = sum%11
    rem = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    if id[17]==rem[j]:
        return True
    else:
        return False
import requests
from bs4 import BeautifulSoup
import pymysql
import json
ids = []
for page in range(1,106):
    res = requests.get('http://172.19.163.200:5003/GetIds?stdid=2102030220&page='+str(page))
    soup = BeautifulSoup(res.text)
    for i in soup.find(name='tbody').find_all(name='tr'):
        ids.append(i.find_all(name='td')[5].text.replace(' ',''))
bad_ids = []
good_ids = []
for i in ids:
    if doVerify(i):
        age = i[6:10]
        if int(age) > 2022:
            bad_ids.append(i)
        else:
            url = 'http://172.19.163.200:5003/GetDistrict?stdid=2102030220&no=' + i
            js = requests.get(url).text
            js.encode('utf-8')
            js = json.loads(js)
            if len(js['original registered residence'].split(' ')) != 3:
                bad_ids.append(i)
            else:
                good_ids.append(i)
    else:
        bad_ids.append(i)
bad_ids.sort(reverse=True)
for i in bad_ids:
    print(i)


sql_data = []
all_data = []
for i in good_ids:
    bir = i[6:10] + '年' + i[10:12] + '月' + i[12:14] + '日'
    url = 'http://172.19.163.200:5003/GetDistrict?stdid=2102030220&no=' + i
    js = requests.get(url).text
    js.encode('utf-8')
    js = json.loads(js)
    pl = js['original registered residence']
    if int(i[16])%2 == 1:
        sex = '男'
        sql_data.append(['2102030200', i, pl, bir, '男'])
    else:
        sex = '女'
    all_data.append(['2102030200', i, pl, bir, sex])
UserId = "2102030220"
Pswd = "aYN7M0h1"
try:
    cnct = pymysql.connect(host='172.19.163.200', user=UserId, password=Pswd, port=3306, db='dxjsj_dzy', charset='utf8')
except:
    print("connect error")
    exit()
for i in range(len(sql_data)):
    crsr = cnct.cursor()
    sql = "INSERT INTO ids_2022_2102030220 (stdid,id,plc,dob,gdr) VALUES('%s','%s','%s','%s','%s')"
    data = tuple(sql_data[i])
    crsr.execute(sql % data)
    cnct.commit()



with open('D:\dxjsj-id-2102030220.txt','w') as f:
    for i in all_data:
        f.write('，'.join(i)+'\n')
File = open('D:\dxjsj-id-2102030220.txt', 'rb')
files = {'result': ('dxjsj-id-2102030220.txt', File, 'multipart/form-data', {'Expires': '0'})}
res = requests.post('http://172.19.163.200:5003/upload',files=files)
print(res.text)


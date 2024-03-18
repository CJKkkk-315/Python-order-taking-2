import pymysql
import requests
from bs4 import BeautifulSoup
import json
StdId = "2102030114"
TableName = "ids_2022_2102030114"
UserId = "dzy_2102030114"
Pswd = "P631fL97"
cnct = pymysql.connect(host='172.19.163.200', user=UserId, password=Pswd, port=3306, db='dxjsj_dzy', charset='utf8')
crsr = cnct.cursor()
url = 'http://172.19.163.200:5003/GetIds?stdid=2102030114&page='
uids = []
for i in range(1,293):
    response = requests.get(url+str(i))
    soup = BeautifulSoup(response.content)
    for j in soup.find(name='tbody').find_all(name='tr'):
        uid = j.find_all(name='td')[1].text.replace(' ','')
        uids.append(uid)
with open('w_dxjsj-id-2102030114.txt','r') as f:
    wrong = [i.replace('\n','') for i in f.readlines()]
right_uid = [i for i in uids if i not in wrong]
def f2e(uid):
    if int(uid[6:8]) <= 22:
        uid = uid[:6] + '20' + uid[6:]
    else:
        uid = uid[:6] + '19' + uid[6:]
    w = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    t = sum([w[i]*int(uid[i]) for i in range(17)])
    f = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]
    uid += f[t % 11]
    return uid
for Id in right_uid:
    if len(Id) == 15:
        Id = f2e(Id)
    if int(Id[-2]) % 2 == 1:

        sql = "insert into " + TableName + "(stdid, id, plc, dob, gdr) values(%s, %s, %s, %s, %s)"
        data = json.loads(requests.get('http://172.19.163.200:5003/GetDistrict?stdid=2102030114&no=' + Id).content)
        city = data['original registered residence']
        birth = Id[6:10] + '年' + Id[10:12] + '月' + Id[12:14] + '日'
        data = (StdId, Id, city, birth, "男")
        i = crsr.execute(sql, data)
        cnct.commit()
crsr.close()
cnct.close()
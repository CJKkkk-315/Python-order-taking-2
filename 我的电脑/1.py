import requests
from bs4 import BeautifulSoup
import time
import json
url = 'http://172.19.163.200:5003/GetIds?stdid=2102030114&page='
uids = []
for i in range(1,293):
    response = requests.get(url+str(i))
    soup = BeautifulSoup(response.content)
    for j in soup.find(name='tbody').find_all(name='tr'):
        uid = j.find_all(name='td')[1].text.replace(' ','')
        uids.append(uid)
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
def is_valid_uid(s):
    w = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    t = sum([w[i] * int(s[i]) for i in range(17)])
    f = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]
    if s[-1] == f[t % 11]:
        return True
    else:
        return False
def is_valid_date(s):
    try:
        time.strptime(s, "%Y%m%d")
        return True
    except:
        return False
wrong = []
for uid in uids:
    if len(uid) == 15:
        u = f2e(uid)
    elif len(uid) == 18:
        u = uid
    else:
        wrong.append(uid)
        continue
    if int(u[6:10]) > 2022:
        wrong.append(uid)
        continue
    if not is_valid_date(u[6:14]):
        wrong.append(uid)
        continue
    if not is_valid_uid(u):
        wrong.append(uid)
        continue
    data = json.loads(requests.get('http://172.19.163.200:5003/GetDistrict?stdid=2102030114&no='+u).content)
    if len(data['original registered residence'].split()) != 3:
        wrong.append(uid)
        continue
wrong.sort(key=lambda x:x if len(x) == 18 else f2e(x),reverse=True)
with open('w_dxjsj-id-2102030114.txt','w') as f:
    for i in wrong:
        f.write(i+'\n')






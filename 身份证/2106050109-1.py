wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1, ]
vi = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2, ]
import json
import requests
import pymysql
def get_verity(eighteen_card):
    """

    :param eighteen_card:
    :return:
    """
    remaining = ''
    if len(eighteen_card) == 18:
        eighteen_card = eighteen_card[0:-1]
    if len(eighteen_card) == 17:
        ai = [int(i) for i in eighteen_card]
        s = sum(wi[i] * ai[i] for i in range(17))
        remaining = s % 11
    return 'X' if remaining == 2 else str(vi[remaining])
def up_to_eighteen(fifteen_card):
    """
    15位转18位
    :param fifteen_card:
    :return:
    """
    eighteen_card = fifteen_card[0:6] + '19' + fifteen_card[6:15]
    return eighteen_card + get_verity(eighteen_card)
r = []
l = []
with open('2106050109.txt', 'r') as f:
    for line in f.readlines():
        card = line.strip()
        # print(line)
        n = len(card)
        if card == '':
            continue
        if n != 15 and n != 18:
            l.append(card)
        elif len(card) == 15:
            card = up_to_eighteen(card)
        elif card[-1] != get_verity(card):
            nianling = card[6:10]
            if int(nianling) > 2022:
                l.append(card)
            else:
                url = 'http://172.19.163.200:5003/GetDistrict?stdid=2102030220&no=' + card
                data = requests.get(url).text
                data.encode('utf-8')
                data = json.loads(data)
                city = data['original registered residence'].split(' ')
                if len(city) < 3:
                    l.append(card)
                else:
                    r.append([card,' '.join(city)])
l.sort(reverse=True)
print('\n'.join(l))




UserId = "2106050109"
Pswd = "DJOnQOVO"
rsql = []
for i in r:
    if int(i[0][-2]) % 2 == 1:
        rsql.append(i)
try:
    cnct = pymysql.connect(host='172.19.163.200', user=UserId, password=Pswd, port=3306, db='dxjsj_dzy', charset='utf8')
except:
    print("connect error")
    exit()
for i in r:
    crsr = cnct.cursor()
    sql = "INSERT INTO ids_2022_2106050109 (stdid,id,plc,dob,gdr) VALUES('%s','%s','%s','%s','%s')"
    data = tuple(['2106050109',i[0],i[1],i[0][6:10] + '年' + i[0][10:12] + '月' + i[0][12:14] + '日','男'])
    crsr.execute(sql % data)
    cnct.commit()
res = []
for i in r:
    if int(i[0][-2])%2 == 1:
        s = '男'
    else:
        s = '女'
    res.append(['2106050109',i[0],i[1],i[0][6:10] + '年' + i[0][10:12] + '月' + i[0][12:14] + '日',s])
with open('dxjsj-id-2106050109.txt','w') as f:
    for i in res:
        f.write('，'.join(i)+'\n')





File = open('dxjsj-id-2106050109.txt', 'rb')
files = {'result': ("dxjsj-id-2106050109.txt", File, 'multipart/form-data', {'Expires': '0'})}
response = requests.post('http://172.19.163.200:5003/upload',files=files)
print(response.content)
import requests
from bs4 import BeautifulSoup
response = requests.get('http://www.tianqihoubao.com/lishi/')
response.encoding = 'gbk'
soup = BeautifulSoup(response.text)
res = []
for i in soup.find(class_='citychk').find_all('dl'):
    p = i.find(name='dt').text
    for j in i.find(name='dd').find_all(name='a'):
        res.append([p,j.text])
        print([p,j.text])
import csv
with open('省份城市数据.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in res:
        f_csv.writerow(i)


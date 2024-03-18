import csv
import requests
import pandas
from bs4 import BeautifulSoup
import os
ext='.xlsx'
files = [f for f in os.listdir() if os.path.isfile(f) and os.path.splitext(f)[1]==ext]
headers = {

      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.45',
    }
dic = {}
file = files[0]
df = pandas.read_excel(file)
hosipital_list = df.values.tolist()
hosipital_list = [i[0] for i in hosipital_list]
for i in hosipital_list:
    dic[i] = []
for hosipital in hosipital_list:
    url = f'https://www.yixue.com/{hosipital}'
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text)
        ans = soup.find(id='mw-content-text').find(name='ul').find_all(name='li')[5].text
        dic[hosipital].append(ans)
    except:
        dic[hosipital].append('未收录')
    try:
        url = f'https://so.99.com.cn/search.php?s=relevance&proj=yyk&f=_all&q={hosipital}'
        res = requests.get(url,headers=headers)
        soup = BeautifulSoup(res.text)
        url1 = soup.find(class_='yy-cont').find(name='a')['href']
        res = requests.get(url1,headers=headers)
        soup = BeautifulSoup(res.text)
        ans = soup.find(class_='wrap-info').find(name='dd').find_all(name='p')[1].text
        dic[hosipital].append(ans)
    except:
        dic[hosipital].append('未收录')
    try:
        res = requests.get(f'https://y.dxy.cn/hospital/?&page=1&name={hosipital}')
        soup = BeautifulSoup(res.text)
        ans = soup.find(id='hospitallist').find(class_='tr').find_all(class_='td')[2].text
        dic[hosipital].append(ans)
    except:
        dic[hosipital].append('未收录')
head = ['医院','医学百科结果','99健康结果','丁香结果']
with open('结果.csv','w',newline='',encoding='utf-8') as f:
    fcsv = csv.writer(f)
    fcsv.writerow(head)
    for i,j in dic.items():
        fcsv.writerow([i]+dic[i])
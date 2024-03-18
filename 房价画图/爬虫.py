import requests, time
from bs4 import BeautifulSoup
hio = []
fio = []
tpc = []
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Referer': 'http://www.baidu.com/link?url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;amp;wd=&amp;amp;eqid=c3435a7d00006bd600000003582bfd1f'
}

for i in range(1, 50):
    print(i)
    url = 'http://bj.lianjia.com/ershoufang/pg' + str(i) + "/"
    res = requests.get(url=url, headers=headers)
    html = res.text
    time.sleep(0.7)

    lj = BeautifulSoup(html, 'html.parser')

    # 提取价格信息
    price = lj.find_all("div", attrs={"class": "priceInfo"})

    for p in price:
        totalPrice = p.span.string
        tpc.append(totalPrice)

    # 提取房源信息
    houseInfo = lj.find_all("div", attrs={"class": "houseInfo"})

    for h in houseInfo:
        house = h.get_text()
        hio.append(house)

    # 提取关注度信息
    followInfo = lj.find_all("div", attrs={"class": "followInfo"})

    for f in followInfo:
        follow = f.get_text()
        fio.append(follow)

##创建数据表（构造DataFrame）
import pandas as pd

house = pd.DataFrame({"totalprice": tpc, "houseinfo": hio, "followinfo": fio})

# 检查下数据集构造的情况
house.to_csv('data.csv')

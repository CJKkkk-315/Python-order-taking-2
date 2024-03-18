import requests
from bs4 import BeautifulSoup
import csv
urls = '''https://tyj.henan.gov.cn/qmjs/
https://tyj.henan.gov.cn/jjty/
https://tyj.henan.gov.cn/tycy/
https://tyj.henan.gov.cn/qsnty/
https://tyj.henan.gov.cn/tywh/
https://tyj.henan.gov.cn/styj/tyxw/tyzh/
https://tyj.henan.gov.cn/xxgk/zcwj/
https://tyj.henan.gov.cn/xxgk/zcjd/
https://tyj.henan.gov.cn/styj/xxgk/xwfb/
https://tyj.henan.gov.cn/styj/xxgk/rsxx/
https://tyj.henan.gov.cn/styj/xxgk/rdjyzxtagk/
https://tyj.henan.gov.cn/styj/xxgk/zdlyxxgk/xzqlqd/
https://tyj.henan.gov.cn/styj/xxgk/zdlyxxgk/czzj/
https://tyj.henan.gov.cn/xxgk/zfxxgknb/'''
headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cache-Control': 'max-age=0',
  'Connection': 'keep-alive',
  'Cookie': 'yfx_c_g_u_id_10000046=_ck22062209322412737974483139993; yfx_f_l_v_t_10000046=f_t_1655861544274__r_t_1655861544274__v_t_1655861544274__r_c_0',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'none',
  'Sec-Fetch-User': '?1',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.45',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Opera";v="87"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}
result = []
urls = urls.split('\n')
for url in urls:
    for i in range(1,200):
        url0 = url + f'index_{i}.html'
        try:
            res = requests.get(url0,headers=headers)
            if res.status_code != 200:
                print(i)
                break
            soup = BeautifulSoup(res.content)
            for j in soup.find(class_='newsList fr').find_all(name='li'):
                title = j.find(name='a').text
                suburl = j.find(name='a')['href']
                time = j.find(name='span').text
                result.append([title,time,suburl])
        except:
            print(url0)
with open('henan.csv','w',encoding='utf8',newline='') as f:
    fcsv = csv.writer(f)
    for i in result:
        fcsv.writerow(i)




import requests
from bs4 import BeautifulSoup
import csv
url = '''http://sport.hebei.gov.cn/tiyukuaixun/
http://sport.hebei.gov.cn/shengjuyaowen/
http://sport.hebei.gov.cn/tongzhigonggao/
http://sport.hebei.gov.cn/xinwenzhongxin/xinwenfabu/
http://sport.hebei.gov.cn/shixianxinwen/
http://sport.hebei.gov.cn/ticaizhichuang/
http://sport.hebei.gov.cn/qunzhongtiyu/sshd/
http://sport.hebei.gov.cn/quanminjianshenzhinan/
http://sport.hebei.gov.cn/jingjitiyu/sshd/
http://sport.hebei.gov.cn/jingjitiyu/yyxl/
http://sport.hebei.gov.cn/jingjitiyu/rcpx/
http://sport.hebei.gov.cn/faguichanye/gzdt/
http://sport.hebei.gov.cn/faguichanye/zcfg/
http://sport.hebei.gov.cn/gongchengjianshe/zhengcefagui/
http://sport.hebei.gov.cn/gongchengjianshe/zhengcejiedu/
http://sport.hebei.gov.cn/yishenqinggongkai/
http://sport.hebei.gov.cn/zhengwugongkai/gbrm/
http://sport.hebei.gov.cn/zhengfenghangfeng/
http://sport.hebei.gov.cn/xinxigongkainianbao/
http://sport.hebei.gov.cn/xingzhengshenpi/
http://sport.hebei.gov.cn/zhengfuxinxigongkai/jianyitian/'''
result = []
urls = url.split('\n')
for url0 in urls:
    try:
        head = url0
        res = requests.get(url0)
        soup = BeautifulSoup(res.content)
        page = int(soup.find(class_='pageinfo').find(name='strong').text)
        end = '_'.join(soup.find(class_='pagelist').find_all(name='li')[-3].find(name='a')['href'].split('_')[:2])
        for i in range(1,page):
            try:
                url = head + end + '_' + str(i) + '.html'
                res = requests.get(url)
                soup = BeautifulSoup(res.content)
                for i in soup.find(class_='am-list-news-bd').find(name='ul').find_all(name='li'):
                    title = i.find(name='h3').text
                    time = i.find_all(name='div')[-1].text.split()[1]
                    suburl = i.find(name='h3').find(name='a')['href']
                    result.append([title,time,suburl])
            except:
                continue
    except:
        print(url0)
with open('hebei.csv','w',encoding='utf8',newline='') as f:
    fcsv = csv.writer(f)
    for i in result:
        fcsv.writerow(i)
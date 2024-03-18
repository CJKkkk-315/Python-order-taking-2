import requests
import re
import json
import csv
import time
data = []

gwd = {'PYTHON开发工程师':'PYTHON%25E5%25BC%2580%25E5%258F%2591','JAVA开发工程师':'JAVA%25E5%25BC%2580%25E5%258F%2591','C++开发工程师':'C++%25E5%25BC%2580%25E5%258F%2591','Linux工程师':'Linux%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588','算法工程师':'%25E7%25AE%2597%25E6%25B3%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588','数据工程师':'%25E6%2595%25B0%25E6%258D%25AE%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588','前端工程师':'%25E5%2589%258D%25E7%25AB%25AF%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588','软件测试工程师':'%25E8%25BD%25AF%25E4%25BB%25B6%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588','Android开发工程师':'Android%25E5%25BC%2580%25E5%258F%2591'}
l = ['010000 北京','020000 上海','030200 广州','040000 深圳','080200 杭州','180200 武汉','110200 福州','110300 厦门']
for jobname,jobid in gwd.items():
    print(jobname)
    for city in l:
        cityname = city.split(' ')[1]
        cityid = city.split(' ')[0]
        for page in range(1,2):
            time.sleep(2)
            url = f"https://search.51job.com/list/"+ cityid + ",000000,0000,00,9,99," + jobid + ",2," + str(page) +".html"
            # print(f'---正在爬取第{page}内容')
            headers = {
                    "Cookie":"_uab_collina=164398700352489499277809; guid=dd5fa5e1a8551bca236c198a882373a2; _ujz=MjAyNjY1OTk1MA%3D%3D; ps=needv%3D0; 51job=cuid%3D202665995%26%7C%26cusername%3DwZ%252BfVjoUzalLd19p7QGCFP12gZuI1rjWc3rX7L19BmM%253D%26%7C%26cpassword%3D%26%7C%26cname%3DUbCTfLG3NyaIG2%252FL%252FMrSgg%253D%253D%26%7C%26cemail%3D%26%7C%26cemailstatus%3D0%26%7C%26cnickname%3D%26%7C%26ccry%3D.0GDGHq0rx5cc%26%7C%26cconfirmkey%3D%25241%2524z5VQkAf2%2524t8xS4fTkJvV5jTv1mejC3.%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D0%26%7C%26cnamekey%3D%25241%2524nucVGvJT%2524KLn5NtN7ZkyO4CqT2xuPJ.%26%7C%26to%3D3df7792abdee956d6f4ad84bd581b3c661fd4021%26%7C%26; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; acw_tc=76b20fed16447395722957137e16b574b659d047d2407b6be77a8d8ec34149; acw_sc__v3=6208bbf7ffaa96fc9df39397f7e1ffb5eb61d0e0; slife=lastlogindate%3D20220213%26%7C%26; acw_sc__v2=6208bdab53671a53a324df5ba877cd0b04297a6b; search=jobarea%7E%60000000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%BF%AA%B7%A2%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FAPython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%B2%E2%CA%D4%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; ssxmod_itna2=Qqjx2DnDRG68DXirqExUxxGxWqH11xmqeDt8D6h8Aa87D0ypRD03peecjU2D6jEI=P8GgMp08+Q+n9Pw+f2OyN13mRnGWpK5zLk6Lo7FTuU+/eHwDO6p8HMENk8HtNE1eM+uWvhLG7mznhIHj1nzC7eG7p9zXgAkdInhQ8v8izPhG1pC9AHzogO7L2OEtzp+yo9Nzh0mtxv1s/PfvRYkHQcC+rToXOKiSWO=DPchHWlPpe9NSxmzRZlDrxEFuOq2uPp+xNGOj1Zyl1a8QL7g3Auk9CeuNcUxT2z2K7ukpwnTpsQQHNcbeyHU9a7T0fqQtYF49aF+OQTPlH2eq0fyD6BTYYsUK4dH9GrStqQ8vz7uuI4k9cSGh3dadswtlrRzRn/Ru+K3D07PxDLxD2nGDD==; ssxmod_itna=Cq0x9DnQKeqmqxBP+POoP4DqAKYRx2R4GNKUYDZDiqAPGhDC3fPhid4iK6Ct=+xmlx7KdgUr80UmZYOiwqb8mK2ieDHxY=DU=QHeoD43KGwD0eG+DD4DWDmnFDnxAQDjxGPc0EHv=DEDYPcDA3Di4D+WwQDmqG0DDUaR4G2D7tcQ75ctQLPvkRBKSiK7i=DjLbD/+wWci65apa=RMiro6pCKDDH9rHKniq117DiDmeRDB=mxBjSITX6IWy99utDcxxbRreCt34tQOYKYYe=K3hoYcLP9D53B2GxBA5LfDv37iD==",
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
            }
            #通过requests模块里面的get请求方法，对url发送请求，并且携带上headers请求头，最后用response变量接收数据
            response = requests.get(url=url,headers=headers)
            #获取数据 获取服务器返回的response响应数据
            print(response.text)
            #解析数据，提取想要的内容.*?匹配任意字符(除了\n以外)
            html_data = re.findall('window.__SEARCH_RESULT__ = (.*?)</script>', response.text)[0]
            # print(html_data)
            #字符串数据 转成字典数据类型 因为字典提取数据更方便
            json_data = json.loads(html_data)
            # print(json_data)
            #json数据取值，就是根据冒号左边的内容提取右边的内容
            engine_jds = json_data['engine_jds']
            #提取出来返回列表，列表一个一个提取元素 用for遍历循环
            if not engine_jds:
                break
            for index in engine_jds:
            #为了方便等会保存数据，提取出来的数据内容可以用字典接收
                    v1 = jobname
                    v2 = index['job_name']
                    v3 = index['providesalary_text']
                    v4 = cityname
                    v5 = index['companysize_text']
                    v6 = index['attribute_text'][1]
                    if v5 and ('经验' in v6 or v6 == '在校生/应届生'):
                        print([v1,v2,v3,v4,v5,v6])
                        data.append([v1,v2,v3,v4,v5,v6])
f = open('result.csv','w')
f_csv = csv.writer(f)
for i in data:
    f_csv.writerow(i)
f.close()
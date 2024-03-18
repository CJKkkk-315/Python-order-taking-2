import requests
import re
import json
import csv
import time
data = []
f = open('result.csv','w',newline='')
f_csv = csv.writer(f)
headers = {
                    "Cookie":"_uab_collina=164398700352489499277809; guid=dd5fa5e1a8551bca236c198a882373a2; _ujz=MjAyNjY1OTk1MA%3D%3D; ps=needv%3D0; 51job=cuid%3D202665995%26%7C%26cusername%3DwZ%252BfVjoUzalLd19p7QGCFP12gZuI1rjWc3rX7L19BmM%253D%26%7C%26cpassword%3D%26%7C%26cname%3DUbCTfLG3NyaIG2%252FL%252FMrSgg%253D%253D%26%7C%26cemail%3D%26%7C%26cemailstatus%3D0%26%7C%26cnickname%3D%26%7C%26ccry%3D.0GDGHq0rx5cc%26%7C%26cconfirmkey%3D%25241%2524z5VQkAf2%2524t8xS4fTkJvV5jTv1mejC3.%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D0%26%7C%26cnamekey%3D%25241%2524nucVGvJT%2524KLn5NtN7ZkyO4CqT2xuPJ.%26%7C%26to%3D3df7792abdee956d6f4ad84bd581b3c661fd4021%26%7C%26; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; acw_tc=76b20fed16447395722957137e16b574b659d047d2407b6be77a8d8ec34149; acw_sc__v3=6208bbf7ffaa96fc9df39397f7e1ffb5eb61d0e0; slife=lastlogindate%3D20220213%26%7C%26; acw_sc__v2=6208bdab53671a53a324df5ba877cd0b04297a6b; search=jobarea%7E%60000000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%BF%AA%B7%A2%B9%A4%B3%CC%CA%A6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FAPython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%B2%E2%CA%D4%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; ssxmod_itna2=Qqjx2DnDRG68DXirqExUxxGxWqH11xmqeDt8D6h8Aa87D0ypRD03peecjU2D6jEI=P8GgMp08+Q+n9Pw+f2OyN13mRnGWpK5zLk6Lo7FTuU+/eHwDO6p8HMENk8HtNE1eM+uWvhLG7mznhIHj1nzC7eG7p9zXgAkdInhQ8v8izPhG1pC9AHzogO7L2OEtzp+yo9Nzh0mtxv1s/PfvRYkHQcC+rToXOKiSWO=DPchHWlPpe9NSxmzRZlDrxEFuOq2uPp+xNGOj1Zyl1a8QL7g3Auk9CeuNcUxT2z2K7ukpwnTpsQQHNcbeyHU9a7T0fqQtYF49aF+OQTPlH2eq0fyD6BTYYsUK4dH9GrStqQ8vz7uuI4k9cSGh3dadswtlrRzRn/Ru+K3D07PxDLxD2nGDD==; ssxmod_itna=Cq0x9DnQKeqmqxBP+POoP4DqAKYRx2R4GNKUYDZDiqAPGhDC3fPhid4iK6Ct=+xmlx7KdgUr80UmZYOiwqb8mK2ieDHxY=DU=QHeoD43KGwD0eG+DD4DWDmnFDnxAQDjxGPc0EHv=DEDYPcDA3Di4D+WwQDmqG0DDUaR4G2D7tcQ75ctQLPvkRBKSiK7i=DjLbD/+wWci65apa=RMiro6pCKDDH9rHKniq117DiDmeRDB=mxBjSITX6IWy99utDcxxbRreCt34tQOYKYYe=K3hoYcLP9D53B2GxBA5LfDv37iD==",
                    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
            }
gwd = ['PYTHON开发工程师','JAVA开发工程师','C++开发工程师','Linux工程师','算法工程师','数据工程师','前端工程师','软件测试工程师','Android开发工程师']
l = ['010000 北京','020000 上海','030200 广州','040000 深圳','080200 杭州','180200 武汉','110200 福州','110300 厦门']
for jobid in gwd:
    print(jobid)
    for city in l:
        # 将城市名和城市代码分开
        cityname = city.split(' ')[1]
        cityid = city.split(' ')[0]
        # 每个城市每个岗位爬取10页内容
        for page in range(1,10):
            # 设置两秒延迟，防止被反爬
            time.sleep(2)
            # 拼接URL
            url = "https://search.51job.com/list/"+ cityid + ",000000,0000,00,9,99," + jobid + ",2," + str(page) +".html"
            # request请求网页html数据
            response = requests.get(url=url,headers=headers)
            # 利用正则提取html中的json数据部分，再利用json库读取数据
            js = json.loads(re.findall('window.__SEARCH_RESULT__ = (.*?)</script>', response.text)[-1])
            # 提取出该页面的岗位信息列表
            js = js['engine_jds']
            # 遍历提取出来的岗位信息列表
            for index in js:
                    # 将我们所需要的对应数据提取出来存入data列表中
                    v1 = jobid
                    v2 = index['job_name']
                    v3 = index['providesalary_text']
                    v4 = cityname
                    print([v1,v2,v3,v4])
                    data.append([v1,v2,v3,v4])
dataf = []
# 设置各个关键词，不区分大小写，用来判断是否有错误的数据
keys = [['JAVA','java','Java'],['C++','c++','c'],['Python','python','PYTHON'],['前端'],['测试'],['Android','ANDROID','android'],['算法'],['数据'],['LINUX','Linux','linux']]
# 遍历列表，对列表的岗位分类找到keys中对应的关键词，再判断对应的关键词是否出现在了岗位名称中，若一个都没有出现，则判断为错误数据，不将其插入新列表
for i in data:
    flag = 1
    for key in keys:
        for word in key:
            if word in i[0]:
                for w in key:
                    if w in i[1]:
                        flag = 0
                        dataf.append(i)
                        break

# 遍历去除错误数据后的新列表
for i in dataf:
    # 对每个薪资以-符号分隔为2个元素
    if '-' in i[2]:
        aw = i[2].split('-')
        # 第一个元素即为薪资下限 第二个元素的数字部分即为薪资上限
        low = float(aw[0])
        # 在第二个元素中判断单位和时间，统一转化为月/万的
        if '万' in aw[1]:
            hight = float(aw[1].split('万')[0])
        elif '千' in aw[1]:
            hight = float(aw[1].split('千')[0])
            hight /= 10
            low /=10
        if '年' in aw[1]:
            hight /= 12
            low /= 12
        # 将完全处理好的数据加入到Excel中
        row = [i[0],i[1],round((hight+low)/2,2),i[3]]
        f_csv.writerow(row)
f.close()
from selenium import webdriver
import csv
from bs4 import BeautifulSoup
urls = []
with open('url.txt','r') as f:
    urls.append(f.readlines())
f = open('movie.csv','a+',encoding='utf-8',newline='')
f_csv = csv.writer(f)
urls = urls[0]
urls = list(map(lambda x:x.replace('\n',''),urls))
driver = webdriver.Chrome(executable_path='D:\PYTHON接单\智联天机\chromedriver.exe')
head = ['电影名','导演','编剧','演员','上映日期','电影类型','时长','评分','人气','地区','语言']
f_csv.writerow(head)
for url in urls:
    driver.get(url)
    name = driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[1]/div[3]/h2/i').text
    star = driver.find_element_by_xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong').text
    hot = driver.find_element_by_xpath('//*[@id="comments-section"]/div[1]/h2/span/a').text
    html = driver.find_element_by_id('info').get_attribute('innerHTML')
    l = str(html).split('<br>')
    l = list(map(lambda i:BeautifulSoup(i.replace('\n','').replace(' ','')).text,l))
    l = [i for i in l if i]
    for i in l:
        o = i.split(':')[0]
        n = i.split(':')[1]
        if o == '导演':
            guide = n
        elif o == '编剧':
            write = n
        elif o == '主演':
            act = n
        elif o == '类型':
            category = n
        elif o == '制片国家/地区':
            place = n
        elif o == '语言':
            language =n
        elif o == '上映日期':
            date = n
        elif o == '片长':
            time = n
    f_csv.writerow([name,guide,write,act,date,category,time,star,hot,place,language])
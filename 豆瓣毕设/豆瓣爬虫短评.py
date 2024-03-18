from selenium import webdriver
import csv
f = open('data.csv','a+',encoding='utf-8',newline='')
f_csv = csv.writer(f)
urls = []
with open('url.txt','r') as f:
    urls.append(f.readlines())
urls = urls[0]
urls = list(map(lambda x:x.replace('\n',''),urls))
driver = webdriver.Chrome(executable_path='D:\PYTHON接单\智联天机\chromedriver.exe')
for i in urls:
    driver.get(i+'/comments?status=P')
    try:
        for j in range(0,500,100):
            driver.get(i + 'comments?start=' + str(j) + '&limit=100&status=P&sort=new_score')
            for k in range(1,101):
                c = driver.find_element_by_xpath('//*[@id="comments"]/div[' + str(k) + ']/div[2]/p/span').text
                try:
                    f_csv.writerow([c])
                except:
                    print(1)
    except:
        print(i)
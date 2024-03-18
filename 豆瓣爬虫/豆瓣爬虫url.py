from selenium import webdriver
driver = webdriver.Chrome(executable_path='D:\PYTHON接单\智联天机\chromedriver.exe')
data = []
for i in range(0,250,25):
    driver.get('https://movie.douban.com/top250?start=' + str(i) + '&filter=')
    for j in range(1,26):
        a = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/ol/li[' + str(j) + ']/div/div[1]/a').get_attribute('href')
        print(a)
        data.append(a+'\n')
f = open('url.txt','w',encoding='utf-8')
f.writelines(data)
f.close()
from selenium import webdriver
import csv
from time import sleep
url = 'https://www.icourse163.org/channel/2001.htm'
driver = webdriver.Chrome(executable_path='D:\PYTHON接单\智联天机\chromedriver.exe')
driver.get(url)
a = driver.find_element_by_xpath('//*[@id="channel-course-list"]/div/div/div[2]/div[2]/div')
pages = a.find_elements_by_tag_name('a')[-2].text
res = []
f = open('结果.csv','w',newline='')
f_csv = csv.writer(f)
for page in range(int(pages)):
    sleep(2)
    for i in range(1,21):
            name = driver.find_element_by_xpath('//*[@id="channel-course-list"]/div/div/div[2]/div[1]/div['+ str(i) +']/div/div[3]/div[1]/h3').text
            school = driver.find_element_by_xpath('//*[@id="channel-course-list"]/div/div/div[2]/div[1]/div[' + str(i) + ']/div/div[3]/div[1]/p').text
            teacher = driver.find_element_by_xpath('//*[@id="channel-course-list"]/div/div/div[2]/div[1]/div[' + str(i) + ']/div/div[3]/div[1]/div').text
            number = driver.find_element_by_xpath('//*[@id="channel-course-list"]/div/div/div[2]/div[1]/div[' + str(i) + ']/div/div[3]/div[2]/span').text
            allHandles1 = driver.window_handles
            # 打开一个详情页
            try:
                driver.find_element_by_xpath('//*[@id="channel-course-list"]/div/div/div[2]/div[1]/div[' + str(i) +']').click()
            except:
                continue
            sleep(2)
            # 再次记录当前所有页面
            allHandles2 = driver.window_handles
            # 通过取差集得到详情页的句柄
            newhandle = [handle for handle in allHandles2 if handle not in allHandles1]
            # 跳转到详情页
            driver.switch_to.window(newhandle[0])
            # 获取所需要的各个信息
            try:
                cate = driver.find_element_by_xpath('//*[@id="j-breadcrumb"]/div/span[2]/a[2]').text
            except:
                cate = ''
            driver.switch_to.window(allHandles1[0])
            f_csv.writerow([name,school,teacher,number,cate])
    driver.find_element_by_xpath('//*[@id="channel-course-list"]/div/div/div[2]/div[2]/div').find_elements_by_tag_name('a')[-1].click()
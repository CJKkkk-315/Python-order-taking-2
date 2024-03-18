from selenium import webdriver
from time import sleep
import csv
# 打开文件
f = open('data.csv','w',encoding='utf-8',newline='')
f_csv = csv.writer(f)
# 写入表头
head = ['车名','价格','过户次数','排量','地区','变速箱','颜色','出厂日期']
f_csv.writerow(head)
# 启动浏览器
driver = webdriver.Chrome(executable_path='chromedriver.exe')
# 访问目标网址
driver.get('https://www.guazi.com/buy')
# 设置爬取页数为20页
for i in range(20):
    try:
        # 每次等待3s让页面加载
        sleep(3)
        # 利用xpath爬取每页20个二手车信息
        for i in range(1,21):
            try:
                row = []
                # 记录当前所有页面
                allHandles1 = driver.window_handles
                # 打开一个二手车详情页
                driver.find_element_by_xpath('//*[@id="pageWrapper"]/div[1]/div[3]/div[2]/div[1]/div[' + str(i) + ']').click()
                # 再次记录当前所有页面
                allHandles2 = driver.window_handles
                # 通过取差集得到详情页的句柄
                newhandle = [handle for handle in allHandles2 if handle not in allHandles1]
                # 跳转到详情页
                driver.switch_to.window(newhandle[0])
                sleep(2)
                # 获取所需要的各个信息
                row.append(driver.find_element_by_xpath('//*[@id="pageWrapper"]/div[1]/div[3]/div[4]/div[2]/h1').text)
                row.append(driver.find_element_by_xpath('//*[@id="pageWrapper"]/div[1]/div[3]/div[5]/ul/li[4]/div').text)
                row.append(driver.find_element_by_xpath('//*[@id="pageWrapper"]/div[1]/div[3]/div[5]/ul/li[5]/div').text)
                row.append(driver.find_element_by_xpath('//*[@id="pageWrapper"]/div[1]/div[3]/div[5]/ul/li[6]/div').text)
                row.append(driver.find_element_by_xpath('//*[@id="pageWrapper"]/div[1]/div[3]/div[5]/ul/li[7]/div').text)
                row.append(driver.find_element_by_xpath('//*[@id="pageWrapper"]/div[1]/div[3]/div[5]/ul/li[8]/div').text)
                row.append(driver.find_element_by_xpath('//*[@id="pageWrapper"]/div[1]/div[3]/div[5]/ul/li[9]/div').text)
                row.append(driver.find_element_by_xpath('//*[@id="pageWrapper"]/div[1]/div[3]/div[5]/ul/li[10]/div').text)
                # 写入文件中
                f_csv.writerow(row)
                # 关闭浏览器
                driver.close()
                # 切换回主页面
                allHandles1 = driver.window_handles
                driver.switch_to.window(allHandles1[0])
    # except处理报错情况
            except:
                # 若报错，则检查详情页是否正确关闭
                allHandles1 = driver.window_handles
                if len(allHandles1) > 1:
                    driver.close()
                allHandles1 = driver.window_handles
                driver.switch_to.window(allHandles1[0])
        driver.find_element_by_xpath('//*[@id="pageWrapper"]/div[1]/div[3]/div[3]/div/button[2]').click()
    except:
        allHandles1 = driver.window_handles
        if len(allHandles1) > 1:
            driver.close()
        allHandles1 = driver.window_handles
        driver.switch_to.window(allHandles1[0])



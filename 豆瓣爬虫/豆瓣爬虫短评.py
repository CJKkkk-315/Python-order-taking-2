from selenium import webdriver
import csv
# 打开data文件,以a+的形式写入文件
f = open('data.csv','a+',encoding='utf-8',newline='')
# 利用csv写入库包装f
f_csv = csv.writer(f)
urls = []
with open('url.txt','r') as f:
    urls.append(f.readlines())
urls = urls[0]
urls = list(map(lambda x:x.replace('\n',''),urls))
# 初始化谷歌浏览器驱动器
driver = webdriver.Chrome(executable_path='chromedriver.exe')
# 遍历每一条链接
for i in urls:
    # 链接后面加上按照评论排序
    driver.get(i+'/comments?status=P')
    try:
        # 每100条评论为一页，爬取5页
        for j in range(0,500,100):
            # 打开对应的评论页
            driver.get(i + 'comments?start=' + str(j) + '&limit=100&status=P&sort=new_score')
            # 爬取每一条评论内容
            for k in range(1,101):
                # 获取文本
                c = driver.find_element_by_xpath('//*[@id="comments"]/div[' + str(k) + ']/div[2]/p/span').text
                try:
                    # 写入csv中
                    f_csv.writerow([c])
                except:
                    #获取失败则跳过
                    print(1)
    # 获取失败则跳过
    except:
        print(i)
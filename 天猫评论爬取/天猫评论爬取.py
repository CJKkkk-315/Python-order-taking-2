from selenium import webdriver
from time import sleep
driver = webdriver.Chrome(executable_path='D:\PYTHON接单\智联天机\chromedriver.exe')
driver.get('https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.6.2a7565a9mSgNHq&id=645328501626&skuId=4806009252274&areaId=330100&user_id=196993935&cat_id=2&is_b=1&rn=982672fe80c286a1563e40530327af4b')
sleep(20)
for i in range(1,21):
    content = driver.find_element_by_xpath('//*[@id="J_Reviews"]/div/div[6]/table/tbody/tr[' + str(i) + ']/td[1]/div[1]/div[1]').text
    print(content)
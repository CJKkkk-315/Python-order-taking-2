from selenium import webdriver
import csv
import _thread
people = []
al = []
with open('hot.csv','r',encoding='utf-8') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        al.append(i[0])
with open('movie(clear).csv','r',encoding='utf-8') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        for j1 in i[1].split('/'):
            people.append(j1)
        for j2 in i[2].split('/'):
            people.append(j2)
        for j3 in i[3].split('/'):
            people.append(j3)
f = open('hot.csv','a+',encoding='utf-8',newline='')
f_csv = csv.writer(f)
names = []
for i in people:
    if i not in names:
        names.append(i)
names1 = []
for i in names:
    if i not in al:
        names1.append(i)
flag = 0
def f(names):
    driver = webdriver.Chrome(executable_path='D:\PYTHON接单\智联天机\chromedriver.exe')
    global flag
    for i in names:
        try:
            print(i)
            driver.get('https://search.douban.com/movie/subject_search?search_text=' + i)
            hot = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div/div/div[2]/div').text
            f_csv.writerow([i,hot])
        except:
            continue
    flag += 1
jnames = [[] for i in range(10)]
for i in range(len(names1)):
  jnames[i%10].append(names1[i])
try:
    for i in jnames:
       _thread.start_new_thread(f, (i,))
except:
   print ("Error: 无法启动线程")
while 1:
   if flag == 10:
       break
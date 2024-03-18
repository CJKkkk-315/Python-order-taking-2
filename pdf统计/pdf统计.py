from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import _thread
import re
import os
import time
import csv
keyword = [['中美贸易战','中美贸易摩擦','中美贸易冲突','中美贸易争端','中美贸易障碍'],
           ['贸易战','贸易摩擦','贸易冲突','贸易争端','贸易障碍'],
           ['中美科技冷战','中美技术冷战'],
           ['科技冷战','技术冷战','科技竞赛'],
           ['中美关系','美中关系']
           ]
f = open('res.csv','a+',encoding='gbk',newline='')
e = open('error.csv','a+',encoding='gbk',newline='')
f_csv = csv.writer(f)
head = ['公司代码','公司名称','年份','第一类','第二类','第三类','第四类','第五类']
f_csv.writerow(head)
def read_from_pdf(file_path):
    with open(file_path,'rb') as file:
        resource_manager = PDFResourceManager()
        return_str = StringIO()
        lap_params = LAParams()
        device = TextConverter(resource_manager,return_str,laparams=lap_params)
        process_pdf(resource_manager,device,file)
        device.close()
        content = return_str.getvalue()
        return_str.close()
        return re.sub('\s+','',content)
ext = 'pdf'
files = os.listdir(os.getcwd()+'\数据文件')
files = [i for i in files if i.split('.')[-1] == ext]
def f(files):
    global flag
    for file in files:
        start = time.time()
        try:
            print(file)
            row = []
            l = file.split('-')
            row.append(l[0])
            row.append(l[1])
            row.append(l[2][:4])
            content = read_from_pdf('数据文件\\' + file)
            for i in keyword:
                n = 0
                for j in i:
                    n += content.count(j)
                row.append(n)
            print(row)
            f_csv.writerow(row)
        except:
            print(file + '（错误文件）')
        elapsed = (time.time() - start)
        print("Time used:", elapsed)
    flag += 1
jdata = [[] for i in range(10)]
for i in range(len(files)):
  jdata[i%10].append(files[i])
flag = 0
try:
    for i in jdata:
       _thread.start_new_thread(f, (i,))
except:
   print ("Error: 无法启动线程")
while 1:
   if flag == 10:
       break
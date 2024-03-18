from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
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
e_csv = csv.writer(e)
f_csv = csv.writer(f)
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
def function1(files):  # 这里是子进程
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
            e_csv.writerow([file])
            print(file + '（错误文件）')
        elapsed = (time.time() - start)
        print("Time used:", elapsed)

def run__process():  # 这里是主进程
    from multiprocessing import Process
    jdata = [[] for i in range(5)]
    for i in range(len(files)):
        jdata[i % 5].append(files[i])
    process = []
    for i in jdata:
       process.append(Process(target=function1, args=(i,)))
    [p.start() for p in process]  # 开启了两个进程
    [p.join() for p in process]   # 等待两个进程依次结束

# run__process()  # 主线程不建议写在 if外部。由于这里的例子很简单，你强行这么做可能不会报错
if __name__ =='__main__':
    run__process()  # 正确做法：主线程只能写在 if内部
import requests
import csv
import json
import _thread
import xlrd
import os
from openpyxl import load_workbook
import re
import time
ext='.xlsx'
ext2='.xls'
ext3='.csv'
files = [f for f in os.listdir() if os.path.isfile(f) and (os.path.splitext(f)[1]==ext or os.path.splitext(f)[1]==ext2 or os.path.splitext(f)[1]==ext3)]
def function(threadName, data):
    global flag
    for i in data:
        try:
            # print(threadName)
            payload = "{'keyword':'" + re.sub('[^0-9]','', str(int(i[0]))) + "','pageNo':1,'pageSize':10,'sortField':'','sortType':''}"
            response = requests.request("POST", url, headers=headers, data=payload)
            js = json.loads(response.text)
            i.append(js['data']['list'][0]['stuName'])
            i.append(js['data']['list'][0]['state'])
            i.append(js['data']['list'][0]['accountNumber'])
        except:
            i.append('')
            i.append('无')
        try:
            f_csv.writerow(i)
            print(i)
        except:
            print(i)
    flag += 1
for file in files:
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)
    data = []
    print(file)
    try:
        x1 = xlrd.open_workbook(file)
        for table in x1.sheets():
            for i in range(table.nrows):
                x = []
                for j in range(table.ncols):
                    x.append(table.cell_value(i, j))
                try:
                    try:
                        x[0] = str(int(x[0]))
                    except:
                        x[0] = re.sub('[^0-9]','', x[0])
                        x[0] = str(int(x[0]))
                except:
                    print(x)
                    continue
                data.append(x)
    except:
        with open(file,'r') as f:
            f_csv = csv.reader(f)
            for x in f_csv:
                try:
                    try:
                        x[0] = str(int(x[0]))
                    except:
                        x[0] = re.sub('[^0-9]','', x[0])
                        x[0] = str(int(x[0]))
                except:
                    print(x)
                    continue
                data.append(x)
    # except:
    #     wb = load_workbook(file)
    #     sheets = wb.worksheets
    #     print(sheets)
    #     for table in sheets:
    #         for row in table.rows:
    #             x = [col.value for col in row]
    #             try:
    #                 try:
    #                     x[0] = str(int(x[0]))
    #                 except:
    #                     x[0] = re.sub('[^0-9]', '', x[0])
    #             except:
    #                 continue
    #             data.append(x)
    #             print(x)
    headers = {
          'authority': 'saleapi.zmlearn.com',
          'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Opera";v="84"',
          'accept': 'application/json, text/plain, */*',
          'content-type': 'application/json;charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'sec-ch-ua-mobile': '?0',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.31',
          'sec-ch-ua-platform': '"Windows"',
          'origin': 'https://www.zmlearn.com',
          'sec-fetch-site': 'same-site',
          'sec-fetch-mode': 'cors',
          'sec-fetch-dest': 'empty',
          'referer': 'https://www.zmlearn.com/',
          'accept-language': 'zh-CN,zh;q=0.9',
          'cookie': 'SSO_TOKEN_KEY=ee7e7a0fc3deae4249d5b294dad7ba8a7f47d177fb401c1e81adce738d3efbd4; JSESSIONID=4F040932486F36E192F5C67063D4A24C; JSESSIONID=6758E839A4598213718177CCC60CF0EA'
        }
    fw = open(file+'.csv','w',newline='')
    jdata = [[] for i in range(30)]
    for i in range(len(data)):
      jdata[i%30].append(data[i])
    f_csv = csv.writer(fw)
    flag = 0
    url = "https://saleapi.zmlearn.com/api/student/user/searchPage?lang=zh-CN&zone=480"

    try:
        for i in jdata:
           _thread.start_new_thread(function, ("Thread-1", i,))
    except:
       print ("Error: 无法启动线程")
    while 1:
       if flag == 30:
           break
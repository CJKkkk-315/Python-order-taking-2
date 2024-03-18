import csv
import pymysql
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='cjk123',
    passwd='123456',
    db='123',
    charset='utf8mb4'
)
cursor = connect.cursor()
data = []
with open('result.csv','r') as f:
    fcsv =csv.reader(f)
    for i in fcsv:
        data.append(i)
for i in data:
    sql = "INSERT INTO position1 (岗位,名称,薪资,城市) VALUES ( '%s', '%s', '%s', '%s' )"
    data = (i[0], i[2], i[3], i[1])
    cursor.execute(sql % data)
    connect.commit()
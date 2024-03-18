import csv
hebei = [i for i in csv.reader(open('hebei.csv',encoding='utf8'))]
henan = [i for i in csv.reader(open('henan.csv',encoding='utf8'))]

# 补充年份信息
hebeif = []
for i in hebei:
    try:
        time = str(int(i[2].split('/')[-3])) + '-' + i[1]
        hebeif.append([i[0],time,i[2]])
    except:
        continue
hebei = hebeif[::]
all = hebei + henan
# 清洗
for i in range(len(all)):
    all[i][0] = all[i][0].replace(' ','').replace('\n','').replace('\'','')
du = []
# 去重 时间筛选
for i in all:
    if int(i[1][:4]) >= 2015:
        if i not in du:
            du.append(i)
all = du[::]

with open('all.csv','w',encoding='utf8',newline='') as f:
    fcsv = csv.writer(f)
    for i in all:
        fcsv.writerow(i)
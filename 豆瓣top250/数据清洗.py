import csv
data = []
with open('movie.csv','r',encoding='utf-8') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        data.append(i)
head = data[0]
data = data[1:]
dataf = []
for i in data:
    name = i[0].replace('的剧情简介','')
    guide = i[1].replace('更多...','')
    write = i[2].replace('更多...','')
    act = i[3].replace('更多...','')
    date = i[4].split('/')[0].split('(')[0]
    category = i[5]
    time = i[6].split('/')[0].split('(')[0]
    star = i[7]
    hot = i[8].replace('全部 ','').replace(' 条','')
    place = i[9]
    language = i[10]
    dataf.append([name,guide,write,act,date,category,time,star,hot,place,language])
with open('movie(clear).csv','w',encoding='utf-8',newline='') as f:
    f_csv = csv.writer(f)
    for i in dataf:
        f_csv.writerow(i)
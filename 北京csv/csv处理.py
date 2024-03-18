import csv
d = {i:0 for i in range(1,13)}
with open('beijing2018(1).csv') as f:
    fcsv = csv.DictReader(f)
    for i in fcsv:
        if int(i['AQI']) <= 50:
            d[int(i['Date'].split('/')[1])] += 1
head = ['Mouth','Good']
with open('result.csv','w',newline='') as f:
    fcsv = csv.writer(f)
    fcsv.writerow(head)
    l = sorted([[i,j] for i,j in d.items()])
    for i in l:
        fcsv.writerow(i)

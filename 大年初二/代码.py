import csv
data = []
head = ['CountyName','CountyFIPScode','StateName','TotalCases','TotalDeath','LastReportedDate']
with open('us-counties.csv','r') as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        data.append(row)
data = data[1:][::-1]
d = {}
for i in data:
    if i[3] not in d:
        d[i[3]] = [i[1],i[3],i[2],i[4],i[5],i[0]]
with open('res.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(head)
    for row in d.values():
        f_csv.writerow(row)


import csv
m = {}
with open('cc_info.csv','r') as f:
    fcsv = csv.reader(f)
    for i in fcsv:
        try:
            m[i[0]] = float(i[4])
        except:
            continue
x = {}
with open('transactions.csv','r') as f:
    fcsv = csv.reader(f)
    for i in fcsv:
        try:
            if i[0] in x:
                x[i[0]][int(i[1][5:7])].append([float(i[2]),int(i[1][8:10])])
            else:
                x[i[0]] = [[] for _ in range(12)]
                x[i[0]][int(i[1][5:7])] = [[float(i[2]),int(i[1][8:10])]]
        except:
            continue
nx = {i:j[::] for i,j in x.items()}
for i in x.keys():
    for j in range(len(x[i])):
        if x[i][j]:
            x[i][j] = round(sum([t[0] for t in x[i][j]]),2)
        else:
            x[i][j] = 0
res = []
neg = []
del x['credit_card']
for i in x.keys():
    flag = 0
    for j in x[i]:
        if j > m[i]:
            neg.append(i)
            flag = 1
            break
    if not flag:
        res.append(i)
# print(len(x))
# print(len(res))
# print(len(neg))
for i in res:
    print(i)
for i in nx.keys():
    for j in range(len(nx[i])):
        nx[i][j] = sorted(nx[i][j],key=lambda x:x[1])
bom = [[[] for i in range(31)] for j in range(12)]
for i in neg:
    num = m[i]
    for j in range(len(nx[i])):
        for k in nx[i][j]:
            num -= k[0]
            if num < 0:
                bom[j][k[1]-1].append(i)
                break
# for i in range(len(bom)):
#     for j in range(len(bom[i])):
#         print(len(bom[i][j]),i,j)
mouth = int(input('请输入月份：'))
day = int(input('请输入日期：'))
for i in bom[mouth-1][day-1]:
    print(i)
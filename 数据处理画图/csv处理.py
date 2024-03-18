import math
import matplotlib.pyplot as plt
def changegrid(gridRD):
    lat = int(gridRD[2:4])
    lon = int(gridRD[4:])
    if gridRD[0] == '6':
        lat += 2.5
        lon += 2.5
    else:
        lat += 0.5
        lon += 0.5
    if gridRD[1] == '2':
        lat = -lat
    return [lat,lon]
import csv
all = []
data = []
gridRD = []
year = {}
mouth = {}
with open('IOTC-2019-WPTmT07-DATA04 - CELL.csv') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        if i[16]:
            all.append(i)
all = all[1:]
for i in all:
    if int(i[2])>= 2003:
        try:
            year[int(i[2])].append(float(i[16]))
        except:
            year[int(i[2])] = [float(i[16])]
        try:
            mouth[int(i[3])].append(float(i[16]))
        except:
            mouth[int(i[3])] = [float(i[16])]
        ll = changegrid(i[6])
        data.append([int(i[2]), int(i[3]), i[7], i[9], i[15], float(i[16]),ll[0],ll[1]])
yeardata = []
for i,j in year.items():
    yeardata.append([i,sum(j)/len(j)])
yeardata.sort()
x = [str(i[0])for i in yeardata]
y = [i[1] for i in yeardata]
plt.plot(x,y)
plt.xticks(rotation=30)
plt.show()
mouthdata = []
for i,j in mouth.items():
    mouthdata.append([i,sum(j)/len(j)])
mouthdata.sort()
x = [str(i[0]) for i in mouthdata]
y = [i[1] for i in mouthdata]
plt.plot(x,y)
plt.show()
print(data)
for i in range(len(data)):
    data[i].append(int((data[i][6] + 45)//5))
    data[i].append(int((data[i][7] - 20)//5))
table = [[[] for i in range(26)] for j in range(14)]
for i in data:
    table[i[8]][i[9]].append(i[5])
for i in range(len(table)):
    for j in range(len(table[0])):
        if table[i][j]:
            table[i][j] = (round(sum(table[i][j])/len(table[i][j]),2),i*5-45+2.5,j*5+20+2.5)
        else:
            table[i][j] = (0,i*5-45+2.5,j*5+20+2.5)
table = table[::-1]
print(len(table))
print(len(table[0]))
table1 = []
for i in table:
    table1 += i
print(table1)

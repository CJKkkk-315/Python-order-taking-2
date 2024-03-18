import netCDF4
import csv
from netCDF4 import Dataset
import numpy as np
nc_obj201701 = Dataset('mercatorfreebiorys2v4_global_mean_201701.nc')
lat=(nc_obj201701.variables['longitude'][:])
longitude = np.array(nc_obj201701.variables['longitude'][:]).tolist()
latitude = np.array(nc_obj201701.variables['latitude'][:]).tolist()
chl = np.array(nc_obj201701.variables['chl'][:])[0][0:,140:420,800:1320]
slat = longitude[800:1320]
slon = latitude[140:420]
data = [[0 for _ in range(520)] for _ in range(280)]
for i in range(520):
    for j in range(280):
        data[j][i] = [chl[k][j][i] for k in range(1) if chl[k][j][i] < 200]
        try:
            data[j][i] = round(sum(data[j][i])/len(data[j][i]),4)
        except:
            data[j][i] = 'nan'
for i in range(len(data)):
    x = []
    for j in range(0,len(data[i]),20):
        x.append(data[i][j:j+20])
    data[i] = x[::]

table = [[[] for i in range(26)] for j in range(14)]
for i in range(0,len(data),20):
    for j in range(len(data[0])):
        s = []
        for k in range(20):
            s += data[i+k][j]
        table[i//20][j] = s[::]
for i in range(len(table)):
    for j in range(len(table[0])):
        table[i][j] = [k for k in table[i][j] if k != 'nan']
        try:
            table[i][j] = round(sum(data[i][j]) / len(data[i][j]), 4)
        except:
            table[i][j] = 'nan'
with open('mercatorfreebiorys2v4_global_mean_201701.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in table:
        f_csv.writerow(i)



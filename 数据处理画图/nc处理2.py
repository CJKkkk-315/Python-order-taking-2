import netCDF4
import csv
from netCDF4 import Dataset
import numpy as np
nc_obj201701 = Dataset('erdMH1chlamday_1a08_1fd9_532a.nc')
longitude = np.array(nc_obj201701.variables['longitude'][:]).tolist()
latitude = np.array(nc_obj201701.variables['latitude'][:]).tolist()
chl = np.array(nc_obj201701.variables['chlorophyll'][:])[0]
for i in chl:
    for j in i:
        print(j)
table = [[[] for i in range(26)] for j in range(14)]
for i in range(0,len(chl)):
    for j in range(len(chl[0])):
        table[int((latitude[i] + 45)//5)][int((longitude[j] - 20)//5)].append(chl[i][j])

for i in range(len(table)):
    for j in range(len(table[0])):
        table[i][j] = [k for k in table[i][j] if k != 'nan']
        try:
            table[i][j] = round(sum(table[i][j]) / len(table[i][j]), 4)
        except:
            table[i][j] = 'nan'
table = table[::-1]
with open('erdMH1chlamday_1a08_1fd9_532a.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in table:
        f_csv.writerow(i)



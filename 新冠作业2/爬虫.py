import requests
import csv

import json


def shellSort(arr):
    n = len(arr)
    gap = int(n / 2)
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap][1] > temp[1]:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = int(gap / 2)
response = requests.get('https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=VaccineSituationData')
js = json.loads(response.text)
data = []
m = []
for i in js['data']['VaccineSituationData']:
    data.append([i['country'],i['total_vaccinations_per_hundred']])
    m.append(i['total_vaccinations_per_hundred'])
shellSort(data)
print('每百人接种数最大值为：',max(m))
print('每百人接种数最小值为：',min(m))
print('每百人接种数平均值为：',round(sum(m)/len(m),2))
with open('排序.csv','w',encoding='gbk',newline='') as f:
    f_csv = csv.writer(f)
    for i in data:
        f_csv.writerow(i)



import openpyxl
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
plt.rcParams['font.sans-serif']=['simhei']
plt.rcParams['axes.unicode_minus'] = False
style.use('ggplot')
wb = openpyxl.load_workbook(r"名单.xlsx")
ws = wb['Sheet1']
num = []
name = []
temp = []
temp_name = []
f_name = []
for each_row in ws.iter_rows(min_row=0, min_col=0, max_row=38, max_col=3):
    name.append(each_row[1].value)
for each in name:
    temp_name.append(each[0])
del temp_name[0]
temp = dict(Counter(temp_name))
for n,value in temp.items():
    num.append(value)
    f_name.append(n)
for i in range(len(f_name)):
    if f_name[i] == '徐':
        num.insert(0, num[i])
        f_name.insert(0, f_name[i])
        del num[i+1]
        del f_name[i+1]
        break
x_labels = f_name
x_value = num
x = range(len(x_value))
plt.bar(x, x_value)
plt.xticks(x, x_labels, fontsize=15)
plt.show()
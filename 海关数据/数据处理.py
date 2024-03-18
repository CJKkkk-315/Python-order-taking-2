data = []
with open('数据文件1.txt',encoding='utf8') as f:
    for i in f.readlines():
        n = i.replace('\n','').split('，')
        data.append(n)
head = data[0]
data = data[1:]
def clean(data):
    for i in range(len(data)):
        for j in range(1,len(data[i])):
            data[i][j] = float(data[i][j].replace(' ','').replace(',',''))
clean(data)
for i in range(1,7):
    aw = []
    for row in data:
        aw.append([row[0],row[i]])
    aw.sort(reverse=True,key=lambda x:x[1])
    print(head[i],'排序前五为:',aw[:5])
for i in range(len(data)):
    print('编号：',i+1,data[i][0])
code = input('请输入5个特区编号,空格分隔：').split()
inout = []
posi = []
neg = []
for i in range(len(data)):
    if str(i+1) in code:
        inout.append(data[i][1])
    if data[i][4] > 0:
        posi.append(data[i][4])
    else:
        neg.append(data[i][4])

print('进出口额最大为',max(inout))
print('进出口额最小为',min(inout))
print('同期进出口比正值：',posi)
print('同期进出口比负值',neg)

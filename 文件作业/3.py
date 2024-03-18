n = int(input('表示冒号固定位置的整数为：'))
data = []
with open('listin.txt','r') as f:
    for i in f.readlines():
        data.append([i.replace('\n','').split(':')[0].split(' '),i.replace('\n','').split(':')[1].split(' ')])
dataf = []
for i in data:
    a = ' '.join([j.replace('\t','') for j in i[0] if j])
    b = ' '.join([j.replace('\t','') for j in i[1] if j])
    dataf.append([a,b])
print(dataf)
f = open('listout.txt','w')
for i in dataf:
    t = n-len(i[0])
    a = ' '*t + i[0]
    f.write(a + ' : ' + i[1] + '\n')

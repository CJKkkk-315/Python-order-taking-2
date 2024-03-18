with open('in.txt','r') as f:
    a = f.readlines()
b = []
for i in range(len(a)):
    b.append(a[i].replace('\n','').split('\t'))
res = []
for i in range(len(b)):
    a = []
    for j in b[i]:
        if '.' in j:
            a.append(float(j))
        else:
            a.append(int(j))
    t1 = max(a)
    t2 = min(a)
    res.append([str(t1),str(t2)])
with open('out.txt','w') as f:
    for i in res:
        f.write('  '.join(i)+'\n')
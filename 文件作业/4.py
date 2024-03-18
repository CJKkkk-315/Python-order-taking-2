with open('filein.c','r') as f:
    r = f.readlines()
r1 = []
for i in r:
    r1.append(i.replace('\n',''))
st = ' '.join(r1)
c = 0
f = 0
while f + 1 < len(st):
    f += 1
    if st[f] == '*' and st[f-1] == '/':
        f += 1
        while True:
            if st[f] == '*' and st[f+1] == '/':
                break
            c = c + 1
            f = f + 1
res = int(c)/len(st)*100
print(str(int(res))+'%')

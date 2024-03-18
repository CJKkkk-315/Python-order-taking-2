r = []
while True:
    t = input()
    try:
        a = t.split(' ')[0]
        b = int(t.split(' ')[1])
        r.append([a,b])
    except:
        break
r.sort(key=lambda x:x[1])
r = r[::-1]
f = open('result.txt','w',encoding='utf-8')
f.write(r[0][0] + '\n')
f.write(r[1][0] + '\n')
f.write(r[2][0] + '\n')
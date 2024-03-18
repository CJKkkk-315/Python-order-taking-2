l = []
while True:
    try:
        l.append(int(input()))
    except:
        break
print(max(l))
print(min(l))
print(l[((len(l)+1)//2)-1])
print(' '.join(list(map(str,sorted(l,reverse=True)))))
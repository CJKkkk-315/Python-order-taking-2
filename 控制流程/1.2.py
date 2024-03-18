ans = input('Enter your eaxm answers:')
r = 'adbdcacbdac'
s = 0
e = 0
t = ''
for i in range(len(r)):
    if r[i] != ans[i]:
        t += 'X'
        e += 1
    else:
        t += r[i]
        s += 9
print('Your missed ' + str(e) + ' questions:' + t)
print('Your score is:' + str(s) + ' percent')


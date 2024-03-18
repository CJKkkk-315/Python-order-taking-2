s = 0
n = 1
while True:
    s = s + n
    n = n + 1
    if s > 4000:
        break
print("n={},s={}".format(n,s))
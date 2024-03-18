import random
data = [random.randint(1000000000,9999999999) for _ in range(20)]
print(data)
data = [data[i] for i in range(len(data)) if i%2 == 0]
data.insert(0,2011321132)
for i in range(len(data)):
    for j in range(len(data)-1-i):
        if data[j] > data[j+1]:
            data[j],data[j+1] = data[j+1],data[j]
print(data)

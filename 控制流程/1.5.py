import matplotlib.pyplot as plt
b = 10000
y = []
x = []
for i in range(2021,2041):
    b *= 1.05
    x.append(i)
    y.append(round(b,2))
for i,j in zip(x,y):
    print(i,end='  ')
    print(j,end='  ')
    print('\n')
plt.plot(x,y)
plt.show()
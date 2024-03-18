import matplotlib.pyplot as plt
import random
color = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
data = [[random.randint(1,100),random.randint(1,100),'#'+''.join(random.sample(color,6))] for i in range(100)]
a = [i[0] for i in data]
b = [i[1] for i in data]
c = [i[2] for i in data]
plt.scatter(a,b,c=c)
plt.show()
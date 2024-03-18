import matplotlib.pyplot as plt
import random
number_of_colors = 100
color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
for i in range(number_of_colors):
   plt.scatter(random.randint(0, 1000), random.randint(0,1000), c=color[i])
plt.show()
import numpy as np
import matplotlib.pyplot as plt

results = {"物理": 79, "英语": 86, "形势与政策": 88, "模拟电子电路": 80, "工程训练": 90,'电子实验':85}
data_length = len(results)
angles = np.linspace(0, 2*np.pi, data_length, endpoint=False)
labels = [key for key in results.keys()]
score = [v for v in results.values()]
score_a = np.concatenate((score, [score[0]]))
angles = np.concatenate((angles, [angles[0]]))
labels = np.concatenate((labels, [labels[0]]))
fig = plt.figure(figsize=(8, 6), dpi=100)
plt.rcParams['font.sans-serif'] = ['SimHei']
ax = plt.subplot(111, polar=True)
ax.plot(angles, score_a)
ax.set_thetagrids(angles*180/np.pi, labels)
ax.set_rlim(0, 100)
ax.set_rlabel_position(270)
plt.show()
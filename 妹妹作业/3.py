import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False
courses = ['六级', '电工电子学', '大学物理', '物理实验', '劳动教育', '体育']
scores = [91, 90, 89, 84, 90, 67]
dataLength = len(scores)
angles = np.linspace(0, 2*np.pi, dataLength, endpoint=False)
courses.append(courses[0])
scores.append(scores[0])
angles = np.append(angles, angles[0])
plt.polar(angles,
          scores,
          'gv--',
          linewidth=2)
plt.thetagrids(angles*180/np.pi, courses, fontsize=13)
plt.fill(angles, scores, facecolor='y', alpha=0.2)
plt.show()

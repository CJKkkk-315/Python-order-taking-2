import matplotlib.pyplot as plt
import csv
# 定义岗位对应的顺序，为后面数据装入city_dic做准备
posi_dic = {'JAVA开发工程师':0,'PYTHON开发工程师':1,'C++开发工程师':2,'前端工程师':3,'软件测试工程师':4,'Android开发工程师':5,'算法工程师':6,'Linux工程师':7,'数据工程师':8}
# 定义城市字典，该字典键名为城市名称，对应的值为一个装有9个空列表的列表
city_dic = {'北京':[[] for _ in range(9)],'上海':[[] for _ in range(9)],'广州':[[] for _ in range(9)],'深圳':[[] for _ in range(9)],'武汉':[[] for _ in range(9)],'杭州':[[] for _ in range(9)],'福州':[[] for _ in range(9)],'厦门':[[] for _ in range(9)]}
# 打开清洗后的数据
result = []
with open('result.csv') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        result.append(i)
for row in result:
    city_dic[row[3]][posi_dic[row[0]]].append(float(row[2]))
def show(posi):
    # 每次执行前先清空画布，避免图片在上一次的画布上重叠
    plt.clf()
    # 根据函数输入的岗位，定位到数据存储在字典的第几列表中
    n = posi_dic[posi]
    # 设置x轴，以及平均薪资图和最大薪资图的y轴
    x,y,ymax = [],[],[]
    # 遍历字典的键值对
    for i,j in city_dic.items():
        # 不需要总体数据 跳过
        if i == '总体':
            continue
        # 将城市名装入x轴中，对应城市名列表中的对应岗位列表的平均值和最大值分别装入y和ymax
        x.append(i)
        y.append(round(sum(j[n])/len(j[n]),2))
        ymax.append(max(j[n]))
    aw1 = []
    aw2 = []
    for i,j,k in zip(x,y,ymax):
        aw1.append([i,j])
        aw2.append([i,k])
    aw1.sort(key=lambda x:x[1])
    aw2.sort(key=lambda x:x[1])
    x = [i[0] for i in aw1]
    y = [i[1] for i in aw1]
    xmax = [i[0] for i in aw2]
    ymax = [i[1] for i in aw2]
    # 同总体概览可视化
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.subplot(3, 1, 1)
    plt.title(posi + '平均薪资')
    plt.bar(x, y)
    plt.ylabel('岗位平均薪资（单位：万）')
    plt.subplot(3, 1, 3)
    plt.title(posi + '最高薪资')
    plt.bar(xmax, ymax)
    plt.ylabel('岗位最高薪资（单位：万）')
    plt.show()
for i in posi_dic.keys():
    show(i)
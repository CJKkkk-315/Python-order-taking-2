import snownlp
import csv
import matplotlib.pyplot as plt
contents = []
# 以读模式读取爬取好的所有评论内容
with open('content.csv','r',encoding='utf8') as f:
    fcsv = csv.reader(f)
    for i in fcsv:
        # 将其全部添加到content的列表中
        contents.append(i[0])
# 由于评论数据较大，截取前5000条作为分析
contents = contents[:5000]
# 定义列表，分别表示消极，中性，积极的评论
res = [0,0,0]
# 循环遍历每一条评论
for content in contents:
    try:
        # 利用snownlp算法对评论文本内容进行分析
        sn = snownlp.SnowNLP(content)
        # 分析完毕后，提取情感得分
        snv = sn.sentiments
        # 如果情感得分大于0.7，则认为是积极评论
        if snv > 0.7:
            res[2] += 1
        # 若小于0.3，则认为是消极评论
        elif snv < 0.3:
            res[0] += 1
        # 否则认为是中性评论
        else:
            res[1] += 1
    except:
        continue
# 添加label数组定义标签
label = ['bad','mid','good']
# 绘制柱状图
plt.bar(label,res)
# 展示
plt.show()

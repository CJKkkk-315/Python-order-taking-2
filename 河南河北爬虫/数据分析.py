import snownlp
from pyecharts.charts import *
from pyecharts import options as opts
from collections import Counter
import jieba
import csv
data = [i for i in csv.reader(open('all.csv','r',encoding='utf8'))]
# 发布频率分析

day = {}
for i in data:
    day[i[1]] = day.get(i[1],0) + 1
fre = sum([i for i in day.values()])/len(day)
print(f'平均发布频率为{round(fre,2)}条/天')

# 分词
object_list = []
with open('停用词库.txt', 'r', encoding='UTF-8') as meaninglessFile:
    stopwords = set(meaninglessFile.read().split('\n'))
stopwords.add(' ')
for i in data:
    seg_list_exact = jieba.cut(i[0], cut_all=False, HMM=True)
    for word in seg_list_exact:
        if word not in stopwords:
            object_list.append(word)
object_list = Counter(object_list)
# 高频词分析
xy = sorted(object_list.items(),key=lambda x:x[1],reverse=True)
print(xy)
x = [i[0] for i in xy[:10]]
y = [i[1] for i in xy[:10]]
bar1 = (
    Bar()
        .add_xaxis(x)
        .add_yaxis("出现次数", y, yaxis_index=0, )
        .extend_axis(yaxis=opts.AxisOpts())
        .set_global_opts(title_opts=opts.TitleOpts(title="高频词分析"))
)
bar1.render('高频词分析.html')
# 词云分析
wordcloud = (
    WordCloud()
            .add('',[(i,j) for i,j in object_list.items()],word_size_range=[20, 50], shape="diamond", word_gap=10)
            .set_global_opts(title_opts=opts.TitleOpts(title="词云图"))
)
wordcloud.render('词云图.html')

# 情感分析
label = ['负向','中性','正向']
res = [0,0,0]
head = ['','负向','中性','正向']
csvres = []
for i in data:
    s = snownlp.SnowNLP(i[0])
    score = s.sentiments
    csvres.append([i[0],score])
    if score > 0.7:
        res[2] += 1
    elif score < 0.3:
        res[0] += 1
    else:
        res[1] += 1
pie = (
        Pie(init_opts=opts.InitOpts(width='1440px', height='800px'))
            .add(series_name='', data_pair=[(i, j) for i, j in zip(label, res)])
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
    )
pie.render('情感分析.html')
with open('情感分析结果.csv','w',newline='',encoding='utf8') as f:
    fcsv = csv.writer(f)
    fcsv.writerow(head)
    fcsv.writerow(['number']+res)
    fcsv.writerow(['percentage'] + [i/sum(res) for i in res])
with open('情感分析.csv','w',newline='',encoding='utf8') as f:
    fcsv = csv.writer(f)
    for i in csvres:
        fcsv.writerow(i)
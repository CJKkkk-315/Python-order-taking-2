# -*- coding: utf-8 -*-
import wordcloud
import matplotlib.pyplot as plt
import numpy
from PIL import Image
from collections import Counter
import jieba
object_list = []
data = ['''
河北农业大学是河北省人民政府与教育部、农业农村部、国家林业和草原局分别共建的省属重点骨干大学，国家大众创业万众创新示范基地，全国深化创新创业教育改革示范高校，教育部卓越工程师、卓越农林人才教育培养计划实施高校，河北省“双一流”建设高校。
学校创建于1902年，是我国最早实施高等农业教育的院校之一，河北省建立最早的高等院校，先后经历了直隶农务学堂、直隶高等农业学堂、直隶公立农业专门学校、河北省立农学院、河北农学院、河北农业大学等历史时期。20世纪50年代，学校的森林系、畜牧兽医系、农田水利系分别整建制参与组建了北京林学院（现北京林业大学）、内蒙古畜牧兽医学院（现内蒙古农业大学）、武汉水利学院（现与武汉大学合并）。1995年与原河北林学院合并组建为新的河北农业大学。2000年原河北水产学校、原河北畜牧科技学校并入河北农业大学。
百年积淀，学校形成了鲜明的办学特色。坚持“农业教育非实习不能得真谛，非试验不能探精微，实习试验二者不可偏废”的教学原则，秉承“崇德、务实、求是”的校训，开创了享誉全国的“太行山道路”，培育了“艰苦奋斗、甘于奉献、求真务实、爱国为民”的“太行山精神”，多次受到党和国家的肯定与表彰，成为高等教育的一面旗帜。先后培养毕业生40多万名，涌现出了一批批兴业英才、学术骨干、管理才俊，如董玉琛、刘旭、杨志峰、赵春江、郭子建等11名院士，君乐宝集团创始人魏立华，全球青年领袖石嫣等。2016年，习近平总书记对李保国同志先进事迹作出重要批示，称赞他是新时期共产党人的楷模，知识分子的优秀代表，太行山上的新愚公。
''']
for i in data:
    i.replace('\n','')
    #对每一行内容，进行jieba分词处理，模式选择精确分词模式
    seg_list_exact = jieba.cut(i, cut_all=False, HMM=True)
    with open('停用词库.txt', 'r', encoding='UTF-8') as meaninglessFile:
        stopwords = set(meaninglessFile.read().split('\n'))
    stopwords.add(' ')
    #打开停用词文件，将分词成果去掉所有的停用词
    for word in seg_list_exact:
        if word not in stopwords:
            object_list.append(word)
# 统计词语出现频率
object_list = Counter(object_list)
# 选择词云背景图
mask = numpy.array(Image.open('heart.png'))
# 设置词云参数
wc = wordcloud.WordCloud(
    font_path = 'C:/Windows/Fonts/simfang.ttf',
    background_color='white',
    mask = mask,
    max_words = 500,
    max_font_size = 120
)
# 生成词云对象
wc.generate_from_frequencies(Counter(object_list))
wc.recolor(color_func=wordcloud.ImageColorGenerator(mask))
plt.figure('词云')
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
# 显示词云
plt.show()
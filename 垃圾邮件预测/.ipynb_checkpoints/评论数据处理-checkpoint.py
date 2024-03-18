import re
import jieba
import pandas as pd
# 去掉非中文字符
def clean_str(string):
    string = re.sub(r"[^\u4e00-\u9fff]", " ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip()
# 读取xlsx评论表格
df = pd.read_excel('产品评价.xlsx')
data = df.values.tolist()
# 分别将评论内容和好差评标签存入txt文件中
f1 = open('content.txt','w',encoding='utf-8')
f2 = open('labels.txt','w',encoding='utf-8')
for i in data:
    f1.write(clean_str(i[1])+'\n')
    f2.write(str(i[2])+'\n')
f1.close()
f2.close()
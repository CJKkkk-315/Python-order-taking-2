import pandas as pd
df = pd.read_csv('花名册.csv',encoding='gbk')
df = df.values.tolist()
for i in range(len(df)):
    if df[i][1] == '叶宇辰':
        df = df[i-3:i+4] + df[:i-3] + df[i+4:]
for i in df:
    print(i)
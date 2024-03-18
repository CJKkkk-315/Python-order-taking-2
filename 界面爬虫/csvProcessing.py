import pandas as pd
import numpy as np
import tkinter as tk
def dataProcess():
    filename = r'中国大学排行榜2021.csv'
    df = pd.read_csv(filename, encoding='ansi')
    df['星级排名'] = df['星级排名'].str.replace('★', '').astype("int32")
    df['综合得分'] = df['综合得分'].apply(lambda x: np.NAN if str(x).isspace() else x)
    df1 = df.dropna()
    dict1 = {}
    dict1 = df1[['名次', '综合得分']].set_index('名次').to_dict(orient='dict')['综合得分']
    m = ''
    for i in range(1, len(df)):
        if pd.isnull(df['综合得分'][i]):
            m = dict1.get(int(df['名次'][i]), 60)
            df['综合得分'][i] = m
    df.to_csv('处理后数据1.csv', encoding='ansi')
    tk.messagebox.showinfo('保存文件', '文件：处理后数据1.csv保存成功！')
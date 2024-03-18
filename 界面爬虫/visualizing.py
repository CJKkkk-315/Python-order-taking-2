import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def dataView():
    filename = r'处理后数据1.csv'
    df = pd.read_csv(filename, encoding='ansi', index_col='名次')
    schoolCount = df.groupby('所在地区').count()
    schoolCount['学校名称'].plot(kind='bar')
    plt.savefig('tu1.jpg')
    plt.clf()
    schoolCount = df.groupby('办学层次').count()
    print(schoolCount)
    schoolCount['学校名称'].plot(kind='pie')
    plt.savefig('tu2.jpg')

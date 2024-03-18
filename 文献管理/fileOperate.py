import os
import pandas as pd


# 写入文件
def writeToCsv(infoDatas,path):
    df = pd.DataFrame(infoDatas)
    df.to_csv(path, header=0, index=0, encoding="utf-8", mode="a")

# 判断搜索类型，返回所需存储路径
def judgeSearchType(searchType,question):
    path="./dataBase"
    return os.path.join(path,f"{searchType}Dir/{question}.csv")

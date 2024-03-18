import numpy as np
import pandas as pd
hmc = pd.read_excel("名单.xlsx", usecols=['序号', '姓名', '学号'])
outputpath = 'data.csv'
hmc.to_csv(outputpath,sep=',',index=False,header=True)

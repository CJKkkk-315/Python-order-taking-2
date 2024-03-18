import csv
import pandas as pd
import glob
import time
import pandas as pd
import numpy as np

from shapely import geometry#判断空间坐标
from jenkspy import jenks_breaks #数据分段
from matplotlib import colors,cm #自定义色彩

##简单的数据处理------------------------------------------------------------------------------------------------------------------------------------------
#为表格加上表头
# df = pd.read_csv('F:\\\\BaiduNetdiskDownload\\\\result_data\\\\train.csv',header=None,nrows=100000,names=[
#     'LoadingOrder','carrierName','timestamp','longitude','latitude','vesselMMSI','speed','direction'
#     ,'veseelNextport','vesselNextportETA','vesselStatus','vesselDatasource','TRANSPORT_TRACE'])
# df.to_csv('F:\\\\2020--master\\\\BDC2020无能万金油-复赛\\\\data\\\\train0623.csv',index=False)

# 按照订单号的首字母分成26个文件
# pd.set_option('display.max_columns', None)
# letter_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
#                'V', 'W', 'X', 'Y', 'Z']
#
# columns = ['LoadingOrder', 'carrierName', 'timestamp', 'longitude',
#            'latitude', 'vesselMMSI', 'speed', 'direction', 'veseelNextport',
#            'vesselNextportETA', 'vesselStatus', 'vesselDatasource', 'TRANSPORT_TRACE']
#
# df = pd.read_csv('F:\\\\BaiduNetdiskDownload\\\\result_data\\\\train.csv', chunksize=1000000)
# count = 1
# for chunk in df:
#     print(count)
#     count += 1
#     chunk.columns = columns
#     for i in range(0, 26):
#         df_mid = chunk[chunk['LoadingOrder'].str.startswith(letter_list[i])]
#         df_mid.to_csv('F:\\\\BaiduNetdiskDownload\\\\result_data\\\\separate_data\\\\separate_data\\\\' + letter_list[i] + '.csv', mode='a', index=False, header=False)

# 并将我们选中的数据进行去重，最后将数据按照订单和出发时间排序，
# count = 0
# for i in range(len(letter_list)):
#     df = pd.read_csv('F:\\\\BaiduNetdiskDownload\\\\result_data\\\\separate_data\\\\separate_data\\\\' + letter_list[i] + '.csv')
#     df.columns = columns
#     df.drop_duplicates(subset=columns, keep='first', inplace=True)
#     df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%dT%H:%M:%S')
#     df.sort_values(by=['LoadingOrder', 'timestamp'], inplace=True)
#     count += df.shape[0]
#     print(i, count)
#     df.to_csv('separate_data/' + letter_list[i] + '.csv', index=False)

# #合并多个子文件
# letter_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
#                'V', 'W', 'X', 'Y', 'Z']
# for i in range(len(letter_list)):
#     df = pd.read_csv('F:\\\\BaiduNetdiskDownload\\\\result_data\\\\separate_data\\\\'+ letter_list[i] +'.csv')
#     df.to_csv('F:\\\\BaiduNetdiskDownload\\\\result_data\\\\train.csv', index=False, header=False, mode='a')


#----------------------------------------------------------------------------------------------------------------------------------------------
import geopandas as gpd
import matplotlib.pyplot as plt
from itertools import islice

# #简单的做出我们想要的路线的可视化路线
# df_trace =  pd.read_csv('F:\\\\BaiduNetdiskDownload\\\\result_data\\\\separate_data\\\\A.csv')
# df_trace.columns= ['LoadingOrder','carrierName','timestamp','longitude','latitude','vesselMMSI','speed','direction'
#         ,'veseelNextport','vesselNextportETA','vesselStatus','vesselDatasource','TRANSPORT_TRACE']
# df_trace.head()
#
# df_trace_ = df_trace[df_trace.TRANSPORT_TRACE=='CNYTN-MXZLO'] #获取我们想要画的轨迹
# gdf_ = gpd.GeoDataFrame(df_trace_, geometry=gpd.points_from_xy(df_trace_.longitude, df_trace_.latitude))
#
# world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))#用包画世界地图# ax = world.plot(color='white', edgecolor='black',figsize=(20,20))   自定义地图的样子
# fig,ax = plt.subplots(1, 1)    #自定义按照包内部数据根据column的类别画地图
# world.plot(column= 'pop_est', ax=ax, legend=True)
# gdf_.plot(ax=ax, color='red',markersize=1)#规定点的颜色
# plt.show()


# #画出全世界的港口位置点。
# df_port =  pd.read_csv('F:\\\\BaiduNetdiskDownload\\\\result_data\\\\port_data.csv')
# df_port.columns= ['TRANS_NODE_NAME','LONGITUDE','LATITUDE']
# df_port.head()
#
# df_port_ = df_port[df_port.TRANS_NODE_NAME!=' ']
# gdf_ = gpd.GeoDataFrame(df_port_, geometry=gpd.points_from_xy(df_port_.LONGITUDE, df_port_.LATITUDE))
#
# world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
# ax = world.plot(color='white', edgecolor='black',figsize=(20,20))#自定义地图的样子
# gdf_.plot(ax=ax, color='red',markersize=1)
# plt.show()
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#将全世界分为若干分块，并计算每个分块的港口数量

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#画出船运轨迹花费的速度与时间空间有关系的折线图

#获取列表唯一值
# lin=[]
# for m in range(test_df.shape[0]):
#     if test_df.TRANSPORT_TRACE[m] == 'CNYTN-MXZLO':
#         xinxi=test_df.LoadingOrder[m]
#         lin.append(xinxi)
# set_res=set(lin)
# list_res = (list(set_res))
# for item in list_res:
#     print(item)

# 对A的解读
#test_df=pd.read_csv('F:\\\\BaiduNetdiskDownload\\\\result_data\\\\separate_data\\\\A.csv')#, chunksize=100000
# print('总共有{}艘船'.format(test_df.vesselMMSI.nunique()))
# print('{}个快递运单'.format(test_df.LoadingOrder.nunique()))
# print('{}个运货公司'.format(test_df.carrierName.nunique()))
# print('{}条运输路径'.format(test_df.TRANSPORT_TRACE.nunique()))
# test_df.TRANSPORT_TRACE=test_df.TRANSPORT_TRACE.fillna("1")#给空值赋值为1
# print('运输路段长度：{}'.format(test_df.TRANSPORT_TRACE.apply(lambda x:len(x.split('-'))).unique()))
# print('运输过程中的 speed 情况：{}'.format(test_df.speed.unique()))
# print('经度跨越：{}'.format(test_df.longitude.max()-test_df.longitude.min()),'纬度跨越：{}'.format(test_df.latitude.max()-test_df.latitude.min()))
# print('测试集中，船只的运输的港口：')
# print(test_df.TRANSPORT_TRACE.value_counts())
# print('测试集时间跨度:')
# print('min time:{} max time:{} 中间time:{}'.format(test_df.timestamp.min(),test_df.timestamp.max(),test_df.timestamp.max()+test_df.timestamp.min()))

# test_df=pd.read_csv('F:\\\\BaiduNetdiskDownload\\\\result_data\\\\separate_data\\\\A.csv')#, chunksize=100000
# x_data=[]
# y_data=[]
# m=0
# for m in range(test_df.shape[0]):
#     if test_df.TRANSPORT_TRACE[m] =='CNYTN-MXZLO' and test_df.LoadingOrder[m]=='AU809825861449' and test_df.vesselStatus[m]=='under way using engine':
#         time=test_df.timestamp[m]
#         speed=test_df.speed[m]
#         x_data.append(time)
#         y_data.append(speed)
# #将两个列表写入csv文件
# f = open('F:\\\\BaiduNetdiskDownload\\\\result_data\\\\A_chuli5.csv','w',encoding='utf-8',newline='' "")
# csv_writer = csv.writer(f)
# csv_writer.writerow(['time','speed'])
# csv_writer.writerows(zip(x_data,y_data))
# f.close()
#
# with open('F:\\\\BaiduNetdiskDownload\\\\result_data\\\\A_chuli5.csv','r',newline='',) as csvfile:
#     reader = csv.reader(csvfile)
#     data=[]
#     for row in islice(reader, 1, None):
#         data.append(row)
# x_data=[x[0] for x in data]
# y_data=[int(y[1]) for y in data]
# # 设置图标样式，figsize=(横坐标长度，纵坐标长度)
# fig = plt.figure(figsize=(150,70))
# # 用来正常显示中文标签
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.plot(x_data,y_data,c='blue')
# # 设置X，Y轴刻度间距，及横坐标倾斜角度
# plt.xticks(np.arange(0,2500,10),rotation=90)#, rotation=45
# plt.yticks(np.arange(0,70,10))
# # 图表标题文字
# plt.title('CNYTN-MXZLO-only under way using engine', fontsize=24)
# plt.xlabel('time', fontsize=10)
# plt.ylabel('speed(Km/h)', fontsize=16)
# # plt.tick_params(axis='both', which='major', labelsize=26)
# plt.show()
#-------------------------------------------------------------------
# 获取所有订单运行状态的爬取
import csv
import pandas as pd
import glob
import time
import pandas as pd
import numpy as np

letter_list = ['A']


columns = ['LoadingOrder', 'carrierName', 'timestamp', 'longitude',
           'latitude', 'vesselMMSI', 'speed', 'direction', 'veseelNextport',
           'vesselNextportETA','vesselStatus', 'vesselDatasource', 'TRANSPORT_TRACE']

columns2 = ['LoadingOrder', 'carrierName', 'timestamp', 'longitude',
           'latitude', 'vesselStatus']

newcol = [0,1,2,3,4,10]

count=0
print('开始合并')
for i in range(len(letter_list)):
    df = pd.read_csv('F:\\\\BaiduNetdiskDownload\\\\result_data\\\\separate_data\\\\' +letter_list[i]+'.csv').dropna()
    df.columns = columns
    df = df.iloc[1:, newcol]  # 跳过标题行
    df.to_csv('F:\\\\BaiduNetdiskDownload\\\\result_data\\\\status.csv', mode='a', header=False, index=False)
    if count == 0:
        df = pd.read_csv('F:\\\\BaiduNetdiskDownload\\\\result_data\\\\status.csv', header=None,
                         names=['LoadingOrder', 'carrierName', 'timestamp', 'longitude',
                                'latitude', 'vesselStatus'])
        df.to_csv('F:\\\\BaiduNetdiskDownload\\\\result_data\\\\status.csv', index=False)
    count += df.shape[0]
    print(i, count)

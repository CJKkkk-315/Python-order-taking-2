import os
import pandas as pd
from pyecharts.charts import Bar
from pyecharts.charts import Map
from pyecharts import options as opts
# 遍历scenic文件夹中的文件
def get_datas():
    df_allinfo = pd.DataFrame()
    for root, dirs, files in os.walk('./'):
        for filename in files:
            try:
                df = pd.read_excel(f'./{filename}')
                df_allinfo = df_allinfo.append(df, ignore_index=True)
            except:
                continue
    # 去重
    df_allinfo.drop_duplicates(subset=['名称'], keep='first', inplace=True)
    return df_allinfo
def get_sales_bar(data):
    sort_info = data.sort_values(by='销量', ascending=True)
    c = (
        Bar()
        .add_xaxis(list(sort_info['名称'])[-20:])
        .add_yaxis('热门景点销量', sort_info['销量'].values.tolist()[-20:])
        .reversal_axis()
        .set_global_opts(
            title_opts=opts.TitleOpts(title='热门景点销量数据'),
            yaxis_opts=opts.AxisOpts(name='景点名称'),
            xaxis_opts=opts.AxisOpts(name='销量'),
            )
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .render('1-热门景点数据.html')
        )
def get_sales_geo(data):
    df = data[['城市','销量']]
    df_counts = df.groupby('城市').sum()
    c = (
        Map()
        .add('假期出行分布', [list(z) for z in zip(df_counts.index.values.tolist(), df_counts.values.tolist())], 'china')
        .set_global_opts(
        title_opts=opts.TitleOpts(title='假期出行数据地图分布'),
        visualmap_opts=opts.VisualMapOpts(max_=100000, is_piecewise=True),
        )
        .render('2-假期出行数据地图分布.html')
    )
def get_level_counts(data):
    df = data[data['星级'].isin(['4A', '5A'])]
    df_counts = df.groupby('城市').count()['星级']
    c = (
        Bar()
            .add_xaxis(df_counts.index.values.tolist())
            .add_yaxis('4A-5A景区数量', df_counts.values.tolist())
            .set_global_opts(
            title_opts=opts.TitleOpts(title='各省市4A-5A景区数量'),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_='inside')],
        )
        .render('3-各省市4A-5A景区数量.html')
    )
def get_level_geo(data):
    df = data[data['星级'].isin(['4A', '5A'])]
    df_counts = df.groupby('城市').count()['星级']
    c = (
        Map()
        .add('4A-5A景区分布', [list(z) for z in zip(df_counts.index.values.tolist(), df_counts.values.tolist())], 'china')
        .set_global_opts(
        title_opts=opts.TitleOpts(title='地图数据分布'),
        visualmap_opts=opts.VisualMapOpts(max_=50, is_piecewise=True),
        )
        .render('4-4A-5A景区数据地图分布.html')
    )
data = get_datas()
get_sales_bar(data)
get_sales_geo(data)
get_level_counts(data)
get_level_geo(data)
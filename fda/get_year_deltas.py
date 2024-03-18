import numpy as np
from datetime import datetime

def get_year_deltas(date_list,day_count=365.):
   """
    返回以年的比例表示的日期间隔的列表
   """
   start=date_list[0]
   delta_list=[(date-start).days/day_count for date in date_list]
   return np.array(delta_list)
dates=[datetime(2015,1,1),datetime(2015,7,1),datetime(2016,1,1)]
print(get_year_deltas(dates))
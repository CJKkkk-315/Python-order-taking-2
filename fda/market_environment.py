class market_environment(object):
   """
    这个类用来初始化用于估值的市场环境相关信息
   """
   def __init__(self,name,pricing_date):      #pricing_date为定价的基准日期
       self.name=name
       self.pricing_date=pricing_date
       self.constants={}       #常数
       self.lists={}           #列表
       self.curves={}          #曲线
   def add_constant(self,key,constant):
       self.constants[key]=constant
   def get_constant(self,key):
       return self.constants[key]
   def add_list(self,key,list_object):
       self.lists[key]=list_object
   def get_list(self,key):
       return self.lists[key]
   def add_curve(self,key,curve):
       self.curves[key]=curve
   def get_curve(self,key):
       return self.curves[key]
    #定义将常数、列表、曲线等加到一个变量中的方法
   def add_environment(self,env):
       """
       如果某个值是已经存在的，这里进行覆盖
       """
       for key in env.constants:
           self.constants[key]=env.constants[key]
       for key in env.lists:
           self.lists[key]=env.lists[key]
       for key in env.curves:
           self.curves[key]=env.curves[key]
          
   """
from fda.get_year_deltas import *
from fda.constant_short_rate import *
dates=[datetime(2015,1,1),datetime(2015,7,1),datetime(2016,1,1)]
csr=constant_short_rate('csr',0.05)
#添加一个市场环境
me_1=market_environment('me_1',datetime(2015,1,1))
me_1.add_list('symbols',['APPL','MSFT','FB'])
me_1.get_list('symbols')

me_2=market_environment('me_1',datetime(2015,1,1))
me_2.add_constant('volatility',0.2)
me_2.add_curve('short_rate',csr)
me_2.get_curve('short_rate')

me_1.add_environment(me_2)
me_1.get_curve('short_rate')

me_1.constants
me_1.lists
me_1.curves
me_1.get_curve('short_rate').short_rate
   """
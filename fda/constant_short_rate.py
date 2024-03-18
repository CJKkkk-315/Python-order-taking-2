from fda.get_year_deltas import *

class constant_short_rate():
    """
    这个类用于短期利率的贴现
    """
    def __init__(self,name,short_rate):
        self.name=name
        self.short_rate=short_rate
        if short_rate<0:
            raise ValueError('Short rate negative.')
 #通过dtobjects参数来判断是否为年分数，如果为True则为实际日期，否则为年分数
    def get_discount_factors(self,date_list,dtobjects=True):
        if dtobjects is True:
            dlist=get_year_deltas(date_list)
        else:
            dlist=np.array(date_list)
        dflist=np.exp(self.short_rate*np.sort(-dlist))   #贴现因子列表
        return np.array((date_list,dflist)).T
    
#dates=[datetime(2015,1,1),datetime(2015,7,1),datetime(2016,1,1)]
#csr=constant_short_rate('csr',0.05)
#csr.get_discount_factors(dates)

#deltas=get_year_deltas(dates)
#print(deltas)
#csr.get_discount_factors(deltas,dtobjects=False)
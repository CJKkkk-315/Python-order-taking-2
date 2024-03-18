# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 19:55:05 2022

@author: Administrator
"""

#衍生品头寸
#类
import sys
# sys.path:返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值 
sys.path.append(r"C:\install\Anaconda\Lib\site-packages\fda")

class derivatives_position(object):
    def __init__(self, name, quantity, underlying, mar_env,  otype, payoff_func):         
        self.name = name         
        self.quantity = quantity         
        self.underlying = underlying         
        self.mar_env = mar_env         
        self.otype = otype         
        self.payoff_func = payoff_func         
    def get_info(self):             
        print('NAME')             
        print(self.name, '\n')             
        print('QUANTITY')             
        print(self.quantity, '\n')             
        print('UNDERLYING')             
        print(self.underlying, '\n')            
        print('MARKET ENVIRONMENT')             
        print('\n**Constants**')             
        for key, value in self.mar_env.constants.items():                 
            print(key, value)             
        print('\n**Lists**')             
        for key, value in self.mar_env.lists.items():                 
            print(key, value)            
        print('\n**Curves**')             
        for key in self.mar_env.curves.items():                 
            print(key, value)             
        print('\nOPTION TYPE')             
        print(self.otype, '\n')             
        print('PAYOFF FUNCTION')             
        print(self.payoff_func)
    







#用例    
from  fda.market_environment import *
from fda.get_year_deltas import *
from fda.constant_short_rate import *
me_gbm = market_environment('me_gbm',datetime(2020, 1, 1))
me_gbm.add_constant('initial_value', 36.)       
me_gbm.add_constant('volatility', 0.2)         
me_gbm.add_constant('currency', 'EUR') 
me_gbm.add_constant('model', 'gbm')



#from derivatives_position import *
me_am_put = market_environment('me_am_put',datetime(2020, 1, 1))
me_am_put.add_constant('maturity',datetime(2020, 12, 31))           
me_am_put.add_constant('strike', 40.)         
me_am_put.add_constant('currency', 'EUR')

payoff_func = 'np.maximum(strike - instrument_values, 0)'
am_put_pos = derivatives_position(                       
     name='am_put_pos',                        
     quantity=3,                        
     underlying='gbm',                       
     mar_env=me_am_put,                        
     otype='American',                        
     payoff_func=payoff_func)


am_put_pos.get_info()          
          







#衍生品投资组合
#类
import numpy as np
import pandas as pd 
from fda import *         
from geometric_brownian_motion import geometric_brownian_motion
from jump_diffusion import jump_diffusion
from square_root_diffusion import square_root_diffusion

from valuation_mcs_european import valuation_mcs_european
from valuation_mcs_american import valuation_mcs_american

from derivatives_portfolio import derivatives_portfolio


# models available for risk factor modeling
models = {'gbm': geometric_brownian_motion,           
          'jd': jump_diffusion,           
          'srd': square_root_diffusion} 
# allowed exercise types
otypes = {'European': valuation_mcs_european,           
          'American': valuation_mcs_american} 

class derivatives_portfolio(object):
    def __init__(self, name, positions, val_env, assets, correlations=None, fixed_seed=False): 
        self.name = name 
        self.positions = positions 
        self.val_env = val_env 
        self.assets = assets 
        self.underlyings = set() 
        self.correlations = correlations 
        self.time_grid = None 
        self.underlying_objects = {} 
        self.valuation_objects = {} 
        self.fixed_seed = fixed_seed 
        self.special_dates = [] 
        
        for pos in self.positions: 
            # determine earliest starting_date
            self.val_env.constants['starting_date'] = \
                min(self.val_env.constants['starting_date'], 
                    positions[pos].mar_env.pricing_date)             
            # determine latest date of relevance
            self.val_env.constants['final_date'] =\
                max(self.val_env.constants['final_date'], 
                    positions[pos].mar_env.constants['maturity'])             
            # collect all underlyings and            
            # add to set (avoids redundancy)
            self.underlyings.add(positions[pos].underlying)   
            
            
            
        # generate general time grid
        start = self.val_env.constants['starting_date'] 
        end = self.val_env.constants['final_date'] 
        time_grid = pd.date_range(start=start, end=end, 
                                  freq=self.val_env.constants['frequency'] 
                                  ).to_pydatetime() 
        time_grid = list(time_grid) 
        for pos in self.positions:
            maturity_date = positions[pos].mar_env.constants['maturity'] 
            if maturity_date not in time_grid: 
                time_grid.insert(0, maturity_date) 
                self.special_dates.append(maturity_date) 
            if start not in time_grid: 
                time_grid.insert(0, start) 
            if end not in time_grid: 
                time_grid.append(end)        
            # delete duplicate entries
            time_grid = list(set(time_grid))         
            # sort dates in time_grid
            time_grid.sort() 
            self.time_grid = np.array(time_grid) 
            self.val_env.add_list('time_grid', self.time_grid) 
            
            
            
            
            if correlations is not None: 
                # take care of correlations
             ul_list = sorted(self.underlyings)
             correlation_matrix = np.zeros((len(ul_list), len(ul_list)))
             np.fill_diagonal(correlation_matrix, 1.0)
             correlation_matrix = pd.DataFrame(correlation_matrix,
                                  index=ul_list, columns=ul_list) 
             
             
             
            for i, j, corr in correlations:
                corr = min(corr, 0.999999999999)
                # fill correlation matrix
                correlation_matrix.loc[i, j] = corr
                correlation_matrix.loc[j, i] = corr
            # determine Cholesky matrix
            cholesky_matrix = np.linalg.cholesky(np.array(correlation_matrix))
            # dictionary with index positions for the
            # slice of the random number array to be used by
            # respective underlying
            rn_set = {asset: ul_list.index(asset)
                   for asset in self.underlyings}
            
            
            
            
            
            # random numbers array, to be used by
            # all underlyings (if correlations exist)
            random_numbers = sn_random_numbers((len(rn_set),
                                                len(self.time_grid),
                                                self.val_env.constants
                                       ['paths']),
                                   fixed_seed=self.fixed_seed)
            
            
            # add all to valuation environment that is
            # to be shared with every underlying
            self.val_env.add_list('cholesky_matrix', cholesky_matrix)
            self.val_env.add_list('random_numbers', random_numbers)
            self.val_env.add_list('rn_set', rn_set)
            
            
            for asset in self.underlyings:
             # select market environment of asset
             mar_env = self.assets[asset]
             # add valuation environment to market environment
             mar_env.add_environment(val_env)
             # select right simulation class
             model = models[mar_env.constants['model']]
             # instantiate simulation object
             if correlations is not None:
                 self.underlying_objects[asset] = model(asset, mar_env,
                                                        corr=True)
                 
             else:
                     self.underlying_objects[asset] = model(asset, mar_env,
                                                            corr=False)
                
                
                
                
                
        for pos in positions:
            # select right valuation class (European, American)
            val_class = otypes[positions[pos].otype]
            # pick market environment and add valuation environment
            mar_env = positions[pos].mar_env
            mar_env.add_environment(self.val_env)
            # instantiate valuation class
            self.valuation_objects[pos] = \
                val_class(name=positions[pos].name,
                          mar_env=mar_env,
                          underlying=self.underlying_objects[
                    positions[pos].underlying],
                payoff_func=positions[pos].payoff_func)
                
                
                
    def get_positions(self):
 
        for pos in self.positions:
            bar = '\n' + 50 * '-'
            print(bar)
            self.positions[pos].get_info()
            print(bar) 
 
    def get_statistics(self, fixed_seed=False):
        res_list = []
        # iterate over all positions in portfolio
        for pos, value in self.valuation_objects.items():
            p = self.positions[pos]
            pv = value.present_value(fixed_seed=fixed_seed)
            res_list.append([
                p.name,
                p.quantity,
                # calculate all present values for the single instruments
                pv,
                value.currency,
                # single instrument value times quantity
                pv * p.quantity,
                # calculate delta of position
                value.delta() * p.quantity,
                # calculate vega of position
                value.vega() * p.quantity,
                ])
            # generate a pandas DataFrame object with all results
            res_df = pd.DataFrame(res_list,
                                  columns=['name', 'quant.', 'value', 'curr.',
                                           'pos_value', 'pos_delta', 'pos_vega'])
            return res_df 
     

























from fda.market_environment import *
#用li
me_jd = market_environment('me_jd', me_gbm.pricing_date)
me_jd.add_constant('lambda', 0.3) 
me_jd.add_constant('mu', -0.75)
me_jd.add_constant('delta', 0.1)
me_jd.add_environment(me_gbm) 
me_jd.add_constant('model', 'jd')

me_eur_call = market_environment('me_eur_call', me_jd.pricing_date)
me_eur_call.add_constant('maturity', datetime(2020, 6, 30))
me_eur_call.add_constant('strike', 38.)
me_eur_call.add_constant('currency', 'EUR')
payoff_func = 'np.maximum(maturity_value - strike, 0)'
eur_call_pos = derivatives_position(
   name='eur_call_pos',
   quantity=5,
   underlying='jd',
   mar_env=me_eur_call,
   otype='European',
   payoff_func=payoff_func)

from fda.constant_short_rate import *
# fix this
# underlying={'gbm': me_gbm,'jd': me_jd}
underlyings={'gbm': me_gbm,'jd': me_jd}
positions = {'am_put_pos' : am_put_pos,
            'eur_call_pos': eur_call_pos}
csr = constant_short_rate('csr', 0.06)
val_env = market_environment('general', me_gbm.pricing_date)
val_env.add_constant('frequency', 'W')
val_env.add_constant('paths', 25000)
val_env.add_constant('starting_date', val_env.pricing_date)
val_env.add_constant('final_date',val_env.pricing_date)
val_env.add_curve('discount_curve', csr)


from derivatives_portfolio import derivatives_portfolio
import matplotlib.pyplot as plt

portfolio = derivatives_portfolio(
    name='portfolio',
    positions=positions,
    val_env=val_env,
    assets=underlyings,
    fixed_seed=False)
 
 
#%time
portfolio.get_statistics(fixed_seed=False)        
portfolio.get_statistics(fixed_seed=False)[
        ['pos_value', 'pos_delta', 'pos_vega']].sum() 
  
portfolio.get_positions()
portfolio.valuation_objects['am_put_pos'].present_value()
portfolio.valuation_objects['eur_call_pos'].delta()          


path_no = 888
path_gbm = portfolio.underlying_objects[
   'gbm'].get_instrument_values()[:, path_no]
path_jd = portfolio.underlying_objects[
   'jd'].get_instrument_values()[:, path_no]
plt.figure(figsize=(10,6))
plt.plot(portfolio.time_grid, path_gbm, 'r', label='gbm')
plt.plot(portfolio.time_grid, path_jd, 'b', label='jd')
plt.xticks(rotation=30)
plt.legend(loc=0)
 
correlations = [['gbm', 'jd', 0.9]]
port_corr = derivatives_portfolio(
        name='portfolio',
        positions=positions,
        val_env=val_env, 
        assets=underlyings,
        correlations=correlations,
        fixed_seed=True)
port_corr.get_statistics() 


path_gbm = port_corr.underlying_objects['gbm'].\
     get_instrument_values()[:, path_no]
path_jd = port_corr.underlying_objects['jd'].\
     get_instrument_values()[:, path_no]
     
plt.figure(figsize=(10, 6))
plt.plot(portfolio.time_grid, path_gbm, 'r', label='gbm')
plt.plot(portfolio.time_grid, path_jd, 'b', label='jd')
plt.xticks(rotation=30)
plt.legend(loc=0); 

 
pv1 = 5 * port_corr.valuation_objects['eur_call_pos'].\
        present_value(full=True)[1]
pv1

pv2 = 3 * port_corr.valuation_objects['am_put_pos'].\
        present_value(full=True)[1]
pv2

plt.figure(figsize=(10, 6))
plt.hist([pv1, pv2], bins=25,
         label=['European call', 'American put']);
plt.axvline(pv1.mean(), color='r', ls='dashed',
         lw=1.5, label='call mean = %4.2f' % pv1.mean())
plt.axvline(pv2.mean(), color='r', ls='dotted',
            lw=1.5, label='put mean = %4.2f' % pv2.mean())
plt.xlim(0, 80); plt.ylim(0, 10000)
plt.legend(); 
 
 
pvs = pv1 + pv2
plt.figure(figsize=(10, 6))
plt.hist(pvs, bins=50, label='portfolio');
plt.axvline(pvs.mean(), color='r', ls='dashed',
lw=1.5, label='mean = %4.2f' % pvs.mean())
plt.xlim(0, 80); plt.ylim(0, 7000)
plt.legend();
 
pvs.std()

pv1 = (5 * portfolio.valuation_objects['eur_call_pos'].
       present_value(full=True)[1])
pv2 = (3 * portfolio.valuation_objects['am_put_pos'].
       present_value(full=True)[1])
(pv1 + pv2).std()
 
 
 


















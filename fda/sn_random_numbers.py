# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 21:34:42 2022

@author: Administrator
"""


import numpy as np

def sn_random_numbers(shape,antithetic=True,moment_matching=True,fixed_seed=False):   
    if fixed_seed:       
        np.random.seed(1000)   
    if antithetic:       
        ran=np.random.standard_normal((shape[0],shape[1],int(shape[2]/2)))       
        ran=np.concatenate((ran,-ran),axis=2)   
    else:       
        ran=np.random.standard_normal(shape)   
    if moment_matching:       
        ran=ran-np.mean(ran)       
        ran=ran/np.std(ran)   
    if shape[0]==1:       
        return ran[0]   
    else:       
        return ran
    
#生成2*2*2的随机数
snrn=sn_random_numbers((2,2,2),antithetic=False,moment_matching=False,fixed_seed=True)
print(snrn)

#生成2*3*2的随机数
snrn_mm=sn_random_numbers((2,3,2),antithetic=False,moment_matching=True,fixed_seed=True)
print(snrn_mm)

#查看随机数的均值和标准差
print(snrn_mm.mean())
print(snrn_mm.std())
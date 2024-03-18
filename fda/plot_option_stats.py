# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 20:21:24 2022

@author: Administrator
"""
import matplotlib.pyplot as plt
def plot_option_stats(s_list,p_list,d_list,v_list): 
    """    
    此函数用于绘制期权的价格，delta,以及vega，关于一组不同的标的    资产的初始价值
    """   
    plt.figure(figsize=(9,7))
    sub1=plt.subplot(311)   
    plt.plot(s_list,p_list,'ro',label='present_value')
    plt.plot(s_list,p_list,'b')
    plt.grid(True);
    plt.legend(loc=0)
    plt.setp(sub1.get_xticklabels(),visible=False)
    sub2=plt.subplot(312)   
    plt.plot(s_list,d_list,'go',label='Delta')
    plt.plot(s_list,d_list,'b')   
    plt.grid(True);plt.legend(loc=0)
    plt.setp(sub2.get_xticklabels(),visible=False)
    sub3=plt.subplot(313)   
    plt.plot(s_list,v_list,'yo',label='Vega')
    plt.plot(s_list,v_list,'b')   
    plt.xlabel('Initial value of underlying')
    plt.grid(True);
    plt.legend(loc=0)


# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 16:25:27 2021

@author: jqj
"""
import math
import numpy as np
import time


def tMIN(bi,ci,ψi,cii,ψii,Wi,Ui,ai,δi,PW,di,H,Kh,Kv,fh,fv,t,vs,vp,p,h,n):
#筛选初始相位函数
#输入参数
# bi 宽度
# ci 底面粘聚力
# ψi 摩擦角
# cii 侧面粘聚力
# ψii 侧面摩擦角
# Wi 各滑块重度
# Ui 底滑面孔隙水压力
# ai 底面与水平面夹角
# δi 侧面与竖直面的夹角
# PW 侧滑面水压力
# di 左侧面宽度
# H 坡高
# Kh 水平地震力系数
# Kv 竖直地震力系数
# fh 横波频率
# fv 纵波频率
# t 初始相位变化范围
# vs 横波波速
# vp 纵波波速
# p 各滑块重度
# n 条块数
#输出参数
# Min Sarma法安全系数

    T=np.arange(0,t,0.1)
    fs=np.zeros(len(T))

    for i in range(len(T)):
        fs[i]=Ub(bi,ci,ψi,cii,ψii,Wi,Ui,ai,δi,PW,di,H,Kh,Kv,fh,fv,T[i],vs,vp,p,h,n)
        
        
    Min=fs[0]
    for i in range(len(T)):
        if Min>=fs[i]>0:
            Min=fs[i]
    print(Min)
    return Min



def Ub(bi, ci, ψi, cii, ψii, Wi, Ui, ai, δi, PW, di, H, Kh, Kv, fh, fv, t, vs, vp, p, h, n):
# 拟动力Sarma法地震边坡稳定性安全系数
#输入参数
# bi 宽度
# ci 底面粘聚力
# ψi 摩擦角
# cii 侧面粘聚力
# ψii 侧面摩擦角
# Wi 各滑块重度
# Ui 底滑面孔隙水压力
# ai 底面与水平面夹角
# δi 侧面与竖直面的夹角
# PW 侧滑面水压力
# di 左侧面宽度
# H 坡高
# Kh 水平地震力系数
# Kv 竖直地震力系数
# fh 横波频率
# fv 纵波频率
# t 初始相位变化范围
# vs 横波波速
# vp 纵波波速
# p 各滑块重度
# n 条块数
#输出参数
# Fs Sarma法安全系数

    ψii = ψii + [0]
    δi = δi + [0]
    pi = [None] * n
    ei = [None] * n
    Ri = [None] * n
    Si = [None] * n
    Ai = [None] * n
    Fh = [None] * n
    Fv = [None] * n
    for i in range(n):
        ψi[i] = math.radians(ψi[i])
        ψii[i] = math.radians(ψii[i])
        ai[i] = math.radians(ai[i])
        δi[i] = math.radians(δi[i])
    for i in range(n):
        Fh[i] = Kh * p[i] * bi[i] * vs / (2 * (math.pi) * (fh + 2.220446049250313e-16)) * (
                    math.cos(2 * (math.pi) * fh * ((t - H / (vs + 2.220446049250313e-16)))) - math.cos(
                2 * (math.pi) * fh * (t - (H - h[i]) / (vs + 2.220446049250313e-16))))
        Fv[i] = Kv * p[i] * bi[i] * vp / (2 * (math.pi) * (fv + 2.220446049250313e-16)) * math.cos(
            2 * (math.pi) * fv * ((t - H / (vp + 2.220446049250313e-16)))) - (
                    math.cos(2 * (math.pi) * fv * (t - (H - h[i]) / (vp + 2.220446049250313e-16))))
        pi[i] = Wi[i] * math.cos(ψi[i] - ai[i]) * math.cos(ψii[i]) / math.cos(ψi[i] - ai[i] + ψii[i] - δi[i + 1])
        ei[i] = math.cos(ψi[i] - ai[i] + ψii[i] - δi[i]) * math.cos(ψii[i + 1]) / (
                    math.cos(ψi[i] - ai[i] + ψii[i] - δi[i + 1]) * math.cos(ψii[i]))
        Ri[i] = ci[i] * bi[i] / math.cos(ai[i]) - Ui[i] * math.tan(ψi[i])
        Si[i] = cii[i] * di[i] / math.cos(ai[i]) - PW[i] * math.tan(ψi[i])
    Si = Si + [0]
    for i in range(n):
        Ai[i] = ((Wi[i] + Fv[i]) * math.sin(ψi[i] - ai[i]) + Ri[i] * math.cos(ψi[i]) + Si[i + 1] * math.sin(
            ψi[i] - ai[i] - δi[i + 1]) - Si[i] * math.sin(ψi[i] - ai[i] - δi[i]) + Fh[i] * math.cos(
            ψi[i] - ai[i])) * math.cos(ψii[i]) / math.cos(ψi[i] - ai[i] + ψii[i] - δi[i + 1])
    ei.reverse()
    Ai.reverse()
    pi.reverse()
    Ei = [None] * n
    for i in range(n):
        Ei[i] = [1] + ei[0:i]
    from functools import reduce
    r = [None] * n
    for i in range(n):
        r[i] = reduce(lambda x, y: x * y, Ei[i])  # 对序列lis中元素逐项相乘lambda用法请自行度娘
    sh = [a * b for a, b in zip(Ai, r)]
    xi = [a * b for a, b in zip(pi, r)]
    SH = 0
    XI = 0
    for i in range(0, len(sh)):
        SH = SH + sh[i]
    for i in range(0, len(xi)):
        XI = XI + xi[i]
    Ub = SH / XI
    Fs = 1
    if Ub < 0:
        while Ub < 0:
            Fs = Fs - 0.001
            ci = [i / Fs for i in ci]
            cii = [i / Fs for i in cii]
            pi = [None] * n
            ei = [None] * n
            Ri = [None] * n
            Si = [None] * n
            Ai = [None] * n
            f1 = [None] * n
            f2 = [None] * n
            for i in range(n):
                f1[i] = math.tan(ψi[i]) / Fs
                f2[i] = math.tan(ψii[i]) / Fs
                ψi[i] = math.atan(f1[i])
                ψii[i] = math.atan(f2[i])
            for i in range(n):
                pi[i] = Wi[i] * math.cos(ψi[i] - ai[i]) * math.cos(ψii[i]) / math.cos(
                    ψi[i] - ai[i] + ψii[i] - δi[i + 1])
                ei[i] = math.cos(ψi[i] - ai[i] + ψii[i] - δi[i]) * math.cos(ψii[i + 1]) / (
                            math.cos(ψi[i] - ai[i] + ψii[i] - δi[i + 1]) * math.cos(ψii[i]))
                Ri[i] = ci[i] * bi[i] / math.cos(ai[i]) - Ui[i] * math.tan(ψi[i])
                Si[i] = cii[i] * di[i] / math.cos(ai[i]) - PW[i] * math.tan(ψi[i])
                Si = Si + [0]
            for i in range(n):
                Ai[i] = ((Wi[i] + Fv[i]) * math.sin(ψi[i] - ai[i]) + Ri[i] * math.cos(ψi[i]) + Si[i + 1] * math.sin(
                    ψi[i] - ai[i] - δi[i + 1]) - Si[i] * math.sin(ψi[i] - ai[i] - δi[i]) - Fh[i] * math.cos(
                    ψi[i] - ai[i])) * math.cos(ψii[i]) / math.cos(ψi[i] - ai[i] + ψii[i] - δi[i + 1])
            ei.reverse()
            Ai.reverse()
            pi.reverse()
            Ei = [None] * n
            for i in range(n):
                Ei[i] = [1] + ei[0:i]
            from functools import reduce
            r = [None] * n
            for i in range(n):
                r[i] = reduce(lambda x, y: x * y, Ei[i])  # 对序列lis中元素逐项相乘lambda用法请自行度娘
            sh = [a * b for a, b in zip(Ai, r)]
            xi = [a * b for a, b in zip(pi, r)]
            SH = 0
            XI = 0
            for i in range(0, len(sh)):
                SH = SH + sh[i]
            for i in range(0, len(xi)):
                XI = XI + xi[i]
            Ub = SH / XI
    else:
        while Ub > 0:
            Fs = Fs + 0.001
            ci = [i / Fs for i in ci]
            cii = [i / Fs for i in cii]
            pi = [None] * n
            ei = [None] * n
            Ri = [None] * n
            Si = [None] * n
            Ai = [None] * n
            f1 = [None] * n
            f2 = [None] * n
            for i in range(n):
                f1[i] = math.tan(ψi[i]) / Fs
                f2[i] = math.tan(ψii[i]) / Fs
                ψi[i] = math.atan(f1[i])
                ψii[i] = math.atan(f2[i])
            for i in range(n):
                # Fh[i]=Kh[i]*p[i]*bi[i]*vs[i]/(2*math.pi*(fh[i]+1e-10))*((np.cos(2*(math.pi)*fh[i]*(t-(H[i]-h[i])/(vs[i]+1e-10))))-np.cos(2*math.pi*fh[i]*((t-H[i]/(vs[i]+1e-10)))))
                # Fv[i]=Kv[i]*p[i]*bi[i]*vp[i]/(2*math.pi*(fv[i]+1e-10))*((np.cos(2*(math.pi)*fv[i]*(t-(H[i]-h[i])/(vp[i]+1e-10))))-np.cos(2*math.pi*fv[i]*((t-H[i]/(vp[i]+1e-10)))))
                pi[i] = Wi[i] * math.cos(ψi[i] - ai[i]) * math.cos(ψii[i]) / math.cos(
                    ψi[i] - ai[i] + ψii[i] - δi[i + 1])
                ei[i] = math.cos(ψi[i] - ai[i] + ψii[i] - δi[i]) * math.cos(ψii[i + 1]) / (
                            math.cos(ψi[i] - ai[i] + ψii[i] - δi[i + 1]) * math.cos(ψii[i]))
                Ri[i] = ci[i] * bi[i] / math.cos(ai[i]) - Ui[i] * math.tan(ψi[i])
                Si[i] = cii[i] * di[i] / math.cos(ai[i]) - PW[i] * math.tan(ψi[i])
                Si = Si + [0]
            for i in range(n):
                Ai[i] = ((Wi[i] + Fv[i]) * math.sin(ψi[i] - ai[i]) + Ri[i] * math.cos(ψi[i]) + Si[i + 1] * math.sin(
                    ψi[i] - ai[i] - δi[i + 1]) - Si[i] * math.sin(ψi[i] - ai[i] - δi[i]) - Fh[i] * math.cos(
                    ψi[i] - ai[i])) * math.cos(ψii[i]) / np.cos(ψi[i] - ai[i] + ψii[i] - δi[i + 1])
            ei.reverse()
            Ai.reverse()
            pi.reverse()
            Ei = [None] * n
            for i in range(n):
                Ei[i] = [1] + ei[0:i]
            from functools import reduce
            r = [None] * n
            for i in range(n):
                r[i] = reduce(lambda x, y: x * y, Ei[i])  # 对序列lis中元素逐项相乘lambda用法请自行度娘
            sh = [a * b for a, b in zip(Ai, r)]
            xi = [a * b for a, b in zip(pi, r)]
            SH = 0
            XI = 0

            for i in range(0, len(sh)):
                SH = SH + sh[i]
            for i in range(0, len(xi)):
                XI = XI + xi[i]
            Ub = SH / XI
    return Fs

mylist=[[3.56,6.26,4.26,6.25,5.27,4.37] ,\
        #宽度bi
        [34.1,32.8,38.5,36.8,37.3,31.2],\
        # 底面粘聚力ci
        [28.4,30.8,32.7,36.6,38.5,41.6],\
        #摩擦角ψi
        [48.5,43,46.8,38.6,36.3,39.7],\
        #侧面粘聚力cii
        [0,32.1,18.7,23,25.9,0],\
        #侧面摩擦角ψii
        [960 ,850, 590 ,530 ,860,420],\
        #滑块重度Wi
        [42 ,41 ,39 ,44 ,50,41],\
        #底滑面孔隙水压力Ui
        [46 ,46.4, 42.1, 48.4 ,49.5,39.4],\
        #底面与水平面夹角ai
        [0 ,65, 49 ,42,50,0 ],\
        #侧面与竖直面的夹角δi
        [42.4 ,41.3 ,39.6 ,48.3,46.3,43.7 ],\
        #PW
        [3.5,6,5,5,4,4],\
        #左侧面宽度di
        10.0,\
        #坡高H
        0.1,\
        #水平地震力系数Kh
        0.0,\
        #竖直地震力系数Kv
        1.0,\
        #横波频率fh
        0.0,\
        #纵波频率fv
        0.5,\
        #持续时间t
        300.0,\
        #横波波速vs
        0.0,\
        #纵波波速vp
        [20,20,20,20,20,20],\
        #左侧面宽度di
        [3.56,6.26,4.26,6.25,5.27,4.37],\
        #重度p
        6
        #条块数
        ]
t0 = time.time()
tMIN(*mylist)
t1 = time.time()
print('time cost:%s sec' % (t1 - t0))

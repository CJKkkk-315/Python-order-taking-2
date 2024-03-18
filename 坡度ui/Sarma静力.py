# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 16:25:27 2021

@author: jqj
"""
import math
import numpy as np
import time

def Ub(bi, ci, ψi, cii, ψii, Wi, Ui, ai, δi, PW, di, n):
# Sarma法 静力地震边坡稳定性安全系数
    ψii = ψii + [0]
    δi = δi + [0]
    pi = [None] * n
    ei = [None] * n
    Ri = [None] * n
    Si = [None] * n
    Ai = [None] * n
    for i in range(n):
        ψi[i] = math.radians(ψi[i])
        ψii[i] = math.radians(ψii[i])
        ai[i] = math.radians(ai[i])
        δi[i] = math.radians(δi[i])
    for i in range(n):
        pi[i] = Wi[i] * math.cos(ψi[i] - ai[i]) * math.cos(ψii[i]) / math.cos(ψi[i] - ai[i] + ψii[i] - δi[i + 1])
        ei[i] = math.cos(ψi[i] - ai[i] + ψii[i] - δi[i]) * math.cos(ψii[i + 1]) / (
                    math.cos(ψi[i] - ai[i] + ψii[i] - δi[i + 1]) * math.cos(ψii[i]))
        Ri[i] = ci[i] * bi[i] / math.cos(ai[i]) - Ui[i] * math.tan(ψi[i])
        Si[i] = cii[i] * di[i] / math.cos(ai[i]) - PW[i] * math.tan(ψi[i])
    Si = Si + [0]
    for i in range(n):
        Ai[i] = (Wi[i] * math.sin(ψi[i] - ai[i]) + Ri[i] * math.cos(ψi[i]) + Si[i + 1] * math.sin(ψi[i] - ai[i] - δi[i + 1]) - Si[i] * math.sin(ψi[i] - ai[i] - δi[i])  ) * math.cos(ψii[i]) / math.cos(ψi[i] - ai[i] + ψii[i] - δi[i + 1])
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
            print(Fs)
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
                Ai[i] = (Wi[i] * math.sin(ψi[i] - ai[i]) + Ri[i] * math.cos(ψi[i]) + Si[i + 1] * math.sin(
                    ψi[i] - ai[i] - δi[i + 1]) - Si[i] * math.sin(ψi[i] - ai[i] - δi[i]) ) * math.cos(ψii[i]) / math.cos(ψi[i] - ai[i] + ψii[i] - δi[i + 1])
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
            print(Ub)
    else:
        while Ub > 0:
            Fs = Fs + 0.001
            print(Fs)
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
                Ai[i] = (Wi[i]  * math.sin(ψi[i] - ai[i]) + Ri[i] * math.cos(ψi[i]) + Si[i + 1] * math.sin(
                    ψi[i] - ai[i] - δi[i + 1]) - Si[i] * math.sin(ψi[i] - ai[i] - δi[i]) ) * math.cos(ψii[i]) / np.cos(ψi[i] - ai[i] + ψii[i] - δi[i + 1])
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


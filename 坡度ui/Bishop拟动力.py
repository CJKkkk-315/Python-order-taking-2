import time
import numpy as np
import math

def BSDtMIN(H, a, p, c, q, Kh, Kv, fh, fv, t, FS, vs, vp):
    # Initial phase screening function of seismic wave
    #  输入参数
    #  H  （坡高）
    #  a  （坡角）
    #  p  （重度）
    #  c  （粘聚力）
    #  q  （摩擦角）
    #  Kh （水平地震力系数）
    #  Kv （竖直地震力系数）
    #  fh （横波频率）
    #  fv （纵波频率）
    #  t   （初始相位变化范围）
    #  FS （瑞典条分法安全系数）
    #  vs （横波波速）
    #  vp（纵波波速）
    #  N   (条分数目)
    #  输出参数
    #  MIN （Bishop法最危险滑动面安全系数）
    T = np.arange(0, t, 0.1)
    fs = np.zeros(len(T))
    for i in range(len(T)):
        fs[i] = BSD(H, a, p, c, q, Kh, Kv, fh, fv, T[i], FS, vs, vp)
    Min = fs[0]
    for i in range(len(T)):
        if Min >= fs[i] > 0:
            Min = fs[i]
    print(Min)
    return Min

def BSD(H, a, p, c, q, Kh, Kv, fh, fv, t, FS, vs, vp):
    # Sliding surface search function
    # 输入参数
    #  H  （坡高）
    #  a  （坡角）
    #  p  （重度）
    #  c  （粘聚力）
    #  q  （摩擦角）
    #  Kh （水平地震力系数）
    #  Kv （竖直地震力系数）
    #  fh （横波频率）
    #  fv （纵波频率）
    #  t   （初始相位变化范围）
    #  FS （瑞典条分法安全系数）
    #  vs （横波波速）
    #  vp（纵波波速）
    # 输出参数
    #  v  （最危险滑动面坡上出露点的横坐标及滑动面圆心横坐标）
    #  Yo （最危险滑动面圆心纵坐标）
    #  Min（最危险滑动面安全系数）
    a=math.radians(a)
    q=math.radians(q)
    Xl = 0
    Xr = np.arange(H / (math.tan(a)), H / (math.tan(a)) + H, 1)
    Xo = np.arange(-H, H, 5)
    fs = np.zeros((len(Xr), len(Xo)))
    for i in range(len(Xr)):
        for j in range(len(Xo)):
            fs[i][j] = BISHOPD(H, a, p, c, q, Kh, Kv, fh, fv, t, FS, vs, vp, Xl, Xr[i], Xo[j])
            if H > -(Xr[i] - Xl) / H * (Xo[j] - (Xr[i] + Xl) / 2) + H / 2:
                fs[i][j] = 10
    min = fs[0][0]
    for i in range(len(Xr)):
        for j in range(len(Xo)):
            if min >= fs[i][j] > 0:
                min = fs[i][j]
    print(min)
    return min

def BISHOPD(H, a, p, c, q, Kh, Kv, fh, fv, t, FS, vs, vp, Xl, Xr, Xo):
    # The formula of safety factor of homogeneous soil slope is obtained based on pseudo-dynamic bishop method
    # 输入参数
    #  H  （坡高）
    #  a  （坡角）
    #  p  （重度）
    #  c  （粘聚力）
    #  q  （摩擦角）
    #  Kh （水平地震力系数）
    #  Kv （竖直地震力系数）
    #  fh （横波频率）
    #  fv （纵波频率）
    #  t   （初始相位变化范围）
    #  FS （瑞典条分法安全系数）
    #  vs （横波波速）
    #  vp（纵波波速）
    #  输出参数
    #  Fs （毕肖普法圆弧滑动面安全系数）
    k1 = math.tan(a)
    k2 = math.tan(q)
    Yo = -(Xr - Xl) / H * (Xo - (Xr + Xl) / 2) + H / 2
    R = ((Xo-Xl)**2+Yo**2)**0.5
    x = np.arange(Xl,Xr,0.1)
    S = np.zeros(len(x))
    C = np.zeros(len(x))
    L = np.zeros(len(x))
    b = (Xr - Xl) / len(x)
    for i in range(len(x)):
        S[i] = (x[i]-Xo)/R
        C[i] = ((R ** 2 - (x[i] - Xo) ** 2) ** 0.5) / R
        L[i] = b / C[i]
    h = np.zeros(len(x))
    W = np.zeros(len(x))
    for i in range(len(x)):
        if x[i] <= 0:
            h[i] = (R ** 2 - (x[i] - Xo) ** 2) ** 0.5 - Yo
        elif x[i] > 0 and x[i] <= H / k1:
            h[i] = k1 * x[i] + (R ** 2 - (x[i] - Xo) ** 2) ** 0.5 - Yo
        else:
            h[i] = H + (R ** 2 - (x[i] - Xo) ** 2) ** 0.5 - Yo

    Fh = np.zeros(len(x))
    for i in range(len(x)):
        Fh[i]= Kh*p*b*vs/(2*(math.pi)*(fh+2.220446049250313e-16))*((math.cos(2*(math.pi)*fh*(t-H/(vs+2.220446049250313e-16))))-math.cos(2*(math.pi)*fh*(t-(H-h[i])/(vs+2.220446049250313e-16))))
    Fv = np.zeros(len(x))
    for i in range(len(x)):
        Fv[i] = Kv*p*b*vp/(2*(math.pi)*(fv+2.220446049250313e-16))*((math.cos(2*(math.pi)*fv*(t-H/(vp+2.220446049250313e-16))))-math.cos(2*(math.pi)*fv*(t-(H-h[i])/(vp+2.220446049250313e-16))))
    M = np.zeros(len(x))
    M11 = np.zeros(len(x))
    M21 = np.zeros(len(x))
    M22 = np.zeros(len(x))
    M23 = np.zeros(len(x))
    M1=0
    M2=0
    M211=0
    M221=0
    M231=0
    for i in range(len(x)):
      if np.min(np.sign(h[i])) < 0:
        M1 = 10
        M2 = 1
      elif Xo > H / math.tan(2 * (math.atan(H / (Xr - Xl) + 2.220446049250313e-16))):
        M1 = 10
        M2 = 1
      else:
        FS = 1.1 * FS
        for i in range(len(x)):
            W[i] = p * b * h[i]
            M[i] = C[i] + (S[i] * k2) / FS
            M11[i] = (c * b + (W[i] - Fv[i]) * k2) / M[i]
            M21[i] = W[i] * S[i]
            M22[i] = Fh[i] * ((R ** 2 - (x[i] - Xo) ** 2) ** 0.5) - h[i] / 2
            M23[i] = Fv[i] * S[i]
        for i in M11:
            M1 += i
        for i in M21:
            M211 += i
        for i in M22:
            M221 += i
        for i in M23:
            M231 += i
        M2=M211+M221/R+M231
        if M2< 0:
            M2 = M1 / 10
        Fs = M1 / M2
        while abs(Fs - FS) >= 0.001:
            FS = Fs
            for i in range(len(x)):
                W[i] = p * b * h[i]
                M[i] = C[i] + (S[i] * k2) / FS
                M11[i] = (c * b + (W[i] - Fv[i]) * k2) / M[i]
                M21[i] = W[i] * S[i]
                M22[i] = Fh[i] * ((R ** 2 - (x[i] - Xo) ** 2) ** 0.5) - h[i] / 2
                M23[i] = Fv[i] * S[i]
            for i in M11:
                M1 += i
            for i in M21:
                M211 += i
            for i in M22:
                M221 += i
            for i in M23:
                M231 += i
            M2 = M211 + M221/R + M231
            if M2 < 0:
                M2 = M1 / 10
            Fs = M1 / M2
    Fs = M1 / M2
    print(Fs)
    return Fs

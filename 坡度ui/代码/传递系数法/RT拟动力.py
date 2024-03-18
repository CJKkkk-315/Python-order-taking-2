import math
import numpy as np
import time

def U1(H,a,p,c,q,FS,Kh,Kv,fh,fv,t,vs,vp,Xl,Xr,B,n):
# 地震边坡稳定性安全系数的计算函数拟动力
# 输入参数
# H（坡高）
# a（坡角）
# p（重度）
# c（粘聚力）
# q（摩擦角）
# FS（初始安全系数）
# Kh（水平地震力系数）
# Kv（竖直地震力系数）
# fh（地震横波频率）
# fv（地震纵波频率）
# t（初始相位）
# vs（横波波速）
# vp（纵波波速）
# Xl（滑裂面从坡底切入点坐标）
# Xr（滑裂面从坡顶切入点坐标）
# B（滑裂面初始角）
# n（条分数目）
# 输出参数
# Fs（安全系数）
# H=50;a=25;p=21;c=20;q=30;FS=1.25;Xl=0;Xr=110;B=-20;n=6;
    a=math.radians(a)
    q=math.radians(q)
    k1=math.tan(a)
    k2=math.tan(q)
    b1=(Xr-Xl)/n-0.1
    db=(2*((Xr-Xl)-n*b1))/(n*(n-1))
    b=np.zeros(n)
    for i in range(n):
        b[i]=b1+i*db
    x=np.zeros(n+1)
    x[0]=0
    for i in range(n):
        x[i+1]=((i+1)*(b[0]+b[i]))/2
    O=(math.degrees(math.atan((H/(Xr-Xl))))-B)/n
    h=np.zeros(len(x))
    for i in range(len(x)):
        if x[i]==0:
            h[i]=0
        elif x[i]>0 and x[i]<=H/k1:
            h[i]=x[i]*(k1-math.tan(math.radians((i)*O+B)))
        else:
            h[i]=H-(x[i]*math.tan(math.radians((i)*O+B)))
            if h[i]<0:
                h[i]=0
    Q = np.zeros(n)
    for i in range(n):
        if x[i] <= H / k1 and x[i + 1] <= H / k1:
            Q[i] = math.atan((h[i] - h[i + 1] + b[i] * k1) / b[i])
        elif x[i] >= H / k1 and x[i + 1] >= H / k1:
            Q[i] = math.atan((h[i] - h[i + 1]) / b[i])
        else:
            Q[i] = math.atan((h[i] - h[i + 1] + H - x[i] * k1) / b[i])
    hh=np.zeros(len(x)-1)
    for j in range(len(x)-1):
        hh[j]=(h[j]+h[j+1])/2
    S=np.zeros(n)
    C=np.zeros(n)
    L = np.zeros(n)
    W = np.zeros(n)
    for i in range(n):
        S[i]=math.sin(Q[i])
        C[i]=math.cos(Q[i])
        L[i] = b[i] / C[i]
        W[i] = p * b[i] * hh[i]
    Fh=np.zeros(n)
    for i in range(n):
        Fh[i]=Kh*p*b[i]*vs/(2*(math.pi)*(fh+2.220446049250313e-16))*((math.cos(2*(math.pi)*fh*(t-H/(vs+2.220446049250313e-16))))-math.cos(2*(math.pi)*fh*(t-(H-hh[i])/(vs+2.220446049250313e-16))))
    Fv=np.zeros(n)
    for i in range(n):
        Fv[i]=Kv*p*b[i]*vp/(2*(math.pi)*(fv+2.220446049250313e-16))*((math.cos(2*(math.pi)*fv*(t-H/(vp+2.220446049250313e-16))))-math.cos(2*(math.pi)*fv*(t-(H-hh[i])/(vp+2.220446049250313e-16))))
    m=np.zeros(n)
    for i in range(n-1):
        m[n-1]=math.cos(0-Q[n-1])-k2*math.sin(0-Q[n-1])
        m[i]=math.cos(Q[i+1]-Q[i])-k2*math.sin(Q[i+1]-Q[i])
    P = np.zeros(n)
    P[0]=FS*((W[n-1]-Fv[n-1])*S[n-1]+Fh[n-1]*C[n-1])-(c*L[n-1]+((W[n-1]-Fv[n-1])*C[n-1]-Fh[n-1]*S[n-1])*k2)
    if P[0] < 0:
        P[0] = 0
    for i in range(1,n):
        P[i]=FS*((W[n-i-1]-Fv[n-i-1])*S[n-i-1]+Fh[n-i-1]*C[n-i-1])-(c*L[n-i-1]+((W[n-i-1]-Fv[n-i-1])*C[n-i-1]-Fh[n-i-1]*S[n-i-1])*k2)+P[i-1]*m[n-i-1]
    P1 = np.zeros(n-1)
    P1 = P[0:n-1]
    arr = np.array(P1)
    if ((arr < 0).any()) == 1:
        g=np.argwhere(P1<0)
        g1 = g[0]
        g2 = g1[0]
        P[g2] = 0
        for i in range(g2+1,n):
            P[i]=FS*((W[n-i-1]-Fv[n-i-1])*S[n-i-1]+Fh[n-i-1]*C[n-i-1])-(c*L[n-i-1]+((W[n-i-1]-Fv[n-i-1])*C[n-i-1]-Fh[n-i-1]*S[n-i-1])*k2)+P[i-1]*m[n-i-1]
    Fs=0
    if abs(P[n - 1]) <= 1:
        Fs = FS
    else:
        while P[n-1] > 1:
            FS = FS - 0.001
            P[0]=FS*((W[n-1]-Fv[n-1])*S[n-1]+Fh[n-1]*C[n-1])-(c*L[n-1]+((W[n-1]-Fv[n-1])*C[n-1]-Fh[n-1]*S[n-1])*k2)
            if P[0] < 0:
                P[0] = 0
            for i in range(1,n):
                P[i]=FS*((W[n-i-1]-Fv[n-i-1])*S[n-i-1]+Fh[n-i-1]*C[n-i-1])-(c*L[n-i-1]+((W[n-i-1]-Fv[n-i-1])*C[n-i-1]-Fh[n-i-1]*S[n-i-1])*k2)+P[i-1]*m[n-i-1]
            P1 = np.zeros(n-1)
            P1 = P[0:n - 1]
            arr = np.array(P1)
            if ((arr < 0).any()) == 1:
                g = np.argwhere(P1 < 0)
                g1 = g[0]
                g2 = g1[0]
                P[g2] = 0
                for i in range(g2 + 1, n):
                    P[i]=FS*((W[n-i-1]-Fv[n-i-1])*S[n-i-1]+Fh[n-i-1]*C[n-i-1])-(c*L[n-i-1]+((W[n-i-1]-Fv[n-i-1])*C[n-i-1]-Fh[n-i-1]*S[n-i-1])*k2)+P[i-1]*m[n-i-1]
        while P[n-1] < -1:
            FS = FS + 0.001
            P[0]=FS*((W[n-1]-Fv[n-1])*S[n-1]+Fh[n-1]*C[n-1])-(c*L[n-1]+((W[n-1]-Fv[n-1])*C[n-1]-Fh[n-1]*S[n-1])*k2)
            if P[0] < 0:
                P[0] = 0
            for i in range(1,n):
                P[i]=FS*((W[n-i-1]-Fv[n-i-1])*S[n-i-1]+Fh[n-i-1]*C[n-i-1])-(c*L[n-i-1]+((W[n-i-1]-Fv[n-i-1])*C[n-i-1]-Fh[n-i-1]*S[n-i-1])*k2)+P[i-1]*m[n-i-1]
            P1 = np.zeros(n-1)
            P1 = P[0:n - 1]
            arr = np.array(P1)
            if ((arr < 0).any()) == 1:
                g = np.argwhere(P1 < 0)
                g1 = g[0]
                g2 = g1[0]
                P[g2] = 0
                for i in range(g2+1,n):
                    P[i]=FS*((W[n-i-1]-Fv[n-i-1])*S[n-i-1]+Fh[n-i-1]*C[n-i-1])-(c*L[n-i-1]+((W[n-i-1]-Fv[n-i-1])*C[n-i-1]-Fh[n-i-1]*S[n-i-1])*k2)+P[i-1]*m[n-i-1]

    Fs = FS
    print(Fs)
    return Fs

# H=50;a=25;p=21;c=20;q=30;FS=1.25;Kh=0.1;Kv=0;fh=2;fv=0;t=0.2;vs=300;vp=0;Xl=0;Xr=110;B=-20;n=6;Fs=1.590
# H=10;a=25;p=21;c=20;q=30;FS=1.25;Kh=0.1;Kv=0;fh=0.5;fv=0;t=1;vs=100;vp=0;Xl=0;Xr=25;B=-20;n=6;Fs=2.577
U1(10,25,21,20,30,1.25,0.1,0,0.5,0,1,100,0,0,25,-20,6)
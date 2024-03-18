Sn = float(input('Sn'))
Un = float(input('Un'))
Uk12 = float(input('Uk12'))
Uk13 = float(input('Uk13'))
Uk23 = float(input('Uk23'))
Pk_12 = float(input('Pk_12'))
Pk_23 = float(input('Pk_23'))
Pk_13 = float(input('Pk_13'))
I0 = float(input('I0'))
P0 = float(input('P0'))
Pk12 = Pk_12
Pk23 = 4*Pk_23
Pk13 = 4*Pk_13
Pk1 = (Pk13+Pk12-Pk23)/2
Pk2 = (-Pk13+Pk12+Pk23)/2
Pk3 = (Pk13-Pk12+Pk23)/2
Uk1 = (Uk12+Uk13-Uk23)/2
Uk2 = (Uk12-Uk13+Uk23)/2
Uk3 = (-Uk12+Uk13+Uk23)/2
Xt1 = (Uk1/100) * Un**2/Sn
Xt2 = (Uk2/100) * Un**2/Sn
Xt3 = (Uk3/100) * Un**2/Sn
Rt1 = (Pk1*Un**2)/(Sn**2 * 1000)
Rt2 = (Pk2*Un**2)/(Sn**2 * 1000)
Rt3 = (Pk3*Un**2)/(Sn**2 * 1000)
Gt = P0/(Un**2 * 1000)
Bt = I0*Sn/(100*Un**2)
print('励磁电导：',Bt)
print('励磁电纳：',Gt)
print('各侧电阻高压：',round(Rt1,3))
print('各侧电阻中压：',round(Rt2,3))
print('各侧电阻低压：',round(Rt3,3))
print('各侧电阻高压：',round(Xt1,3))
print('各侧电抗中压：',round(Xt2,3))
print('各侧电抗低压：',round(Xt3,3))





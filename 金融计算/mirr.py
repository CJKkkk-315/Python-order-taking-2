from numpy_financial import mirr,irr,npv
# 初期资产原值
s1 = 0
# 后续每年收益
s2 = [0,0,0,0,0]
# 资产原值贷款额的年利率
t1 = 0
# 再投资收益的年利率
t2 = 0
res = mirr([-s1]+s2,t1,t2)
print(res)

from numpy_financial import mirr,irr,npv
# 初期资产原值
s1 = 0
# 后续每年收益
s2 = [0,0,0,0,0]
res = irr([-s1]+s2)
print(res)
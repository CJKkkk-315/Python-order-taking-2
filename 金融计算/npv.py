from numpy_financial import mirr,irr,npv
# 初期资产原值
s1 = 0
# 后续每年收益
s2 = [0,0,0,0,0]
# 年贴现率
t1 = 0
res = npv(t1,[-s1]+s2)
print(res)
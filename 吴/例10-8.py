str = input('请输入字符串：')
isnumeric = True
for i in range(len(str)):
    if str[i] not in '0123456789':
        isnumeric = False
if isnumeric:
    print(str,'是数字字符串')
else:
    print(str,'含有非数字字符')
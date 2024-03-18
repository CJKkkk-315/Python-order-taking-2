from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import random
import csv
key = b'1234567812345678' #秘钥，b就是表示为bytes类型
data = []
f = open('密码库.csv','r',encoding='utf-8')
fcsv = csv.reader(f)
for row in fcsv:
    data.append(row)
f.close()


def completion(s):
    need = (16 - len(s) % 16)
    for i in range(need):
        s += '\0'.encode('utf-8')
    return s
def encrypt(password):
    password = password.encode('utf-8')
    aes = AES.new(key, AES.MODE_ECB)
    password = completion(password)
    password = aes.encrypt(password)
    password = b2a_hex(password)
    password = password.decode()
    return password
def decrypt(password):
    aes = AES.new(key, AES.MODE_ECB)
    password = aes.decrypt(a2b_hex(password))
    password = password.rstrip('\0'.encode('utf-8'))
    password = password.decode()
    return password
def save_password():
    randompass1 = list('1234567890abcdefghijklmnopqrstuvwxyz')
    randompass2 = list('abcdefghijklmnopqrstuvwxyz')
    info = '''
    请选择
    1.自动生成密码
    2.输入密码
    '''
    n = int(input('保存密码条数：'))
    for i in range(n):
        name = input('网站名称：')
        url = input('url：')
        date = input('生成日期：')
        username = input('用户名：')
        print(info)
        c = input('你的选择：')
        if c == '2':
            password = input('请输入密码：')
        elif c == '1':
            password = []
            l = int(input('密码长度：'))
            flag1 = int(input('是否包含大写字母(是:1/否:0)：'))
            flag2 = int(input('是否包含特殊符号(是:1/否:0)：'))
            flag3 = int(input('是否包含数字(是:1/否:0)：'))
            if flag1:
                password.append(chr(ord('A')+random.randint(1,25)))
            if flag2:
                password .append('#')
            if flag3:
                password += random.sample(randompass1,l-len(password))
            else:
                password += random.sample(randompass2, l - len(password))
            random.shuffle(password)
            password = ''.join(password)
            print('生成的密码为：',password)
        password = encrypt(password)
        with open('密码库.csv', 'a+', newline='', encoding='utf-8') as f:
            fcsv = csv.writer(f)
            fcsv.writerow([name,url,date,username,password])
            data.append([name,url,date,username,password])
def print_password():
    pw = input('请输入管理密码：')
    if pw == '123456':
        for j in data:
            print(j[0],j[1],j[2],j[3],decrypt(j[4]))
    else:
        print('密码错误！')
        for j in data:
            print(j[0],j[1],j[2],j[3],j[4])


if __name__ == '__main__':
    info = '''
    请选择
    1.保存密码
    2.查看密码库
    3.退出
    '''
    while True:
        print(info)
        c = input('请输入你的选择：')
        if c == '1':
            save_password()
        elif c == '2':
            print_password()
        else:
            break
import string


def rot13(text):
    '''实现rot13的解密算法'''
    # TODO: 请补写代码，完成功能
    d = {}
    for i in range(26):
        d[chr(ord('a')+i)] = chr(ord('a')+(i+13)%26)
        d[chr(ord('A') + i)] = chr(ord('A') + (i + 13) % 26)
    result = ''
    for i in text:
        if i in d:
            result += d[i]
        else:
            result += i
    return result


if __name__ == '__main__':
    plaintext = 'How can you tell an extrovert from an introvert at NSA?'
    secret = "Va gur ryringbef,gur rkgebireg ybbxf ng gur BGURE thl'f fubrf."
    print("ROT13 Result:")
    print(rot13(plaintext))
    print(rot13(secret))

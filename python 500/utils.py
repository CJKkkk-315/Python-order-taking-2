'''模块：帮助函数
'''

# pylint: disable=C0103

def is_int(part):
    '''
    判断给定的字符串是否是整数。
    >>> is_int('1.5')
    False
    >>> is_int('1')
    True
    >>> is_int('12241324')
    True
    >>> is_int('+1')
    True
    >>> is_int('-12241324')
    True
    >>> is_int('-abcd')
    False
    '''
    offset = 1 if part[0] in '-+' else 0

    for ch in part[offset:]:
        if ch not in '0123456789':
            return False

    return True

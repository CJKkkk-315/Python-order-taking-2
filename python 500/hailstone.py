# pylint: disable = C0114, C0116, C0103
from py4204 import measure_time


def hailstone(k):
    """return the length of hailstone of k.
    """
    length = 1
    while k != 1:
        length += 1
        if k % 2 == 0:
            k /= 2
        else:
            k = k * 3 + 1
    return length


def find_longest_hailstone(n):
    '''返回区间[2, n+1)中hailstone序列最长的整数值及其序列长度
    '''
    value, longest = 1, 1
    # todo2: 请在下面补写代码，完成函数功能
    for i in range(2,n+1):
        if hailstone(i) > longest:
            value = i
            longest = hailstone(i)
    return value, longest


def main():
    n = 100000  #int(input("Please enter a positive number:"))
    longest, value = find_longest_hailstone(n)
    print(f"hailstone: range={n} longest={longest} value={value}")


if __name__ == "__main__":
    measure_time(main, 1)

'''
问题：已知三角形的两边a,b以及夹角sita，求第三边c的长度。
思路：按照输入-处理-输出的思路来考虑问题。
   输入：使用input函数,输入格式为 "3,4,90"，数字使用","分割。
   处理：利用cos公式计算c值  c**2 = a**2+b**2-2*a*b*sin(sita*pi/180)
   详细：
        1)先把用户输入的字符串line使用split分成多个部分；
        2)如果分成了三个部分，则符合要求继续处理，否则报
        错："无效输入(1)"；
        3)如果三个部分都是整数，则符合要求继续处理，否则
        报错："无效输入(2)"；
        4)把三个部分转换成整数；
        5)*如果两边长均大于0，且角度值在(0,180)之间，则符
        合要求继续处理，否则报错："无效输入(3)"；代码没有
        实现；
        6)使用cos函数计算第3边；
        7)输出最后计算的结果。
   输出：如果输入正确，处理结果为 "c=5.0"；如果输入不正确，提示用户"无效输入"
'''
# pylint: disable=C0103

from math import cos, sqrt, pi
from utils import is_int

def main():
    '''已知两边及夹角，求第三边。
    '''
    line = input("输入两边及夹角(用逗号分隔):")
    parts = line.split(',')
    if len(parts) == 3:
        if is_int(parts[0]) and is_int(parts[1]) and is_int(parts[2]):
            a, b, sita = int(parts[0]), int(parts[1]), int(parts[2])
            if a > 0 and b > 0 and sita > 0 and sita < 180:
                c = sqrt(a*a + b*b - 2*a*b*cos(pi*sita/180))
                print(f"c={c:.2f}")
            else:
                print("无效输入(3)")
        else:
            print("无效输入(2)")
    else:
        print("无效输入(1)")

if __name__ == "__main__":
    main()

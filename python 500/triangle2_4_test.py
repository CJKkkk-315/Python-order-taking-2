'''
>>> import os
>>> import sys
>>> dir_rel = os.path.dirname(os.path.abspath(__file__))
>>> sys.path.append(dir_rel)
>>> def redirect_input(*lines):
...     import io
...     sys.stdin = io.StringIO(chr(10).join(lines))
... 
>>> redirect_input('6,6,60','a,b,80','90,80,70,60','-10,20,80','10,20,270')
>>> from triangle2 import main
>>> main()
输入两边及夹角(用逗号分隔):c=6.00
>>> main()
输入两边及夹角(用逗号分隔):无效输入(2)
>>> main()
输入两边及夹角(用逗号分隔):无效输入(1)
>>> main()
输入两边及夹角(用逗号分隔):无效输入(3)
>>> main()
输入两边及夹角(用逗号分隔):无效输入(3)
'''
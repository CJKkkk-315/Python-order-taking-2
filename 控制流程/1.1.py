n1 = float(input('Enter a number (such as 3.5 or 4.5):'))
n2 = float(input('Enter a second number:'))
if n1 > n2 :
    print('The first number is larger')
else :
    print('The first number is smaller')
if abs(n1-n2) <= 0.01:
    print('The numbers are close together')
elif abs(n1-n2) == 1:
    print('The numbers are one apart')
if n1*n2 > 0:
    print('The numbers have the same sign')
else :
    print('The numbers have the different sign')
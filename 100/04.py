def division_function(number_one,number_two):
    if number_two == 0:
        raise ZeroDivisionError('divide zero error')

    return number_one/number_two
print(division_function(0,100))
print(division_function(200,10))
print(division_function(20,0))


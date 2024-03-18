def summary_odd_number(start_number,end_number):
    s = 0
    for i in range(start_number,end_number):
        if i%2 == 1:
            s += i
    return s
print(summary_odd_number(0,100))
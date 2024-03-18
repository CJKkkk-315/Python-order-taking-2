'''common functions for course Python Programming
'''
import time


def output(alist, nums_per_row=6):
    '''output alist elements with each row for nums_per_row
    elments
    '''
    for idx, value in enumerate(alist, 1):
        print(f"{value:10}", end="")
        if idx % nums_per_row == 0:
            print()


def get_number(msg="Please enter an integer(>0):"):
    '''read from input with a negative or positive number,
    otherwise dead looping
    '''
    while True:
        str_in = input(msg)
        str_in = str_in.strip()
        is_number = True

        idx = 1 if str_in[0] == '-' else 0

        for char in str_in[idx:]:
            if char not in '0123456789':
                is_number = False
                break
        if is_number is False:
            print("input error, please try again!")

        return int(str_in)


def measure_time(f, times=100):
    '''measure the total running time for function f executing times
    '''
    start = time.time()
    for _ in range(times):
        f()
    end = time.time()
    print(f'{f.__name__:10s} excuting {times} times using {end-start:.4f}s')

"""
10. DECORATOR + RECURSION INTERACTION
*************************************
    * Create a recursive function that performs a calculation.
    * Apply a decorator that logs information about each function call.
    * Observe how the decorator behaves during recursive execution and explain the result.
"""

def my_decorator(func):
    def wrapper(n):
        print(f'\033[1;34;40mLOG\033[0m : Remaining digits to count ({n})')
        return func(n)
    return wrapper

@my_decorator
def count_digits(n):
    if(n == 0):
        return 0
    return 1 + count_digits(n//10)

num = 4556735
print(f'\033[0;32;47mNumber of Digits in {num} = {count_digits(756486)}\033[0m')


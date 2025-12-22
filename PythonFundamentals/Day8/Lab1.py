"""
1.  EXECUTION TIME DECORATOR
*****************************
    * Create a decorator that measures how long a function takes to execute.
    * The decorator should print the execution time after the function has finished.
    * Apply the decorator to a function that processes a list of numbers.
"""
from timeit import default_timer as timer
def my_decorator(func):
    def wrapper(list1):
        t_start = timer()
        r = func(list1)
        s_stop = timer()
        print(f'Execution time after function {s_stop - t_start}') 
    return wrapper

@my_decorator
def greater8(list1):
    result = [i for i in list1 if i >= 8]
    return result

greater8([1,5,9,3,2,10,30,56,4,8,51,9,36])
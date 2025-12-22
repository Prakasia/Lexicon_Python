# from math import sqrt as sq

# from Day8 import sample_func

# print(sample_func.abs_diff(10,4))

"""
                    DECORATOR METHOD
"""
# def my_decorator(func):
#     def wrapper():
#         print('Something is happening before the func call.')
#         func()
#         print('Something is happening after the func is called.')
#     return wrapper

# @my_decorator
# def say_hello():
#     print('Hello')

# #call a decorator function
# say_hello()


# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f'Arguments passed to the function: {args} and {kwargs}')
#         result = func(*args, **kwargs)
#         print(f'Function returned results : {result}')
#         return result
#     return wrapper

# @my_decorator
# def add(a, b):
#     return a+b

# add(10,5)


"""
                STATIC METHODS
"""

# does not have self, 
# does not interact with instance attribute
# class MathHelper:
#     @staticmethod
#     def addnumbers(x,y):
#         return (x+y)

#staticmethod, @property, @classmethod
# @functools.wraps

# import functools

# def my_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f'Calling {func.__name__}')
#         return func(*args, **kwargs)
#     return wrapper

# @my_decorator
# def greetfunction(name):
#     print(f'Hello {name}!!!')

# greetfunction('Steve Thomas')


"""
                FUNCTIONAL PROGRAMMING
"""

# HIGHER ORDER FUNCTIONS

# def apply_function(func, value):
#     return func(value)

# def square(x):
#     return (x*x)

# def cube(x):
#     return x ** 3

# # Pass functions as arguments
# print(apply_function(square,3))
# print(apply_function(cube,3))

# print(apply_function(lambda s:s+5, 7))

"""
                RECURSION FUNCTIONS
"""

# FACTORIAL CLASSIC EXAMPLE

# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)

# print(fact(5)) # 5*4*3*2*1 = 120

#memoization
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if (n <= 1):
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))
print(fib.cache_info())
 
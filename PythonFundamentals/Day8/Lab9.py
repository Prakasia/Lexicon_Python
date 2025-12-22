"""
9.  RECURSIVE PROBLEM DESIGN
*****************************
    * Design a problem that can naturally be solved using recursion.
    * Implement a recursive solution.
    * Optimize the solution using memoization.
    * Demonstrate the difference in performance or behavior.
"""

#COUNTING DIGITS IN A NUMBER

import time as t
from functools import lru_cache


def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

@lru_cache(maxsize=None)
def fib_memo(n):
    if n <= 1:
        return n
    return fib_memo(n-1) + fib_memo(n-2)



print('FIBONACCI WITHOUT MEMOIZATION')
st = t.time()
print(fib(30))
print(f'Recursion without memoization, time = {t.time() - st} ')
print('FIBONACCI WITH MEMOIZATION')
st = t.time()
print(fib_memo(30))
print(f'Recursion with memoization, time = {t.time() - st}')
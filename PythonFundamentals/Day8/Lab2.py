"""
2.      FUNCTIONAL LIST TRANSFORMATION
        *******************************
    * Use a functional approach to transform a list of numbers.
    * Apply one operation that changes the values and one operation that filters values.
    * The solution must use lambda expressions together with built-in higher-order functions.
"""

def change_values(x):
    new_values = []
    new_values = [i** 3 for i in x]
    return new_values

def filter_values(y):
    return filter(lambda i : i%2 == 0, y)

values = [1,2,3,4,5]
print(f'Original values = {values}')
print(f'After first operation = {change_values(values)}')
print(f'Higher order function value = {list(filter_values(change_values(values)))}')
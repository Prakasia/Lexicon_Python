"""
7. PRESERVING FUNCTION METADATA
*******************************
    * Create a decorator that wraps a function.
    * Ensure that the wrapped function retains its original metadata.
    * Verify this by inspecting the function’s name and documentation before and after
        decoration.
"""
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(s):
        print(f'Before calling function {func.__name__}')
        result = func(s)
        print(f'After calling function {func.__name__}')
        return result
    return wrapper

@my_decorator
def greeting(name):
    """
    Greeting message
    """
    return f"Hello {name} !!"

# print('Before decoration: ')
# print(f'*******************')
print(f'{greeting("Alice")}')
# print(f'Function name : {greeting.__name__}')
# print(f'Function doc : {greeting.__doc__}')
print(f'After decoration :')
print(f'*******************')
print(f'Function name : {greeting.__name__}')
print(f'Function doc : {greeting.__doc__}')


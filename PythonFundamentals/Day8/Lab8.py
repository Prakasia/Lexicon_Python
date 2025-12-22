"""
8. FLEXIBLE DECORATOR WITH ARGUMENTS
************************************
    * Create a decorator that accepts its own arguments.
    * The decorator should alter its behavior based on the provided arguments.
    * Apply the decorator to multiple functions using different decorator arguments.
"""

def decorator_with_args(deco_args):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print(f'Calling {func.__name__} with {deco_args}')
            result = func(*args, **kwargs)
            return result
        return wrapper  
    return my_decorator

@decorator_with_args("ADD")
def addnums(a,b):
    return a+b

@decorator_with_args("GREET")
def greeting(name):
    return f'Hello {name}!!'

print(addnums(10,10))
print(greeting('Alice'))
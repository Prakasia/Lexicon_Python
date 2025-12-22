"""
4. DECORATOR THAT MODIFIES RETURN VALUES
*****************************************
    * Create a decorator that intercepts the return value of a function.
    * Modify the return value in some meaningful way before returning it.
    * Apply the decorator to at least one function and demonstrate the effect.
"""

def my_decorator(func):
    def wrapper(st):
        s = func(st)
        return (s + " Modified again")
    return wrapper


@my_decorator
def converttoupper(st):
    return st.upper()

m = "Python"
print(converttoupper(m))

"""
    *ARGS AND KWARGS
    Goal: Practice flexible function parameters and argument unpacking.
    *****************
Create functions that:
1. Accept any number of values using *args and return their sum
2. Accept any number of values using *args and return the maximum
3. Accept any number of keyword arguments using **kwargs and print them
4. Combine a, *args, and **kwargs and print all arguments in a readable way

"""
# *args
def add(*args):             
    return sum(args)
# *args
def maximum(*args):
    return(max(args))
# **kwargs
def func1(**kwargs):
    print('kwargs = {}'.format(kwargs))

# **kwargs, *args, a
def func2(a, *args, **kwargs):
    print('Value of a = {}'.format(a))
    print('Value of args = {}'.format(args))
    print('Values of kwargs :')
    for key, value in kwargs.items():
        print('{} : {}'.format(key, value))


val = add(10,20,30,40,50)
print('Sum = {}'.format(val))
val = maximum(10, 100, 30, 45, 11, 7, -54)
print('Maximum = {}'.format(val))
func1(name = 'Alice', age = 30, subject = 'Python', city = 'Stockholm')
func2('names', 4, 2, 3, 65, k1 = 'Alice', k2 = 'Bob', k3 = 'Anna', k4 = 'Catherine')

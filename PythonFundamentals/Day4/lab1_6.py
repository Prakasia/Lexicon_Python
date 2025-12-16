"""
Docstring for Day4.lab1
1. LOCAL VS GLOBAL VARIABLE
*****************************
Create a program that demonstrates the difference between a local variable and a global variable. 
The program should clearly show both values.
"""
# x = 100

# def variable_scope():
#     y = 20
#     print('Inside function value of y = {} - LOCAL VARIABLE'.format(y))
#     print('Inside function value of x = {} - GLOBAL VARIABLE'.format(x))

# variable_scope()
# print('Outside function value of variable x = {} - GLOBAL VARIABLE'.format(x))
# print('Variable y cannot be accessed since it is local to the function \'variable_scope()\'')


# -----------------------------------------------------------------------------

"""
2. FUNCTION USING A GLOBAL VARIABLE
***********************************
Write a function that reads the value of a global variable without changing it. 
Show in the output that the global value remains the same after the function call.
"""

# x = 200

# def global_variable():
#     b = x
#     print('The value of global variable inside function is {}'.format(b))

# print('The value of global variable before function call : {}'.format(x))
# global_variable()
# print('The value of global variable after function call is {}'.format(x))

# -----------------------------------------------------------------------------

"""
3. FUNCTION THAT MODIFIES A GLOBAL VARIABLE
********************************************
Write a program where a function changes the value of a global variable using the global keyword.
Display the value before and after the function call.
"""

# global_variable = 'HelloWorld'

# def change_global_variable():
#     global global_variable
#     print('Inside Function')
#     print('Before Changing Global variable = {}'.format(global_variable))
#     global_variable = 'HelloPythonWorld'
#     print('After Changing Global variable = {}'.format(global_variable))

# print('Global variable before function call = {}'.format(global_variable))
# change_global_variable()
# print('Global variable after function call = {}'.format(global_variable))

# -----------------------------------------------------------------------------

"""
4. LOCAL VARIABLE SHADOWING THE GLOBAL VARIABLE
***********************************************
Create an example where a global variable and a local variable have the same name. The program
should demonstrate which value is used inside the function and which is used outside.
"""

# name = 'Alice'

# def function_call():
#     name = 'Bob'
#     print('Inside the function \'name\' = {}'.format(name))

# print('Before function call \'name\' = {}'.format(name))
# function_call()
# print('After function call \'name\' = {}'.format(name))

# -----------------------------------------------------------------------------


"""
5. INNER FUNCTION AND LEGB RULE
******************************
Write a function that contains an inner function. Use print statements to show 
which version of a name is being used (local, enclosing, or global).
"""

name = 'Global variable'

def outer_func1():
    name = 'Enclosing variable'
    print('Inside the function call')
    print('In Outer function \'name\' = {}'.format(name))

    def inner_func():
        name = 'Local Variable'
        print('In the Inner function \'name\' = {}'.format(name))
    
    inner_func()

print('The value of global variable \'name\'  = {}'.format(name))
outer_func1()
print('After function call the value of global variable is {}'.format(name))

# -----------------------------------------------------------------------------

"""
6. USING NONLOCAL
*****************
Create an example where an inner function modifies a variable in the enclosing function using the
nonlocal keyword. Show the change before and after.
"""

def outer_func():
    name = 'Enclosing variable'
    print('Inside the function call')
    print('Before calling inner function \'name\' = {}'.format(name))

    def inner_func():
        nonlocal name 
        name = 'Changed to local variable'
        print('In the Inner function \'name\' = {}'.format(name))
    
    inner_func()
    print('After calling the inner function \'name\' = {}'.format(name))

outer_func()
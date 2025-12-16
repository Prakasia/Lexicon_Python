# x = 15
# def printer():
#     x=30
#     return x
# print(x)
# print(printer())
# print(x)

# 1. Name assignment will create or change local names by default
# 2. Name references search (at most) four scopes, these are (LEGB rule)
    # Local - Name assigned within a function (def or lambda) and not declared global in that function
    # Enclosing functions - Name in the local scope of any and all enclosing func, inner or outer
    # Global - Names assigned at the top level of a module file or declared globally in a def within a file
    # Built-in - Built-in names, module, range...
# 3. Names declared in global and nonlocal statement map assigned name to enclosing module and function scopes

# Examples 
# Local x is local:
f = lambda x:x**2

# Enclosing func

# name ='This is some global name'

# def greet():
#     name = 'Erick'

#     def hello():
#         print('Hello' + name)
#     hello()

# greet()
# print(name)

# global keyword affects the global value inside a function

# class

class Sample():
    pass

x = Sample()

print(type(x))

# Class : user defined template for creating objects.
# Eg : fruits : combining data and functions into a bundle
# create objects of this class

# attributes: variables defined in the class

# Instance attribute : within an object
# Class attribute within the class accessible with class

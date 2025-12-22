"""
                PYTHONIC CLASSES AND PROPERTIES
                *******************************
1. Create a class with a property and setter. Create a class with one attribute that
can only be accessed and modified through a property and setter. Include a
method that performs a calculation using the attribute.
"""

# class Square:
#     def __init__(self, side):
#         self.side = side

#     @property 
#     def side_value(self):
#         return self.side
    
#     @side_value.setter
#     def side_value(self,value):
#         self.side = value

#     def sq_area(self):
#         return self.side * self.side
    
# s = Square(5)
# print(f'Side = {s.side_value}\t Area = {s.sq_area()}')

# s.side_value = 10
# print(f'New Side = {s.side_value}\t New Area = {s.sq_area()}')
# print('-----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
        
"""
2. Create a class with a clean __str__ representation. Create a class with at least
three attributes and implement __str__ to make printed objects readable and
nicely formatted.
"""

# class Person1:
#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city

#     def __str__(self):
#         return f'{self.name} is {self.age} years old and lives in {self.city} city'
    
# p1 = Person1('Alice', 31, 'Uppsala')
# print(p1)
# print('-----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------

"""
3. Create a class with a meaningful __repr__. Create a class where __repr__ returns
a string that could realistically recreate the object.
"""

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def __repr__(self):
#         return f"Rectangle({self.length},{self.width})"
    
# r1 = Rectangle(5, 10)
# print(repr(r1))
# #Can recreate the obect using the return string from __repr__
# r2 = repr(r1)
# print(r2)

# print('-----------------------------------------------------------------------------')
        
# -----------------------------------------------------------------------------

"""
4. Create a class that initializes from **kwargs. Write a class where attributes are
automatically created from keyword arguments, even when different objects
receive different arguments.
"""

# class Something:
#     def __init__(self, data:dict):
#         self.__dict__ = data

#     def __str__(self):
#         return ', '.join(f'{key} : {value}' for key, value in self.__dict__.items())
    

# data_dict1 = {
#     'Name' : 'Alice',
#     'Age' : 30,
#     'Email' : 'alice@gmail.com'
# }

# data_dict2 = {
#     'Country' : 'Sweden',
#     'Language' : 'Svenska',
#     "country-code" : '+46',
#     'Capital' : 'Stockholm'
# }

# s1 = Something(data_dict1)
# print(s1)
# s2 = Something(data_dict2)
# print(s2)

# print('-----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------

"""
5. Create a class that builds its string using a comprehension. Write a class whose
__str__ method constructs its output using a comprehension and join().
"""

class Person2:
    def __init__(self, data:dict):
        self.__dict__ = data

    def __str__(self):
        return ('\033[1;34;40m | \033[0m').join(f'{key} : {value}' for key, value in self.__dict__.items())
    
data_dict1 = {
    'Name' : 'Alice',
    'Age' : 30,
    'Email' : 'alice@gmail.com',
    'City' : 'Stockholm',
    'Phone no' : 72345678
}

p1 = Person2(data_dict1)
print(p1)

print('-----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------
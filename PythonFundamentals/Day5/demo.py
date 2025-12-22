"""
Properties in python class
"""


# class Person:
#     def __init__(self,name, email, age):
#         self.name = name 
#         self.email = email
#         self.age = age

#     def __str__(self):
#         return f'{self.name} is {self.age} years old and email {self.email}'
    

# p1 = Person('Alice', 'alice@email.com', 30)
# p2 = Person('Bob', 'bob@email.com', 34)

# print(p1)
# print(p2)

# # this is possible in python but not recommended
# p1.phone = '072213123'
# print(p1.phone)

# class Person:
#     def __init__(self, **kwargs):
#         self.__dict__ = kwargs

#     def __str__(self):
#         return f'{self.name} is {self.age} years old'
    
# p1 = Person(name = 'Alice', age = 38)
# print(p1)
# p2 = Person(name = 'Bob',) 
# print(p2)
# return f'{self.name} is {self.age} years old'
#                              ^^^^^^^^
# AttributeError: 'Person' object has no attribute 'age'

"""
showing kwargs in class
"""
# class Something:
#     def __init__(self, data:dict):
#         self.__dict__ = data

#     def __str__(self):
#         # str_rep = ''
#         # for key, value in self.__dict__.items():
#         #     str_rep += f'{key} = {value}, '
#         # return str_rep
#         return ', '.join(f'{key} = {value}' for key, value in self.__dict__.items())
        
    
# data_dict1 = {
#     'a' : 10,
#     'b' : 20,
#     'name' : 'One'
# }

# data_dict2 = {
#     'a' : 24,
#     'b' : 9
# }

# s1 = Something(data_dict1)
# print(s1)
# s2 = Something(data_dict2)
# print(s2)

"""
String representation
"""
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     # String representation of Object 
#     # Usually used on error messages for the users 
#     def __repr__(self):
#         return f'Point({self.x}, {self.y})'
    
#     # Usually for developers
#     def __str__(self):
#         return f'Point with x = {self.x} and y = {self.y}'

# point1 = Point(10, 20)
# # print(point1.x, point1.y)

# print(point1)
# print(repr(point1))

"""
__eq__
"""
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
    
# point1 = Point(10,20)
# point2 = Point(10,20)

# print(point1 == point2)

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def swap_xy(self):
#         self.x, self.y = self.y, self.x

# point1 = Point(10,20)
# print(point1.x,point1.y)
# point1.swap_xy()
# print(point1.x,point1.y)


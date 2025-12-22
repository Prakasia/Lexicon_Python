"""     
            POLYMORPHISM
"""

# DUCK TYPING

# def make_it_upper(x):
#     return x.upper()

# class Shouty:
#     def __init__(self,text):
#         self.text = text

#     def upper(self):
#         return self.text.upper() + '!!!'
    
# print(make_it_upper('hello'))
# print(make_it_upper(Shouty('hello')))


# def safe_upper(x):
#     try:
#         return x.upper()
#     except AttributeError:
#         return str(x).upper()
    
# print(safe_upper('hi'))
# print(safe_upper(123))
# print(safe_upper(Shouty('welcome')))
  
""" 

    we define a base class
    we define sub classes
    Subclasses will overrides methods

"""
# class Animal:
#     def speak(self):
#         raise NotImplementedError
    
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
    
# class Cat(Animal):
#     def speak(self):
#         return "Mew!"
    
# print(Dog().speak())
# print(Cat().speak())

""" 
        ABSTRACT CLASSES 
        
"""

# from abc import ABC, abstractmethod
# import json as j

# class Serializer(ABC):
#     @abstractmethod
#     def serialize(self, obj):
#         pass

# class JsonSerializer(Serializer):
#     def serialize(self, obj):
#         return j.dumps(obj)
    
# js = JsonSerializer()
# print(js.serialize({"name : Shalu"}))
"""
5.  FEEL THE PAIN OF ISINSTANCE
Objective: Recognize why type-check chains do not scale.
*********************************************************
Instructions:
1. Write a function that:
    o accepts an object
    o behaves differently depending on the object’s type
    o uses isinstance
2. Add a new class that should be supported.
3. Identify all places that must be modified.
4. Redesign the solution using polymorphism so:
    o new classes require no changes to existing functions
"""
# class Fruit():
#     def fav(self):
#         return 'Orange'
# class Vegetable():
#     def fav(self):
#         return 'Carrot'
# #Adding new class
# class Juice():
#     def fav(self):
#         return 'Lemonade'
    
# def foodPrefer(f):
#     if isinstance(f, Fruit):
#         return f.fav()
#     elif isinstance(f, Vegetable):
#         return f.fav()
#     elif isinstance(f, Juice): # Add new elif instance
#         return f.fav()
    
# print(foodPrefer(Fruit()))
# print(foodPrefer(Vegetable()))
# print('After adding new class \'Juice\' new elif has to be added to function')
# print(foodPrefer(Juice()))

print('After redesigning using polymorphism')

class Food:
    def fav(self):
        NotImplemented

class Fruit():
    def fav(self):
        return 'Orange'
class Vegetable():
    def fav(self):
        return 'Carrot'
#Adding new class
class Juice():
    def fav(self):
        return 'Lemonade'
    
def foodPrefer(obj):
    return obj.fav()

print(foodPrefer(Fruit()))
print(foodPrefer(Vegetable()))
print(foodPrefer(Juice()))





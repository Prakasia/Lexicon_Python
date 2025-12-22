"""          COMBINED OOP + SCOPE + PYTHONIC TECHNIQUES
            ********************************************
"""

"""
17. Demonstrate LEGB with nested functions. Create a function that contains
another function. Use variables with the same name at multiple levels and
demonstrate which is used where. Modify the enclosing variable using nonlocal.
"""






# -----------------------------------------------------------------------------

"""
18. Create a class that processes input using a comprehension. Write a class that
receives a list or dictionary and transforms or filters the data internally using a
comprehension.
"""
# print('List Transformation')
# class listtransform:
#     def __init__(self,data):
#         self.data = data

#     def transform(self):
#         return [i * 2 for i in self.data]

# origingal_data = [10,30,50,60]
# t_data = listtransform(origingal_data)
# transformed_data = t_data.transform()
# print(f'Original data = {origingal_data}')
# print(f'Data after transformation = {transformed_data}')
    
# -----------------------------------------------------------------------------

"""
19. Create a class that builds itself from a dictionary. Write a class that receives a
dictionary and turns every key/value pair into attributes. Build __str__ using a
comprehension.
"""
# class AttributeObject:
#     def __init__(self,data:dict):
#         for key, value in data.items():
#             setattr(self, key, value)

#     def __str__(self):
#         return ', '.join(f'{key} : {value}' for key, value in self.__dict__.items())
        

# obj_data = {
#     'Name' : 'Alice',
#     'Age' : 28,
#     'City' : 'Stockholm'
# }     
# obj = AttributeObject(obj_data)
# print(obj)
# print(obj.Name)
# print(obj.Age)
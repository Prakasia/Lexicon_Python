"""
Docstring for challenge2
Challenge 2 - CLASS WITH BOTH CLASS-LEVEL AND INSTANCE-LEVEL BEHAVIOUR
**************************************************************************
Write a class that uses:
- at least one class attribute
- at least one instance attribute
- at least one method that uses the class attribute
- at least one method that uses only the instance attributes
Then add a way to change the class attribute and show how this affects all existing objects. 
Also show how changing an instance attribute affects only one object.
"""

class Person():
    # class attribute
    City = 'Stockholm'
    def __init__(self, name, age):
        # instance attributes
        self.name = name
        self.age = age
    # Method that uses the class attribute
    def get_city_info(self):
        print('City is {}'.format(self.City))
    # Method that uses only the instance attributes
    def get_info(self):
        print('Name : {}\tAge : {}'.format(self.name,self.age))

person1 = Person('Alice', 30)
person2 = Person('Bob', 40)

print('Initial values before changing')
person1.get_city_info()
person2.get_city_info()
person1.get_info()
person2.get_info()
print('')
# changing the class attribute of person1 object
Person.City = 'Uppsala'
print('After changing the class attribute')
person1.get_city_info()
person2.get_city_info()
person1.get_info()
person2.get_info()
print('')

#changing the instance attribute
person2.age = 20
print('After changing the instance attribute')
person1.get_city_info()
person2.get_city_info()
person1.get_info()
person2.get_info()

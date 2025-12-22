""" 
                    INHERITANCE

Allows us to create a class that inherits all the methods and properties from another class

Base class      : class being inherited from
Derived class   : class that inherits from another class




"""

# class A:
#     def __init__(self, value):
#         print(f'In A.__init__ and value = {value}')
#         self.value = value

# class B(A):
#     def __init__(self, value):
#         print(f'In B.__init__ and value ={value}')
#         super().__init__(value)
#         self.value += 10

# class C(A):
#     def __init__(self, value):
#         print(f'In C.__init__ and value ={value}')
#         super().__init__(value)
#         self.value *= 4

# class D(C, B):
#     def __init__(self, value):
#         print(f'In D.__init__ and value ={value}')
#         super().__init__(value)

# d = D(10)
# print(d.value)

# # Base class
# class Animal():
#     def __init__(self):
#         print('Animal created!')

#     def WhoAmI(self):
#         print('Animal')

#     def eat(self):
#         print('Eating nom nom..')

# # Derived class
# class Dog(Animal):
#     def __init__(self):
#         print('Dog created')
    
#     def WhoAmI(self):
#         print('Dog')

#     def Bark(self):
#         print('Woof Woof')

# d = Dog()
# d.WhoAmI()
# d.Bark()
# d.eat()                 # It inherits from the base class

class Employee:
    increase = 1.04
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def __str__(self):
        return f'{self.first_name} {self.last_name} earns {self.salary}'
    
    def increase_salary(self):
        self.salary = int(self.salary * self.increase)
    
# 
class Developer(Employee):
    increase = 1.10
    def __init__(self, first_name, last_name, salary, prog_lang):
        super().__init__(first_name, last_name, salary)
        self.prog_lang = prog_lang

    def __str__(self):
        return f'{super().__str__()} and fav lang is {self.prog_lang}'
    

emp1 = Employee('Anna', 'Bob', 45000)
emp2 = Employee('Bob', 'Bson', 42000)
dev1 = Developer('Karl', 'Kson', 50000, 'Python')
print('Before Increase: ')
print(emp1)
print(emp2)
print(dev1)

emp1.increase_salary()
emp2.increase_salary()
dev1.increase_salary()
print('After Increase: ')
print(emp1)
print(emp2)
print(dev1)
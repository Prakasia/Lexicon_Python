"""
10  DESIGN TASK - CONTROLLED INHERITANCE
    * Design a small inheritance hierarchy that models a real-world concept.
    * Requirements:
     - Use inheritance and super() correctly
     - Override at least one method
     - Include at least one class variable
     - Include either a protected or private attribute
     - Do not use polymorphism or duck typing
    * Create objects and demonstrate that the inheritance structure works as intended
"""
# protected attribute - _variable(single underscore)
# private attribute - __variable(double underscore)

class Employee:
    company_name = 'Modern'               # class variable
    def __init__(self, name, salary):
        self._name = name                 # protected attribute
        self.__salary = salary            # private attribute

    def printinfo(self):
        return (f'{"Name":<10} : {self._name}\n{"Salary":<10} : {self.__salary}\n{"Company":<10} : {self.company_name}')

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def printinfo(self):
        return f'{super().printinfo()} \n{"Depratment":<10} : {self.department}'
    
emp = Employee('Alice',25000)
print(emp.printinfo())
m = Manager('Anna', 30000, 'developer')
print(f'-------------------------------')
print(m.printinfo())   
print(f'-------------------------------')

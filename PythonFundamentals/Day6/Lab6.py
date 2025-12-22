"""
6           CLASS VARIABLES ACCROSS INHERITANCE
            ***********************************

    * Create a base class with a class variable.
    * Create two subclasses.
    * Override the class variable in one subclass but not the other.
    * Create objects from all classes and show how the value di􀆯ers depending on which
      class is used.

"""

class BaseClass:
    classvariable = 100
    def __init__(self):
        pass

class SubClass1(BaseClass):
    classvariable = 200
    def __init__(self):
        super().__init__()

class SubClass2(BaseClass):
    def __init__(self):
        super().__init__()

base_obj = BaseClass()
sub1_obj = SubClass1()
sub2_obj = SubClass2()

print(f'In Base Class class variable = {base_obj.classvariable}')
print(f'In Subclass1 class variable = {sub1_obj.classvariable}')
print(f'In Subclass2 class variable = {sub2_obj.classvariable}')
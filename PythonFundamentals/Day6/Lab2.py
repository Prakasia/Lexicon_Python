"""
2.                 MODIFYING STATE THROUGH SUPER()
                **************************************
    * Create a base class that stores a numeric value.
    * Create two subclasses that modify this value in di􀆯erent ways inside their
        constructors.
    * Use super() so that each class in the inheritance chain contributes to the final value.
    * Print the final result.
"""

class BaseClass:
    def __init__(self):
        self.value = 10
        print(f'\033[1;34;40m This is the Base Class with value {self.value} \033[0m')

class Subclass1(BaseClass):
    def __init__(self):
        super().__init__()
        self.value *= 10
        print(f'\033[1;32;40m This is Subclass 1 with value {self.value} \033[0m')

class Subclass2(Subclass1):
    def __init__(self):
        super().__init__()
        self.value += 10
        print(f'\033[1;33;40m This is Subclass2 with value {self.value} \033[0m')

obj = Subclass2()
print(f'Final value = {obj.value}')
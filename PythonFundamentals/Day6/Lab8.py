"""
8.
    * Create a base class with a private attribute using double underscores.
    * Attempt to access the attribute directly and observe what happens.
    * Then access it using name mangling and explain how Python handles private
    attributes internally.
"""

class Base:
    def __init__(self):
        self.__private_attribute = 10

obj = Base()
## attempting to access directly shows error
# print(f'{obj.__private_attribute}')

# Using name Mangling
print(f'Access using name mangling {obj._Base__private_attribute}')
print(f'\033[1;32;40mName mangling is used to prevent accidential access or overrides in subclasses.\
Python internally changes __private_attr to _Base__private_attr. \033[0m')
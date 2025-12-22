"""
7.                  PROTECTED ATTRIBUTES
                    ********************
    * Create a base class that uses a protected attribute (single underscore).
    * Access and modify this attribute from a subclass.
    * Demonstrate that the attribute can be accessed, and explain why this is allowed but
      discouraged outside the class hierarchy.

"""

class BaseClass:
    def __init__(self):
        self._protected_value = 20

class SubClass(BaseClass):
    def __init__(self):
        super().__init__()

    def modify_protectedValue(self,value):
        self._protected_value = value

subObj = SubClass()
print(f'Before modification Protected value = {subObj._protected_value}')
subObj.modify_protectedValue(100)
print(f'After modification Protected value = {subObj._protected_value}')
"""
5.      OVERRIDING A METHOD AND CALLING A PARENT
        ****************************************
    * Create a base class with a method that prints a message.
    * Override this method in a subclass.
    * Inside the overridden method, call the parent version using super() and then add
        additional behavior.
    * Call the method and show both outputs.
"""

class BaseClass:
    def __init__(self):
        pass
    def __str__(self):
        return f'Hello !! Welcome '

class Subclass(BaseClass):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f'{super().__str__()}to the world of Python'


base_obj = BaseClass()
sub_obj = Subclass()
print(base_obj)
print(sub_obj)
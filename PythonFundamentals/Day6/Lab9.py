"""
9.          Overriding __str__ in a Subclass
            *******************************
    * Create a base class with a meaningful __str__ method.
    * Override __str__ in a subclass.
    * Use super().__str__() inside the subclass and add subclass-specific information.
    * Print objects of both classes to show the di􀆯erence.
"""

class BaseClass:
    def __init__(self):
        pass
    def messagemethod(self):
        return f'Hello !!'

class Subclass(BaseClass):
    def __init__(self):
        super().__init__()

    def messagemethod(self):
        return f'{super().messagemethod()} Hello Again from subclass'


base_obj = BaseClass()
sub_obj = Subclass()
print(base_obj.messagemethod())
print(sub_obj.messagemethod())
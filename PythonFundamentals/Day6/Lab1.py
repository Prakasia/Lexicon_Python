"""
            CONSTRUCTOR EXECUTION ORDER
            ***************************
* Create a base class and two subclasses that form an inheritance chain.
* Each class must print a message from its constructor.
* Create an object of the most derived class and observe the order in which the
    constructors are executed.
* Use super() in all constructors.
"""

class BaseClass:
    def __init__(self):
        print('\033[1;34;40m This is the base  \033[0m')

class Subclass1(BaseClass):
    def __init__(self):
        super().__init__()
        print('\033[1;32;40m This is Subclass 1 \033[0m')

class Subclass2(Subclass1):
    def __init__(self):
        super().__init__()
        print('\033[1;33;40m This is Subclass2 \033[0m')

obj = Subclass2()
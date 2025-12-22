"""
6.  ABSTRACT BASE CLASS ENFORCEMENT
Objective: Understand why ABCs exist.
***************************************
1. Design an abstract base class that:
    o represents a role or capability
    o defines at least one abstract method
2. Attempt to:
    o create a subclass that does not implement the method
    o instantiate it
3. Observe and explain the error.
4. Create:
    o one valid subclass
    o a second valid subclass with different behavior
5. Write a function that:
    o accepts the abstract base class
    o calls the abstract method
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# try:
#     s = Square()
# except TypeError as e:
#     print("Shows the below error message : ")
#     print(f'\033[1;34;40m {e} \033[0m')
#     print('\033[1;32;40m This is because Square inherits from Shape but did not implement area method \033[0m')


def find_area(obj):
    return obj.area()

s = Square(4)
c = Circle(10)

print(f'Area of square of side 4 is {find_area(s)}')
print(f'Area of circle of radius 10 is {find_area(c)}')



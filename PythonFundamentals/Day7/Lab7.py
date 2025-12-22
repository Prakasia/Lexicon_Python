# #Duck typing
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height
    
# # violation no 'area' method   
# class BrokenShape:
#     pass  

# def print_area_duck(shape):
#     print(f"Area: {shape.area()}")
    
# rect = Rectangle(3, 4)
# print_area_duck(rect)
# broken_shape = BrokenShape()
# try:
#     print_area_duck(broken_shape)
# except AttributeError as e:
#     print("Duck typing error:", e)
#     print('Error timing: Runtime, when shape.area() is called.\
#           Error message: AttributeError: \'BrokenShape\' object has no attribute \'area\'\
#           Developer experience: Error occurs only when executing the code')
    
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
    
def print_area_abc(shape):
    print(f"Area: {shape.area()}")

square = Square(5)
print_area_abc(square)  

# violation there is no 'area' method 
class BrokenShape2(Shape):
    pass  

try:
    broken_shape2 = BrokenShape2()
except TypeError as e:
    print("Abstract class error:", e)

print(f'Error timing: Instantiation time.\
      Error message: TypeError: Can\'t instantiate abstract class BrokenShape2 with abstract methods area\
      Developer experience: clear message about missing implementation.')
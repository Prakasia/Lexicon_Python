"""
            DUNDER METHODS
            **************
6. Implement __eq__. Create a class where two objects are equal if their attributes
match.
"""

class Rectangle1:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __eq__(self,other):
        return self.length == other.length and self.width == other.width
    
r1 = Rectangle1(5, 10)
r2 = Rectangle1(5, 10)
print(r1 == r2)
print('-----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------

"""
7. Implement __lt__. Create a class where objects can be compared using < based
on one chosen attribute.
"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __lt__(self, other):
        return (self.length*self.width) < (other.length * other.width)

r1 = Rectangle(5, 10)
r2 = Rectangle(10, 2)
print(r1 < r2)
print('-----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------


"""
8. Implement __add__. Create a class where adding two objects with + produces a
new combined object.
"""

class Something:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __add__(self,other):
        return f'Something (name = {self.name} & {other.name} , age = {self.age} + {other.age})'
    
    def __repr__(self):
        return f'Something(name = {self.name}, age = {self.age})'

s1 = Something('Alice', 30)
print(s1)
s2 = Something('Anna', 60)
print(s2)
s3 = s1 + s2
print(s3)
print('-----------------------------------------------------------------------------')

# -----------------------------------------------------------------------------

"""
9. Implement __len__. Create a class where len(object) returns a meaningful
numeric value based on internal data.
"""
class Cart1:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return f"Cart(items={self.items})"
    
c = Cart1()
c.add_item("Apple")
c.add_item("Orange")
c.add_item("Grapes")

print(c)
print(len(c))
print('-----------------------------------------------------------------------------')


# -----------------------------------------------------------------------------

"""
10. Implement __contains__. Create a class where you can check "value in object"
using __contains__.
"""
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __contains__(self, item):
        return item in self.items

    def __repr__(self):
        return f"Cart(items={self.items})"
    
cart = Cart()
cart.add_item("Apple")
cart.add_item("Orange")

print(cart)            
print("Apple" in cart) 
print("Banana" in cart)
print('-----------------------------------------------------------------------------')



# -----------------------------------------------------------------------------

"""
11. Implement __getitem__. Create a class that allows indexing with square brackets
to access internal data.
"""

class Cart2:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __getitem__(self, index):
        return self.items[index]

    def __repr__(self):
        return f"Cart(items={self.items})"

cart = Cart2()
cart.add_item("Apple")
cart.add_item("Orange")
cart.add_item("Banana")

print(cart)        
print(cart[0])     
print(cart[2])    
print('-----------------------------------------------------------------------------')
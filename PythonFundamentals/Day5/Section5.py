"""
20. Combine kwargs, property, and a dunder method. 

Create a class that: - accepts
all attributes via **kwargs - includes at least one property with getter and setter -
implements one or more dunder methods - includes a method that performs a
calculation using its data
"""
class Product:
    def __init__(self,data:dict):
        for key, value in data.items():
            setattr(self, key, value)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        self._price = value

    def __str__(self):
        return ", ".join(
            f"{key}={value}"
            for key, value in self.__dict__.items())
    
    def discounted_price(self):
        return self._price * (1 - self.discount/100)
        
c1 = {
    'Name' : 'Apple',
    'Qty' : 2,
    'price' : 30,
    'discount' : 10
    }

cart1 = Product(c1)
print(cart1)
print(f'Before changing, Value of price = {cart1.price}')
print(f'Calculating the discounted price {cart1.discounted_price()}')
cart1.price = 45
print(f'After changing, Value of price = {cart1.price}')
print(f'Calculating the discounted price {cart1.discounted_price()}')
print(cart1)
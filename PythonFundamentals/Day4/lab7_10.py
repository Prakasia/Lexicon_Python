"""
7. CREATING YOUR OWN CLASS
***************************
Write a class with at least two instance attributes and a method 
that prints or returns information based on those attributes. 
Create at least two objects and demonstrate that they can have different values.
"""

class Country1():
    def __init__(self, name, capital):
        self.name = name
        self.capital = capital

    def info(self):
        print('Country : {}\t Capital : {}'.format(self.name,self.capital))

country1 = Country1('Sweden', 'Stockholm')
country2 = Country1('Norway', 'Oslo')
country1.info()
country2.info()

# -----------------------------------------------------------------------------

"""
8. CLASS ATTRIBUTE VS INSTANCE ATTRIBUTES
*****************************************
Create a program demonstrating a class attribute shared across multiple objects. 
Then change the attribute for only one object and show that the other objects still use 
the original class attribute.
"""

class Country():
    language = 'Unknown'
    def __init__(self, name, capital):
        self.name = name
        self.capital = capital

    def info(self):
        print('Country : {}\t Capital : {}'.format(self.name,self.capital))

country1 = Country('Sweden', 'Stockholm')
country2 = Country('Norway', 'Oslo')
print('Before changing the class attribute')
print('Language attribute in country1 = {}'.format(country1.language))
print('Language attribute in country2 = {}'.format(country2.language))

country1.language = 'Svenska'

print('After changing the class attribute')
print('Language attribute in country1 = {}'.format(country1.language))
print('Language attribute in country2 = {}'.format(country2.language))

# -----------------------------------------------------------------------------

"""
9. CLASS WITH CALCULATION METHOD
*********************************
Write a class with one attribute and a method that calculates something based on that attribute 
(for example area, price, or length). Show how changing the attribute affects the calculation.
"""

class Square():
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return (self.side * self.side)
    
sq1 = Square(5)
print(f'Side = {sq1.side}\tArea = {sq1.calculate_area()}')
sq1 = Square(10)
print(f'Side = {sq1.side}\tArea = {sq1.calculate_area()}')

# -----------------------------------------------------------------------------

"""
10. METHOD FOR UPDATING AN ATTRIBUTE
*************************************
Write a class where an attribute can be updated through a custom method. Demonstrate how the
updated attribute changes the behavior of another method in the class.
"""

class product():
    def __init__(self, price):
        self.price = price
        self.discount = 0
    
    def update_discount(self, discount):
        self.discount = discount

    def calculte_finalprice(self):
        final_price = self.price * (1 - self.discount/100)
        return final_price

product1 = product(3500)
print('Discount = {}\tProduct Price = {}'.format(product1.discount,product1.calculte_finalprice()))
product1.update_discount(20)
print('Discount = {}\tProduct Price = {}'.format(product1.discount,product1.calculte_finalprice()))
product1.update_discount(35)
print('Discount = {}\tProduct Price = {}'.format(product1.discount,product1.calculte_finalprice()))

# -----------------------------------------------------------------------------
"""
5. STATIC UTILITY METHODS
**************************
    * Create a class that acts as a utility container.
    * The class should contain multiple static methods.
    * Each static method should perform a small, independent operation.
    * Demonstrate usage without creating any class instances.
"""

class UtilityContainer:

    @staticmethod 
    def ispalindrome(txt):
        return (txt == txt[::-1])
    
    @staticmethod 
    def reverse(txt):
        return txt[::-1]
    
    @staticmethod 
    def toupper(txt):
        return txt.upper()
    
    @staticmethod 
    def tolower(txt):
        return txt.lower()
    
print(UtilityContainer.ispalindrome('racecar'))
print(UtilityContainer.tolower('Python'))
print(UtilityContainer.reverse('Hello World'))
print(UtilityContainer.toupper('hello'))
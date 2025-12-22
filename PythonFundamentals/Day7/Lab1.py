"""
1. DISCOVER DUCK TYPING
Objective : Understand that shared behavior, not shared type, enables polymorphism.
*****************************************************************************************
Instructions : 
1. Write a function that:
    o accepts a single argument
    o calls one method on that argument
2. Call the function with:
    o a built-in type
    o a custom class you create yourself
3. The function must work without modification for both.
Constraints
    • Do NOT use isinstance
    • Do NOT check types explicitly

"""

def find_count(txt, wd):
    return txt.count(wd)

class duckTyping:
    def __init__(self, text):
        self.text = text

    def count(self, wd):
        return self.text.count(wd)

x = "Welcome to Python. Python is powerful and fast. Python is friendly & easy to learn. Python is open"
print(find_count(x,"Python"))
print(find_count(duckTyping(x), "Python"))

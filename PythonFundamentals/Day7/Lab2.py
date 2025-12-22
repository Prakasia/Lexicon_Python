"""
2. BREAK DUCK TYPING ON PURPOSE
Objective: Understand the risk of duck typing.
**************************************************
Instructions
    1. Take your function from Lab 1.
    2. Pass an object that does not implement the expected behavior.
    3. Observe the error.
    4. Explain: when the error occurs
"""

def find_count(txt, wd):
    return txt.count(wd)

class duckTyping:
    def __init__(self, text):
        self.text = text

    def count(self, wd):
        return self.text.count(wd)
    
x = 'Hello World 2'
print(find_count(x,2))
print(find_count(duckTyping(x), 2))

"""
The Error occur because we pass an integer which was supposed to be a string 
"""
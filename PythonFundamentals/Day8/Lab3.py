"""
3. CLOSURE BASED CONFIGURATION
   ***************************
    * Create a function that returns another function.
    * The returned function should behave differently depending on a value captured from the
        outer function.
    * Create at least two functions from the same factory function and demonstrate the difference
        in behavior.
"""

def prefix_creator(prefix):
    def add_prefix(text):
        return f'{prefix} - {text}'
    return add_prefix

func1 = prefix_creator("Hello")
func2 = prefix_creator("Good Morning")

print(func1("Welcome to python programming!"))
print(func2("Have a nice day!"))



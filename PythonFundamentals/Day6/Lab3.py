"""
3.              MULTIPLE INHERITANCE AND MRO
                ****************************
    * Create two parent classes that both modify the same attribute in their constructors.
    * Create a child class that inherits from both parents.
    * Use super() in all constructors.
    * Print the final value and print the MRO of the child class.
    * Explain why the final value is produced.

"""

class Parent1:
    def __init__(self):
        super().__init__()
        self.value += 4
        print(f'Parent1 : value = {self.value}')

class Parent2:
    def __init__(self):
        super().__init__()
        self.value *= 5
        print(f'Parent2 : value = {self.value}')

class Child(Parent1, Parent2):
    def __init__(self):
        self.value = 0
        print(f'Child start, value: {self.value}')
        super().__init__()
        print(f'Child end, value = {self.value}')

c = Child()
print(f'Final value = {c.value}')
print(Child.mro())
# print(f'\033[1;32;40m Child constructor set the value = 0 \
#       then it follows MRO Child -> Parent1 -> Parent2 - object \
#       So first the value = 0, then   \033[0m')
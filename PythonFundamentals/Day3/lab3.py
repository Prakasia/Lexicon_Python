"""
Docstring for Day3.lab3
    FUNCTIONS AND CONDITIONALS
    Goal: Practice function creation, return values, and conditional logic.
    ***************************
Create functions that:
1. Return a greeting with a name
2. Return a default greeting if no name is given
3. Check if a number is even
4. Add two numbers only if both are even, otherwise return 0
"""

def greeting(name):
    return ('Hello ' + name)
def greeting2(name = 'default'):
    return ('Hello ' + name)

def even_func(num):
    return(num%2==0)

def addOnlyifEven(num1, num2):
    if(even_func(num1) and even_func(num2)):
        return (num1+num2)
    
#Greeting with name 
st = greeting('Shalu')
print(st)

#Greeting with default
st = greeting2()
print(st)

#Check even
even = even_func(30)
print(even)

#Add only if both are even
s = addOnlyifEven(3,2)
s = addOnlyifEven(8,2)
if(s):
    print(f'Sum is {s}')
else:
    print('Odd')
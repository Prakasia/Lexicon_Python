"""
6. Loop - Power Calculation
****************************
Write a program that takes two integers as input (base and exponent) and calculates the
power using loops.
"""

base = int(input(' Enter base : '))
exponent = int(input(' Enter the exponent : '))
power = 1
for i in range (exponent):
    power *= base

print(f' {base} to the power of {exponent} is {power}')
#---------------------------------------------------------------------------------------------


"""
7. Tuple - Sum of Elements
*****************************
Write a program that calculates the sum of all elements in a given tuple.
"""

my_tuple = (2,4,6,8,10)
sum = 0
for element in my_tuple:
    sum += element
print(f' Sum of all elements in the given tuple is {sum}')
#---------------------------------------------------------------------------------------------


"""
8. Tuple with Condition
**************************
Create a new tuple that contains only the even numbers from a given tuple of integers.
"""

given_tuple = (12,34,11,45,4,6,7,9,10)
even_list = [x for x in given_tuple if x%2 == 0]
even_tuple = tuple(even_list)
print(f' Original tuple is {given_tuple}')
print(f' Tuple with only even numbers : {even_tuple}')
#---------------------------------------------------------------------------------------------
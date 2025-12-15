""" 
PYTHON CALCULATOR (NUMBERS AND ARITHMETIC)
Goal: Practice numeric operations & print formatting.
******************************************
Create a program that:
1. Takes two numbers from the user
2. Calculates and prints:
o Sum
o Difference
o Product
o Division
o Power
3. Print the results in a nicely formatted way.
"""

num1,num2 = input('Enter two numbers ').split()
num1 = int(num1)
num2 = int(num2)
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2
power = num1 ** num2

print(f' Sum = {sum}\n Difference = {difference}\n Product = {product}\n Division = {division}\n Power = {power}')
"""
Docstring for Day3.lab2
    LIST AND COMPREHENSIONS
    Goal: Practice list operations, loops, and list comprehensions.
    ***********************
Create a program that:
1. Takes a given list of numbers
2. Generates and prints:
    * A list of squares using a loop
    * A list of squares using a list comprehension
    * A list of positive numbers using a comprehension

"""

user_list = input('Enter the list of numbers separated by space : ')
user_list = user_list.strip().split()
user_list = [int(x) for x in user_list]
square_list_loop =[]

print(f'User list = {user_list}')
#list of squares using loop
for x in user_list:
    square_list_loop.append(x*x)
print(f'Square list using loop = {square_list_loop}')

#List comprehension
square_list2 = [(x*x) for x in user_list]
print(f'Square list using list comprehension = {square_list2}')

# Positive numbers from user list
pos_numbers = [x for x in user_list if x > 0]
print('List of positive numbers = {}'.format(pos_numbers))
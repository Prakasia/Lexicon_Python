"""
    EVEN NUMBER FILTER TOOL - MINI PROJECT
    Goal: Practice input handling, list processing, and the filter() function.
    ***************************************
Create a program that:
1. Accepts a line of numbers from the user
2. Converts the input into a list of integers
3. Uses filter() + lambda to keep only even numbers
4. Prints:
    * The list of even numbers
    * The count of even numbers
"""

user_input = input('Enter the numbers separated by space : ')
user_input = user_input.strip().split()
user_input = [int(x) for x in user_input]   #LIST OF INTEGERS

evens = filter(lambda num : num%2 == 0, user_input)
evens_list = list(evens)

count = len(evens_list)

print('The list of even numbers : {}'.format(evens_list))
print('Number of even number = {} '.format(count))

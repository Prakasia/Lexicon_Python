"""
LIST COMPREHENSION TRANSFORMATIONS
Goal: Become comfortable with comprehensions
****************************************
Given:
numbers = [1,2,3,4,5,6,7,8,9]
Students must create using list comprehensions:
1. A list of squares
2. A list of only even numbers
3. A list of numbers doubled
4. A list of only numbers greater than 5
5. A list of strings: "Number: X" for each element

"""

numbers = [1,2,3,4,5,6,7,8,9]

square_list = [i*i for i in numbers]
print(' List of squares : {}'.format(square_list))

even_list = [i for i in numbers if i%2 == 0]
print(' List of even numbers : {}'.format(even_list))

double_list = [(i*2) for i in numbers]
print(' List of numbers doubled : {}'.format(double_list))

num_greaterthan5 = [i for i in numbers if(i>5)]
print(' List of numbers greater than 5 : {}'.format(num_greaterthan5))

num_strings = ['Number : {}'.format(i) for i in numbers]
print(' Number string list : {}'.format(num_strings))
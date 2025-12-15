"""
USERNAME GENERATOR 
Goal: Combine indexing, slicing, formatting, variables.
******************* 
Ask the user for:
• First name
• Last name
• Birth year
Then generate a username using slicing, for example:
first 2 letters of first name + last 3 letters of last name + last 2 digits of birth year

"""

first_name = input(' Enter your first name: ')
last_name = input(' Enter your last name: ')
birth_year = input(' Enter your bith year: ')
user_name = (first_name[:2] + last_name[:2] + birth_year[-2:]).upper()
print(' Your username is {}'.format(user_name))
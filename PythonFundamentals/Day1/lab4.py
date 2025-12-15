"""
STRING METHOD INVESTIGATION
Goal: Practice built-in string methods & transformations.
***************************
Using a string from user input, students must show: 
1. Uppercase version 
2. Lowercase version 
3. How many characters the string has 
4. Split the string into words 
5. Replace one letter with another
"""

user_string = input('Enter a string: ')
print(' Uppercase Version : {}'.format(user_string.upper()))
print(' Lowercase Version : {}'.format(user_string.lower()))
print(' Number of character in string : {}'.format(len(user_string)))
print(' Words in the string {}'.format(user_string.split()))
print(' Replacing all occurance of \'a\' with \'z\' : {}'.format(user_string.replace('a','z')))


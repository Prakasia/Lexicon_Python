"""
9. Dictionaries - Merge
*************************
Write a program that merges two dictionaries into one. If a key exists in both, the value from
the second dictionary should be used.
"""

my_dict1 = {
    1 : 'a',
    2 : 'b',
    3 : 'c',
    4 : 'd'
    }

my_dict2 = {
    3 : 'S',
    5 : 'Y',
    4 : 'Z',
    7 : 'M' 
}

my_merged_dict = my_dict1.copy()
for key, value in my_dict2.items():
    my_merged_dict[key] = value

print(f' Dict1 = {my_dict1}')
print(f' Dict2 = {my_dict2}')
print(f' Merged dict = {my_merged_dict}')


#---------------------------------------------------------------------------------------------

"""
10. List Comprehension - Even Numbers
******************************************
Write a program that takes a list of integers and uses list comprehension to create a new list
containing only the even numbers.
"""

user_list = input(' Enter a list of integers separated by spaces: ')
user_list = user_list.strip().split()
user_list = [int(x) for x in user_list]
even_list = [x for x in user_list if x%2 == 0]
print(f' List containing only even number is {even_list}')
#---------------------------------------------------------------------------------------------


"""
11. String - Reverse
****************************
Write a program that takes a string as input and prints the reversed string.
"""

user_string = input(' Enter the string to reverse: ')
print(f' Reversed string :: {user_string[::-1]}')
#Reversing only the words
string_elements = user_string.split()
reversed_string_elements = string_elements[::-1]
separator = " "
reversed_string = separator.join(reversed_string_elements)
print(f' Words in string reversed :: {reversed_string}')

#---------------------------------------------------------------------------------------------
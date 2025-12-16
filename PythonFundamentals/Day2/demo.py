#                   DICTIONARY
# ************************************************************* #

# name = 'Shalu'
# age = 50
# print(f" My name is {name} and I'm {age} years old")

#dict (key:value)
# my_dictionary = {
#     1:'value one',
#     2:'value two',
#     3:'value three',
#     4:['name1', 'name2']
# }

# print(my_dictionary[4][0].upper())

# #update the value in key
# my_dictionary[1] = 'updated value one'
# print(my_dictionary)

# my_dictionary[4] += ['name3']
# print(my_dictionary[4])

# new_dict = {}

# new_dict['animal'] = 'cat'
# new_dict['answer'] = 42
# print(new_dict)

# nested_dictionay = {
#     'person1' : {
#         'name' : {
#             'first' : 'Alice',
#             'last' : 'Allison'
#         },
#         'age' : 30
#     },
#     'person2' : {
#         'name' : {
#             'first' : 'Bob',
#             'last' : 'Bobson' 
#         },
#         'age' : 30
#     }
# }
# print(nested_dictionay['person2']['name']['last'])

# dictionary = {
#     'key1' : 1,
#     'key2' : 2,
#     'key3' : 3,
#     'key4' : 4,
#     'key5' : 5
# }
# print(dictionary.keys())
# print(dictionary.values())
# print(dictionary.items()) #tuple with list of tuples

# ------------------------------------------------------------------------

#       TUPLE
# *****************************

# tuples are immutable : its values cannot be changed eg: days of a calendar 

# my_tuple = (1,2,3, 'four',3,5,3,6,9,3)

# we cannot append or change a value in tuple
# print(len(my_tuple))
# print(my_tuple[-1])
# print(my_tuple.index('four'))
# print(my_tuple.count(3))

# ---------------------------------------------------------------
#       SETS & BOOLEANS

#  Set doesnot allow duplicate values in it. Unique elements
# my_set = {1,2,3}
# my_set.add(4)
# print(my_set)

# my_list = [1, 2, 3, 1, 2, 3, 4, 5, 6, 6]
# print(set(my_list))

##      Boolean  capital T or capital F

# a = True
# b = False

# logical operators 'and', 'or'

# intendations : very important in python no colon and semicolon

#   LOOPS
# sequence = [1, 2, 3, 4, 5]

# for item in sequence:
#     print(item)

# ages = {
#     'John' : 4,
#     'Doe' : 5,
#     'Moe' : 6
# }

# for key in ages:
#     print('This is the key: ',end="")
#     print(key)
#     print ('This is the value: ',end="")
#     print(ages[key])
#     print('\n')

mypairs = [(1,10), (2,20), (3,30)]
# for tup in mypairs:
#     print(tup)

for item1, item2 in mypairs:
    print(item1)
    print(item2)




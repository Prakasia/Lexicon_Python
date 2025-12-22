"""
            COMPREHENSION EXCERCISES
12. Rewrite a loop using a list comprehension. Convert any loop-based list
transformation into a single list comprehension.
"""
# number_list = [1,2,3,4,5,6,7]
# square_list = []
# for i in number_list:
#     square_list.append(i*i)
# print(f'Square list using loop method : {square_list}')

# even_list_c = [i*i for i in number_list ]
# print(f'Square list using list comprehension {even_list_c}')

# -----------------------------------------------------------------------------

"""
13. Create a filtered list comprehension. Make a comprehension that filters elements
based on a condition.
"""
# number_list = [10, 22, 34, 40,6, 7, 9]
# even_list = []
# for i in number_list:
#     if(i%2 == 0):
#         even_list.append(i)
# print(f'Even list using loop method : {even_list}')

# even_list_c = [i for i in number_list if i % 2 == 0]
# print(f'Even list using list comprehension {even_list_c}')

# -----------------------------------------------------------------------------


"""
14. Create a dictionary using a dict comprehension. Use two lists and combine them
into a dictionary via comprehension.
"""

# list1 = ['a', 'b', 'c', 'd']
# list2 = [1, 3, 4, 5, 6, 7, 8, 9]

# d = {k:v for k, v in zip(list1,list2)}
# print(d)


# -----------------------------------------------------------------------------

"""
15. Build a formatted string using a comprehension. Generate a formatted string
from object or dictionary data using comprehension and join().
"""
# class Marks:
#     def __init__(self,data:dict):
#         self.__dict__ = data

#     def __str__(self):
#         return 'Students passed \n' +                                                  \
#                 '\n'.join(f'{key} : {value}' for key, value in self.__dict__.items()    \
#                 if value >= 40)
    
# st_marks = {
#     "Alice": 70,
#     "Bob": 40,
#     "Charlie": 35,
#     "Tom" : 50,
#     "Anna" : 30
# }

# print(f'Student Mark list = {st_marks}')
# m = Marks(st_marks)
# print(m)

# -----------------------------------------------------------------------------


"""
16. Create a nested comprehension. Generate a two-dimensional structure (like a
table or grid) with nested comprehensions.
"""

# table_data = [[j * i * 2 for j in range(1,7) ]for i in range(1,5)]
# table_str = "\n".join(" ".join(f'{num:4}' for num in row) for row in table_data)
# print(table_str)
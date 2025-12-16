"""
1. String Indexing
***************
Given the string s = 'Python', use indexing to print the following:
- 'o'
- 'Pyth'
- 'yth'
- 'nohtyP'
"""

s = 'Python'
print(s[4])
print(s[:4])
print(s[1:4])
print(s[::-1])
# ----------------------------------------


"""
2. Nested List
  *************
Given the list l = [3, 7, [1, 4, 'hello']], change the value 'hello' to 'goodbye'.
"""

l = [3, 7, [1,4, 'hello']]
l[2][2] = 'goodbye'
print(l)
# ----------------------------------------


"""
3. Dictionaries - Access Values
********************************
Using keys and indexing, retrieve the value 'hello' from the following dictionaries:
d1 = {'simple_key':'hello'}
d2 = {'k1':{'k2':'hello'}}
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]} - this is tricky :)
"""

d1 = {'simple_key':'hello'}
d2 = {'k1':{'k2':'hello'}}
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print('\'hello\' in d1 : {}'.format(d1['simple_key']))
print('\'hello\' in d2 : {}'.format(d2['k1']['k2']))
print('\'hello\' in d3 : {}'.format(d3['k1'][0]['nest_key'][1][0]))
# -----------------------------------------------------------------------------------------


"""
4. Sets - Unique Values
***************************
Use a set to find the unique values in the list:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
"""

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print(' Unique values in the list {}'.format(set(mylist)))
# -----------------------------------------------------------------------------------------


"""
5. Print Formatting
***********************
You are given the variables:
age = 4
name = 'Sammy'
Use print formatting to display:
"Hello my dog's name is Sammy and he is 4 years old"
"""

age = 4
name = 'Sammy'
print(f' Hello my dog\'s name is {name} and he is {age} years old.')
# -----------------------------------------------------------------------------------------
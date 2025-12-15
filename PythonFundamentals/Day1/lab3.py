"""
STRING INDEXING & SLICING EXPLORER
Goal: Practice indexing, slicing, stepping
**********************************
Given the string:
s = "ProgrammingIsFun"
Students must extract:
1. The first letter
2. The last 3 letters
3. Every second letter
4. The word "Programming"
5. The word "Fun" without using indices directly (must use slicing)
6. The string reversed

"""

s = "ProgrammingIsFun"
print(' First letter in \'s\' is {}'.format(s[0]))
print(' Last three letters are : {}'.format(s[-3:]))
print(' Every second letter : {}'.format(s[::2]))
print(' {}'.format(s[:11]))
print(' Without using indices directly : {}'.format(s[(len(s)-3):]))
print(' Reversed string : {}'.format(s[::-1]))
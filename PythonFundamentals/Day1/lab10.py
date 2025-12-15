"""
MINI PROJECT : STUDENT INFORMATION FORMATTER
Goal: Combine strings, formatting, indexing, list creation.
******************************************************
Ask user for:
• Name
• Age
• Favorite subject
• Favorite quote
Then:
1. Use formatting (.format() or f-strings) to print a nicely formatted paragraph.
2. Capitalize the name.
3. Remove whitespace around inputs.
4. Create a list of the letters from the name.
5. Print the first and last letter from that list.

"""
name = input(' Enter your name : ')
age = input(' Enter your age : ')
fav_subject = input(' Enter your favorite subject : ')
fav_quote = input(' Enter your favorite quote : ')
name = name.upper().strip()
age = age.strip()
fav_subject = fav_subject.strip()
fav_quote = fav_quote.strip()

print(f' Hi, My name is {name}. I am {age} years old. My favorite subject is {fav_subject}.\n My favorite quote is {fav_quote}.')

print(' Name in capitals : {}'.format(name))

name = name.split()
name_letters = [char for str in name for char in str]
print(name_letters)

print(' First letter : {} and last letter : {}'.format(name_letters[0],name_letters[-1]))
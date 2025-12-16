"""
Docstring for Day3.lab4
    FILTER AND LAMBDA FUNCTIONS
    Goal: Practice the filter() function and lambda expressions.
    ***************************
Create programs that:
1. Use filter() + a function to keep only even numbers
2. Use filter() + lambda to keep only even numbers
3. Filter names that have 3 or more characters
4. Filter words that contain the letter "a"

"""
def even_func(num):
    return (num%2==0)

numbers = [2,45,67,88,70,24,31]
evens1 = filter(even_func,numbers)
print(f'Even List using filter and function : {list(evens1)}')

evens2 = filter(lambda num : num%2 == 0, numbers )
print(f'Even List using filter and lambda : {list(evens2)}')

name_list = ['Alice', 'Mo', 'Bob', 'Anna', 'Jo', 'Su']
filter_names = filter(lambda name:len(name) >= 3, name_list)
print(f'Name list after filtering using lambda function : {list(filter_names)}')

word_list = ['hello', 'bye', 'apple', 'banana', 'broccoli', 'soup', 'grapes']
filter_words = filter(lambda words : 'a' in words, word_list)
print(f'Word list with \'a\' : {list(filter_words)}')

# range fn always starts on zero and goes upto the value , but not the value

# for i in range(2,10,2):
#     print(i)

# nums = list(range(5))
# print(nums)
# LIST COMPREHENSION
# x = [2, 4, 6]
# out = [(item**2) for item in x]
# print(out)
# --------------------------------------------------------------------------------------------

# FUNCTION
# def givemeHello():
#     return 'hello'

# print(givemeHello())

# def evenfunc(num):
#     print(f'Checking if {num} even')

#     print(num%2 == 0)

# evenfunc(42)

# def helloYou(nam='Default'):
#     return ('hello '+ nam)

# print(helloYou('Shalu'))

# def addEvenOnly(num1,num2):
#     """
#     INPUT : two numbers
#     OUTPUT : False if both numbers are odd
#              add if both number are even
#     """

#     if (num1%2 != 0) or (num2%2 !=0):
#         return False
#     else :
#         return num1+num2
    
# print(addEvenOnly(1,2))
# print(addEvenOnly(4,8))
# print(addEvenOnly(1,3))

# myList = [1,2,3,4,5,6,7,8,9,10]

# evens = filter(lambda num : num % 2 == 0, myList) # convert to list first and then print
# print(list(evens))
# args positional arguments 

# st = 'My name is Shalu Prakasia'
# st.upper()
# st.lower()
# st.split()

# d = {
#     'k1' : 1,
#     'k2' : 2
# }

# def func(a, b, **kwargs):
#     print(a, b)
#     print(kwargs)

# func(1, 2, c=12, d=17)

# args = tuple
# kwargs = dictionry
# position matters in this funcion:

def func2(a, b, *args, name = 'shalu', **kwargs ):
    print('a = {}'.format(a))
    print('b = {}'.format(b))
    print('args = {}'.format(args))
    print('name = {}'.format(name))
    print('kwargs = {}'.format(kwargs))

func2(1, 2, 3, name='anna', age=35, email='anna@gmail.com')

# *ARGS AND **KWARGS are used to allow functions to accept arbitrary 
# number of arguments. Helps when designing with varying number of inputs 
# to a function
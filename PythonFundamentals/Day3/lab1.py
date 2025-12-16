"""
    RANGE AND LOOP (Numbers and Iteration)
    Goal: Practice range(), loops, and numeric iteration
    ***************************************
Create a program that:
1. Prints all odd numbers from 1-20
2. Calculates and prints the sum of numbers from 1-100
3. Asks the user for a number and prints its multiplication table (1-10)

"""

# Odd numbers from 1 - 10
print(' Odd numbers from 1 to 20: ')
for num in range(1,21):
    if num%2 != 0:
        print(' {}'.format(num), end="")
print()

# Calculates and print the sum of numbers from 1 to 100
sum = 0
for num in range(1,101):
    sum += num
print(f' Sum of numbers from 1 to 100 is {sum}')

#Number and its multiplication table
number = int(input('Enter a number to print the multiplication table: '))
print(' MULTIPLICATION TABLE OF {}'.format(number))
for i in range(1,11):
    print(f'\t{i} * {number} = {i*number}')
"""
3. EAFP vs LBYL
Objective: Practice EAFP-style error handling.
**************************************************
Instructions
1. Write a function that:
    o performs an operation on two inputs
    o may fail depending on the inputs
2. Implement it using:
    o try
    o except
3. Test the function with:
    o valid inputs
    o invalid inputs
    o edge cases
Constraints
• Do NOT use isinstance
• Do NOT pre-check types
"""

def find_sum(num1, num2):
    try:
        return (num1 + num2)
    except Exception as e:
        return e

print(find_sum(2,3))            # Adds
print(find_sum('a', 'b'))       # Concatinates
print(find_sum('ab',6))         # Error
print(find_sum([1],[1,2,3]))    # Concatenates
print(find_sum([], 2))


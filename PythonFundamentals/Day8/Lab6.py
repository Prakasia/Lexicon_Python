"""
6. HIGHER ORDER FUNCTION PIPELINE
*********************************
    * Create a function that takes another function as input.
    * Chain multiple function calls together to process a value step by step.
    * Use both named functions and lambda expressions in the pipeline.
"""

def pipelinefunc(value, funcs):
    for func in funcs:
        value = func(value)
    return value

def doublethenum(n):
    return n*2

def add_ten(n):
    return n+10

def halve_num(n):
    return int(n/2)

def addtext(n):
    return f'{str(n)} is the new number'

num = 20
func_list = [doublethenum, add_ten, halve_num, addtext ]
result = pipelinefunc(num, func_list)
print(result)
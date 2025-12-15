"""
VARIABLES & REASSIGNMENT
Goal: Understand variable assignment and updating values.
************************
Students must:
1. Create variables for salary, bonus, and tax_rate.
2. Calculate:
    * total income
    * taxes
    * net income
3. Reassign variables to simulate a raise and recalc everything.
"""
def calculate(salary, bonus, t_rate):
    t_inc = salary + bonus
    tax = t_inc * t_rate
    net_inc = t_inc - tax
    return t_inc, tax, net_inc


salary = 25000
bonus = 1000
tax_rate = .20

total_income, taxes, net_income = calculate(salary,bonus,tax_rate)
print(f' Total Income = {total_income} taxes = {taxes} and net income = {net_income}')

salary = 35000
bonus = 1000
tax_rate = .2
total_income, taxes, net_income = calculate(salary,bonus,tax_rate)
print(' After a salary of 10000\n Total Income = {} taxes = {} and net income = {}'.format(total_income,taxes,net_income))


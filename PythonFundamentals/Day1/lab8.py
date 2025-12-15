""" 
MATRIX NAVIGATION
Goal: Practice nesting + comprehensions
******************
Create three lists and nest them to form a matrix. Example:
[ [1,2,3],
[4,5,6],
[7,8,9] ]
Students must:
1. Print the number in row 1, column 2
2. Print the entire second row
3. Print the diagonal (1,5,9)
4. Create a new list of all first-column elements using indexing
5. Then repeat using a list comprehension

"""

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
matrix = [list1, list2, list3]
print(matrix)
print(' Number in row1 column2 {}'.format(matrix[0][1]))
print(' Second row : {}'.format(matrix[1]))
print(' Diagonal Elements : {},{},{}'.format(matrix[0][0], matrix[1][1], matrix[2][2]))
first_col1 = []
for row in matrix:
    first_col1.append(row[0])
print(' First column elements using indexing: {}'.format(first_col1))
first_col2 = [row[0] for row in matrix]
print(' First column elements using list comprehension: {}'.format(first_col2))


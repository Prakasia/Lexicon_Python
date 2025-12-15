"""
LIST BUILDER
Goal: Practice list manipulation.
**************
Students must:
1. Create a list with 5 mixed-type elements
2. Use append() to add two new items
3. Use pop() to remove an element
4. Reverse the list
5. Sort the list (if possible)
6. Print the final result
"""

lst = ['A', 'a', 'c', 1, 2]
print(' Initial list : {}'.format(lst))
lst.append('b')
lst.append(7)
print(' List after appending : {}'.format(lst))
popped_item = lst.pop(1)
print(' After removing an element at index 1 : {}'.format(lst))
lst.reverse()
print(' List in reverse : {}'.format(lst))

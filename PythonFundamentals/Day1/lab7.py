"""
SHOPPING CART PROGRAM
Goal: Combine lists, len(), append(), pop(), indexing
**********************
Simulate a shopping cart using lists.
Steps:
1. Start with an empty list cart = []
2. Ask user 5 times to input an item and append it
3. After all items are added:
    * Print the full cart
    * Remove the last item
    * Show how many items remain
    * Print only the first and last items

"""

cart = []
for i in range (5):
    element = input(' Enter item {} '.format(i+1))
    cart.append(element)
print(' Cart = {}'.format(cart))
removed_item = cart.pop()
print(' Number of items remaining after removing last item : {}'.format(len(cart)))
print(' First element : {} & Last element : {}'.format(cart[0],cart[len(cart)-1]))



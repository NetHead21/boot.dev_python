# No-Index Syntax
# In my opinion, Python has the most elegant syntax for iterating directly over the items in a list without worrying about index numbers. If you don't need the index number you can use the following syntax:

# trees = ['oak', 'pine', 'maple']
# for tree in trees:
#     print(tree)
# # Prints:
# # oak
# # pine
# # maple

# tree, the variable declared using the in keyword, directly accesses the value in the list rather than the index of the value. If we don't need to update the item and only need to access its value then this is a more clean way to write the code.


# When should we use the no-index syntax?

# When we want to write code that is harder to read
#     When we don't need to know the index, just the value
# When the index starts at zero


# Which method of writing for-loops is considered more 'clean' assuming you don't need the index?

#     for item in items
# for i in range(0, len(items))

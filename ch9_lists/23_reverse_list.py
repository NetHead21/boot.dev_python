# Reverse List
# Assignment
# Some of our players would like to view their inventories in reverse order.

# Let's write a function that takes a list as an input and returns a new list except all the items are in reverse order.

# For example:

# [1, 2, 3] -> [3, 2, 1]
# ['a', 'b', 'c', 'd'] -> ['d', 'c', 'b', 'a']

# Tip
# The Python range function is very useful when working with lists.

# Where should you start your loop from?
# Where should you end your loop?
# What should the step be? In other words, how should you increment i in each iteration of the loop?


def reverse_list(items):
    return items[::-1]

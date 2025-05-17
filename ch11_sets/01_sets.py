# Sets
# Sets are like Lists, but they are unordered and they guarantee uniqueness. Only ONE of each value can be in a set.

# fruits = {"apple", "banana", "grape"}
# print(type(fruits))
# # Prints: <class 'set'>

# print(fruits)
# # Prints: {'banana', 'grape', 'apple'}

# Add Values
# fruits = {"apple", "banana", "grape"}
# fruits.add("pear")
# print(fruits)
# # Prints: {'banana', 'grape', 'pear', 'apple'}

# No error will be raised if you add an item already in the set.

# An Empty Set
# Because the empty bracket {} syntax creates an empty dictionary, to create an empty set, you need to use the set() function.

# fruits = set()
# fruits.add("pear")
# print(fruits)
# # Prints: {'pear'}

# Set Iteration
# fruits = {"apple", "banana", "grape"}
# for fruit in fruits:
#     print(fruit)
#     # Prints:
#     # banana
#     # grape
#     # apple

# Note: Sets are unordered, so the order of iteration is not guaranteed.

# Assignment
# Complete the remove_duplicates function. It should take a list of spells that a player has learned and return a new List where there is at most one of each title. You can accomplish this in at least two ways:

# Iteration:

# Create a set to track spells that have been seen
# Create a list to store the unique spells
# Iterate over the list
# If the spell is not in the set, add it to the set and the list
# Return the list
# Set conversion:

# Convert the list to a set
# Convert the set back to a list and return it.
# It makes no sense to learn a spell twice! Once it's learned, it's learned forever.


def remove_duplicates(spells):
    return list(set(spells))


# How do I remove an item from a set?

#     my_set.remove('item')
# my_set.del('item')
# delete my_set['item']
# del my_set['item']


# What is the type of my_val in the following statement: my_val = {}

# Set
# Map
# List
#     Dictionary


# Which would be a good use of a set?

# To store id -> user pairs
#     To store all the possible spells in a game
# To store all the enemies in a game by difficulty

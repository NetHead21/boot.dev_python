# Merge Dictionaries
# Guilds can merge in Fantasy Quest. We need to be able to take two player dictionaries (representing guilds) and merge them into a single guild.

# Assignment
# Complete the merge function. It accepts two dictionaries as input and returns a single merged dictionary that contains all the keys and values from the input dictionaries.

# If a key exists in both dictionaries, the value from the second dictionary should overwrite the value from the first dictionary. Here's the example usage:

# two_towers = {"Frodo": 56, "Aragorn": 10}
# rotk = {"Aragorn": 100, "Gandalf": 809}
# merged_dict = merge(two_towers, rotk)
# print(merged_dict)
# # Output: {'Frodo': 56, 'Aragorn': 100, 'Gandalf': 809}

# Notice how the key Aragorn's value gets overridden. His sword got upgraded.


def merge(dict1, dict2):
    dict1.update(dict2)
    return dict1

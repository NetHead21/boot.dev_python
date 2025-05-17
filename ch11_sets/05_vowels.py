# Vowels
# The anti-spam team at Fantasy Quest is doing text analysis on player's in-game chats.

# Assignment
# Complete the count_vowels function. It takes a string and returns:

# The number of vowels in the string
# A set of the unique vowels found in the string
# We are only interested in the 5 vowels: a, e, i, o, u, and their capitalized versions. Treat uppercase and lowercase vowels as separate. For example, "A" and "a" are not the same.

# Tips
# Create a set of the ten vowels
# Create a counter started at 0
# Create an empty set to store the unique vowels
# Iterate over the characters in the string
# If the character is in the set of vowels:
# Increment the counter
# Add the character to the set of unique vowels
# Return the counter and the set of unique vowels
# New Empty Set
# my_new_set = set()

# New Set With Values
# my_new_set = {"apple", "banana", "grape"}


def count_vowels(text):
    vowels = set("aeiouAEIOU")
    vowel_count = sum(1 for char in text if char in vowels)
    vowel_found = {char for char in text if char in vowels}

    return vowel_count, vowel_found

# If Practice
# Remember, you can use the == operator to check if two values are equal. For example:

# is_equal = 5 == 5
# # is_equal is True

# Assignment
# Complete the check_swords_for_army function. If the number of swords and the number of soldiers match, return the string:

# correct amount

# Otherwise, return the string:

# incorrect amount

# Punctuation matters! Make sure you return the strings exactly as they appear above.

# Tip
# You only need to use one if statement and two return statements to complete the function.


def check_swords_for_army(number_of_swords, number_of_soldiers):
    # if number_of_swords == number_of_soldiers:
    #     return "correct amount"
    # else:
    #     return "incorrect amount"
    return (
        "correct amount"
        if number_of_swords == number_of_soldiers
        else "incorrect amount"
    )

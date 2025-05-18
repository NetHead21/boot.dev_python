# Join Strings
# Remember, in Python the + operator can be used to concatenate (smoosh) strings together. For example:

# print("hello" + " " + "world")
# # hello world

# author = "Tolkien"
# message = "The " + "world never deserved " + author
# print(message)
# # The world never deserved Tolkien

# Assignment
# Complete the join_strings() function. It takes a list of strings and returns a new single string. The new string is the concatenation of all the input strings from the list end-to-end, in order, with a comma between them.

# For example:

# string_list = ["Annie", "Reiner", "Bertholdt"]
# joined_string = join_strings(string_list)
# print(joined_string)
# # "Annie,Reiner,Bertholdt"

# string_list = ["Eren", "Mikasa", "Armin"]
# joined_string = join_strings(string_list)
# print(joined_string)
# # "Eren,Mikasa,Armin"


def join_strings(strings):
    return ",".join(strings)

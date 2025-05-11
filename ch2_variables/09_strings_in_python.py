# F-Strings in Python
# Ever played Pokemon and chosen a funny name so that the in-game messages would come out funny?

# america strength

# In Python we can create strings that contain dynamic values with the f-string syntax.

# num_bananas = 10
# f_string = f"You have {num_bananas} bananas"
# print(f_string)
# # You have 10 bananas

# Opening quotes must be preceded by an f.
# Variables within curly brackets have their values "interpolated" (injected) into the string.
# It's just a string with a special syntax.
# Assignment
# Fix the bug on line 7. Use an f-string to inject the dynamic values into the string:

# Replace NAME with the value of the name variable
# Replace RACE with the value of the race variable
# Replace AGE with the value of the age variable
# Do not "hard-code" the values into the string. For example, this is not the solution we're looking for (even though it happens to work in this case):

# print("Yarl is a dwarf who is 37 years old.")

# We need the player to see their values.

# Punctuation matters! Make sure your output matches the expected output exactly.

name = "Yarl"
age = 37
race = "dwarf"

# Don't edit above this line

print(f"{name} is a {race} who is {age} years old.")

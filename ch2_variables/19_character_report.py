# Character Report
# One of our interns built a program that prints information about Fantasy Quest player characters. It's almost done, but when you were reviewing his code, you found some bugs.

# Assignment
# Fix the bugs to get the character report working!

# Run the code to see it fail.
# Fix the bug with the f-string on line 9.
# Update the syntax so that each variable is the data type you'd expect:
# name: String
# level: Integer
# character_class: String
# armor: Float
# magic_resistance: Float
# account_active: Boolean
# Examples of Data Types
# Type	Rule	Example
# String	Double quotes	"Hello"
# Integer	Whole number	42
# Float	Decimal	2.0
# Boolean	True or False	True

# name = "Lopen"
# level = "25"
# character_class = Windrunner
# armor = 12.4
# magic_resistance = 15
# account_active = "True"

# print("Character Report")
# print("{name} is a level {level} {character_class}.")
# print(f"They have {armor} armor and {magic_resistance} magic resistance.")
# print(f"Their account is currently active: {account_active}")

# # Don't edit below this line

# print("=========================")
# print("Character Report Complete")
# print("Data types:")
# print(
#     f"name: {type(name).__name__}, level: {type(level).__name__}, character_class: {type(character_class).__name__}"
# )
# print(
#     f"armor: {type(armor).__name__}, magic_resistance: {type(magic_resistance).__name__}"
# )
# print(f"account_active: {type(account_active).__name__}")


name = "Lopen"
level = 25
character_class = "Windrunner"
armor = 12.4
magic_resistance = 15.0
account_active = True

print("Character Report")
print(f"{name} is a level {level} {character_class}.")
print(f"They have {armor} armor and {magic_resistance} magic resistance.")
print(f"Their account is currently active: {account_active}")

# Don't edit below this line

print("=========================")
print("Character Report Complete")
print("Data types:")
print(
    f"name: {type(name).__name__}, level: {type(level).__name__}, character_class: {type(character_class).__name__}"
)
print(
    f"armor: {type(armor).__name__}, magic_resistance: {type(magic_resistance).__name__}"
)
print(f"account_active: {type(account_active).__name__}")

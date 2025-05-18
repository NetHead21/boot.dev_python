# List Division
# Remember, in Python you can divide two numbers using the / operator. For example:

# print(6 / 2) # 3.0
# print(8 / 4) # 2.0

# You can also iterate over each item in a list using a for in loop. For example:

# numbers = [1, 7, 3, 2, 5]
# for num in numbers:
#     print(num)
# # 1
# # 7
# # 3
# # 2
# # 5

# Assignment
# Complete the divide_list() function. It takes a list and a number as input, and should return a new list that contains all the elements of the original list after dividing them by the second input.

# For example:

# divided_list = divide_list([6, 8, 10], 2)
# print(divided_list)
# # [3.0, 4.0, 5.0]


def divide_list(nums, divisor):
    return [i / divisor for i in nums]

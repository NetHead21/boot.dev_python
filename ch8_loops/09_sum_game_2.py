# Sum Game 2
# Assignment
# Complete the sum_of_odd_numbers function. It should calculate the sum of all the odd numbers starting at 1 up to (but not including) the given end number and return the result.

# Tips
# What number should you start with if you only want odd numbers?
# How much should you increment by in each iteration of the loop to get the next odd number?


def sum_of_odd_numbers(end):
    return sum([i for i in range(end) if i % 2 != 0])

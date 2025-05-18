# Number Sum
# In this chapter we are going to hammer down the concepts we've learned by running through a bunch of practice problems without introducing any new concepts.

# Assignment
# Complete the number_sum function. It should add up all the numbers from 1 to n. For example:

# number_sum(5) -> 1+2+3+4+5 -> 15
# number_sum(3) -> 1+2+3 -> 6


def number_sum(n):
    return sum(i for i in range(1, n + 1))

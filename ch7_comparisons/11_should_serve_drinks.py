# Should Serve Drinks
# Assignment
# In Fantasy Quest, players can go to a town's local pub. Drinking virtual beer refills their stamina!

# Complete the function that determines if a bartender should serve drinks to a customer. Only return True if all of these conditions apply. If any of these conditions are False, return False:

# The customer's age is 21 or older
# The bartender is working
# The time is at least 5 but no later than 10
# Tips
# Understand the Problem
# This assignment tests your ability to think critically by challenging your expectations up to this point. First, understand the problem before rushing to conclusions about the requirements. Then, convert these positive conditions into negatives. Finally, convert them into code.

# If the customer's age is less than 21, return False.
# If the bartender is on break, return False.
# If the time is before 5 or after 10, return False.
# Return True.
# Why go through the hassle of inverting the logic? The alternative is to write a function that is deeply nested and therefore less readable and more confusing than the solution.

# def check_conditions(condition_1, condition_2, condition_3):
#     if condition_1:
#         if not condition_2:
#             if condition_3 > 1:
#                 return True
#     return False

# If Statements Don't Need a Comparison
# Where "is_big" is a boolean value, the following statements are identical:

# if is_big:
#     # ...

# if is_big == True:
#     # ...

# The first option should be preferred due to length; however, the second is more readable. The == True is redundant.


def should_serve_customer(customer_age, on_break, time):
    return customer_age >= 21 and not on_break and time >= 5 and time <= 10

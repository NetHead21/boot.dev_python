# Counting Practice
# Checking for Existence
# If you're unsure whether a key exists in a dictionary, use the in keyword.

# cars = {
#     "ford": "f150",
#     "toyota": "camry"
# }

# print("ford" in cars)
# # Prints: True

# print("gmc" in cars)
# # Prints: False

# Assignment
# We need to be able to report to our players how many enemies are in their immediate vicinity - but they want the count of each enemy by its kind. Fix the count_enemies function. It accepts as input:

# enemy_names: a list of strings.
# It should return a dictionary where:

# The keys are all the enemy names from the list
# The values are the counts of how many times each enemy appeared in the list.
# Run the code in its current state. It will raise a KeyError.
# Fix the code.


def count_enemies(enemy_names):
    enemies_dict = {}
    for enemy_name in enemy_names:
        enemies_dict[enemy_name] += 1
    return enemies_dict

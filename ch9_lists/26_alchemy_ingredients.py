# Alchemy Ingredients
# Fantasy Quest added a new Alchemy skill.

# Assignment
# Complete the check_ingredient_match function. It accepts two lists of strings:

# recipe: The list of ingredients needed.
# ingredients: The list of ingredients the character has.
# It should return two values:

# A float representing the percentage of required ingredients the character has.
# A new list of ingredients the character is missing but that are required.
# For example, if these were the lists:

# recipe = ["Dragon Scale", "Unicorn Hair", "Phoenix Feather", "Troll Tusk"]
# ingredients = ["Dragon Scale", "Phoenix Feather", "Troll Tusk"]

# percentage, missing_ingredients = check_ingredient_match(recipe, ingredients)
# print(percentage, missing_ingredients)
# # Prints: 75.00 ["Unicorn Hair"]


def check_ingredient_match(recipe, ingredients):
    # Convert recipe to a set for lookup efficiency
    recipe_set = set(recipe)

    # Ensure ingredients counted are only those from the recipe (ignoring extras)
    matched_ingredients = [item for item in ingredients if item in recipe_set]

    # Compute the number of unique matches
    unique_matches = set(
        matched_ingredients
    )  # Ensure duplicates don't inflate the percentage

    # Find missing ingredients
    missing_ingredients = [item for item in recipe if item not in unique_matches]

    # Calculate the correct percentage
    percentage = (len(unique_matches) / len(recipe)) * 100 if recipe else 0.0

    return round(percentage, 2), missing_ingredients

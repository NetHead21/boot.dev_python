# Multiple Return Values
# A function can return more than one value by separating them with commas.

# def cast_iceblast(wizard_level, start_mana):
#     damage = wizard_level * 2
#     new_mana = start_mana - 10
#     return damage, new_mana # return two values

# Receiving Multiple Values
# When calling a function that returns multiple values, you can assign them to multiple variables.

# dmg, mana = cast_iceblast(5, 100)
# print(f"Damage: {dmg}, Remaining Mana: {mana}")
# # Damage: 10, Remaining Mana: 90

# When cast_iceblast is called, it returns two values. The first value is assigned to dmg, and the second value is assigned to mana. Just like function inputs, it's the order of the values that matters, not the variable names. We could just as easily called the variables one and two:

# one, two = cast_iceblast(5, 100)
# print(f"Damage: {one}, Remaining Mana: {two}")
# # Damage: 10, Remaining Mana: 90

# That said, descriptive variable names make your code easy to understand, so use them!

# What Happened to the Variables?
# The damage and new_mana variables from cast_iceblast's function body only exist inside of the function. They can't be used outside of the function. We'll explain that more later when we talk about scope.

# Assignment
# Complete the become_warrior function. It accepts 2 inputs: the full_name string, and the power integer. It should return 2 values: a "title" string and a "new power" integer.

# Create the title using f-strings. Combine full_name with "the warrior" in this format:
# full_name the warrior

# Create the new_power value that is equal to the input power plus one.
# Return both title and new_power
# For example:

# title, power = become_warrior("Aang Airbender", 100)
# print(title)
# # "Aang Airbender the warrior"
# print(power)
# # 101


def become_warrior(full_name, power):
    return f"{full_name} the warrior", power + 1


# Don't edit below this line


def main():
    test("Frodo Baggins", 5)
    test("Bilbo Baggins", 10)
    test("Gandalf The Grey", 9000)


def test(input1, input2):
    result1, result2 = become_warrior(input1, input2)
    print(result1, "has a power level of:", result2)


main()

# Order of Functions
# All functions must be defined before they're used.

# You might think this would make structuring Python code hard because the order of the functions needs to be just right. As it turns out, there's a simple trick that makes it super easy.

# Most Python developers solve this problem by defining all the functions in their program first, then they call an "entry point" function last. That way all of the functions have been read by the Python interpreter before the first one is called.

# Conventionally this "entry point" function is usually called main to keep things simple and consistent.

# def main():
#     health = 10
#     armor = 5
#     add_armor(health, armor)

# def add_armor(h, a):
#     new_health = h + a
#     print_health(new_health)

# def print_health(new_health):
#     print(f"The player now has {new_health} health")

# # call entrypoint last
# main()


# Functions must be ____ before they can be ____
#     defined, called
# called, defined


# Functions must be defined in the order that they call each other.
# True
#     False


# Which is best practice to make sure you don't define functions out of order?

#     Create an entrypoint function (usually called main) and call it at the end of the file
# Create a function called main, Python will always call it first
# Create a function called main and call it at the beginning of the file
# Create a function called entrypoint, Python will always call it first

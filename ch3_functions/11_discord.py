# Discord
# Getting help is a critical part of learning to code (and even in your day to day working as a developer). We've already talked about Boots and spellbooks, which are great first lines of defense. But what else can you do?

# First, it's totally normal to look stuff up online as you work on Boot.dev. It's not cheating. It's impossible to memorize everything, and it's frankly just not necessary, even as a professional developer.

# Second, sometimes you just need a human. Luckily, we have an amazing Discord community full of developers and fellow students ready to help you out. So,

# Open our Discord community page
# Join the server and sync your account
# With your account linked up, you'll be able to chat with other learners and mentors, as well as use the #help forums to ask questions
# Additionally, if you help others in the Discord, you'll earn karma that will help you earn fellowship achievements
# Assignment
# Enough Discord talk, back to writing code.

# In Fantasy Quest, characters lose health due to heat exhaustion. The game tracks the temperature in Freedom units (Fahrenheit), but we need to display the temperature in Celsius for players outside the US. Here's the formula to calculate the temperature in Celsius from Fahrenheit (f):

# 5/9 * (f - 32)

# Complete the to_celsius function body. It should return the temperature in Celsius for a given Fahrenheit temperature (f parameter).


def to_celsius(f):
    return 5 / 9 * (f - 32)


## Don't touch below this line


def test(f):
    c = round(to_celsius(f), 2)
    print(f, "degrees fahrenheit is", c, "degrees celsius")


test(100)
test(88)
test(104)
test(112)

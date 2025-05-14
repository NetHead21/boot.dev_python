# Experience Points
# Adventurers need experience points (XP) to level up and become stronger. We want to show the total XP a player has gained given their current level.

# Each character starts with 0 XP at level 1. To reach the next level, they need XP equal to their current level times 5.

# Level	XP so far	XP for next level
# 1	0	5
# 2	5	10
# 3	15	15
# 4	30	20
# Assignment
# Complete the calculate_experience_points function.

# It accepts a level (integer) and returns the total XP a player has gained so far.


def calculate_experience_points(level):
    total_xp = 0
    for i in range(1, level):
        total_xp += i * 5
    return total_xp

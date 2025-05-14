# Even Teams
# Fantasy Quest PvP teams are uneven when the match begins. We need a function that will correctly split the two teams evenly.

# Assignment
# Complete the split_players_into_teams function.

# It accepts a list of players (strings representing their names) and returns two lists in this order:

# A new list of all the players with even-numbered indexes in the original list.
# A new list of all the players with odd-numbered indexes in the original list.
# Use a slice with a "step" to create two new lists from the players list. Don't be afraid to consult your spellbook for list slicing help!


def split_players_into_teams(players):
    return players[::2], players[1::2]

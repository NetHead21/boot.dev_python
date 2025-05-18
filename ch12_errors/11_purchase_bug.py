# Purchase Bug
# There's a bug in the merchant system that allows players to buy items from the shop even when they don't have enough gold.

# Assignment
# Complete the purchase_item function.

# If the character doesn't have enough gold raise an Exception with the text not enough gold.
# Otherwise, return the amount of remaining money the customer has after completing the purchase.


def purchase_item(price, gold_available):
    if gold_available >= price:
        return gold_available - price
    else:
        raise Exception("not enough gold")

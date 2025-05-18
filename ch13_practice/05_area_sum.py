# Area Sum
# The area of a rectangle is calculated by multiplying its height and width. For example, the area of a rectangle with a height of 3 and a width of 5 is:

# 3 * 5 = 15

# area of rect

# Assignment
# Complete the area_sum() function. It accepts a list of rectangles, where each rectangle is a dictionary that has the following structure:

# {
#   "height": 5,
#   "width": 6
# }

# It should calculate the area of each rectangle and return the sum of all the areas.


def area_sum(rectangles):
    # sum_of_areas = 0

    # for element in rectangles:
    #     sum_of_areas += (element['height'] * element['width'])

    # return sum_of_areas
    return sum(element["height"] * element["width"] for element in rectangles)

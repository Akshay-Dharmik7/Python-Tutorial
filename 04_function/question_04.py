# 4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math

def circle_stat(radius):

    # calculate area of circle
    area = math.pi * radius ** 2

    # calculate circumference of circle
    circumference = 2 * math.pi * radius

    return {
        "area" : round(area, 3),
        "circumference" : round(circumference, 3)
    }

print(circle_stat(4))
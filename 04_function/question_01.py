# 1. Basic Function Syntax
# Problem: Write a function to calculate and return the square of a number.

def calc_square(number):

    if number == 0:
        return None
    else:
        return number ** 2

print(calc_square(5))

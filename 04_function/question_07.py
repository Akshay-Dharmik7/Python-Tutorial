# 7. Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_all(*args):
    return sum(args)

# we can used any name instead of args
# def sum_all(*vals):
#     return sum(vals)

print(sum_all(1, 2, 3, 4))
print(sum_all(1, 2, 3, 4, 5, 6))
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))
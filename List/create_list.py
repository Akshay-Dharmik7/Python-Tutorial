# using []
# 1.1 empty list
empty = []
print(empty)
print(type(empty))
# -------------------------------------------
# 1.2 number list
numbers = [1, 2, 3, 4]
print(numbers)
# -------------------------------------------
# 1.3 letter list
letters = ['a', 'b', 'c']
print(letters)
# -------------------------------------------

# 1.4 mixed list
mixed_list = [1, 'a', 2, 'b', True]
print(mixed_list)
# -------------------------------------------

# using list() function.
# 2.1 empty list
empty = list()
print(empty)
# -------------------------------------------

# 2.2 numbers list
# range function
numbers = list(range(5))
print(numbers)
# -------------------------------------------
# 2.3 letters list
letters = list("akshay")
print(letters)


# single dimension list
# multi-dimension list - nested list
# 3.1 number nexted list
number_matrix_list = [[1,2,3], [4, 5, 6]]
print(number_matrix_list)

# 3.2 letter nested list
letters_matrix_list = [['a', 'b', 'c'], ['d', 'e', 'f']]
print(letters_matrix_list)

# 3.3 mixed nested list
mixed_matrix_list = [[1, 2, 3], ['a', 'b', 'c'], [True, False]]
print(mixed_matrix_list)
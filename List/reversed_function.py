# Single list
list1 = [1, 3, 6, 4, 7]

new_list = list(reversed(list1))
print("Original List:", list1)
print("Reversed List:", new_list)


# matrix list
matrix_list = [
    ['d', 'e', 'f'],
    ['a', 'b', 'c'],
    ['g', 'h', 'i']
]

# sort in accending
new_matrix_list = list(reversed(matrix_list))
print("Original List:", matrix_list)
print("Reversed List:", new_matrix_list)

# Reversed() funtion not create a duplicate reversed list, its create iterator object
# to create a duplicate list we need to wrap the reversed() function into a list() function.





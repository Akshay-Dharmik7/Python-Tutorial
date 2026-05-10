# reference copy
# list1 = [1, 3, 2, 4]
# list2 = list1
# list2.append(5)
# print("Original List", list1)
# print("New List", list2)

# copying list using assgiment operation will cause issue in oroginal list if we performing operation on new list.


# shallow copy
# reference copy
# matrix_list1 = [
#     [1, 3, 2, 4],
#     [6, 9, 4, 8]
# ]
# matrix_list2 = matrix_list1.copy()
# matrix_list1.pop()
# matrix_list2[0].append(5)
# print("Original List", matrix_list1)
# print("New List", matrix_list2)

# matrix_list2.pop()
# print("Original List after pop ", matrix_list1)
# print("New List after pop ", matrix_list2)

# deep copy
# import copy
# matrix_list1 = [
#     [1, 3, 2, 4],
#     [6, 9, 4, 8]
# ]
# matrix_list2 = copy.deepcopy(matrix_list1)
# matrix_list1.pop()
# matrix_list2[0].append(5)
# print("Original List", matrix_list1)
# print("New List", matrix_list2)

# to check independent copy is created or not we can we IS operator.

import copy

# assigment
original = [
    [1, 3, 2, 4],
    [6, 9, 4, 8]
]

copy1 = original
print("Shared Object?", original is copy1, "\n")

# shallow copy
copy2  = original.copy()
print("Shared Object?", original is copy2)
print("Shared List?", original[0] is copy2[0], "\n")

# deep copy
copy3  = copy.deepcopy(original)
print("Shared Object?", original is copy3)
print("Shared List?", original[0] is copy3[0], "\n")
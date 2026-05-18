list = [1, 5, 5, 4, 3]

# 1- max()
print("Max: ", max(list))

# 2- min()
print("Min: ", min(list))

# 3- sum()
print("Sum: ", sum(list))

# 4- len()
print("Length: ", len(list))

# 5- all()
print("All: ", all(list))
print("All: ", all([1, 0, 2]))
print("All: ", all(['a', '', 'b']))
print("All: ", all(['a', 'b', 'c']))

# 5- any()
print("Any: ", any(list))
print("Any: ", any([1, 0, 2]))
print("Any: ", any(['a', '', 'b']))
print("Any: ", any([0, 0, 0]))

# METHODS of List
# 1- .count()
print("Count: ", list.count(5))

# 2- .index()
print("Index: ", list.index(5))

# Operators for List
# 1. In
print(4 in list)
print(8 in list)
print(8 not in list)

# 2 Comparison operators
list1 = [5, 2, 3]
list2 = [2, 5, 3]

print(list1 == list2)
print(list1 > list2)
# Note python only check first element and gives result based on comparing 1st index of both list.

list1 = [5, 2, 3]
list2 = [5, 2, 3]
print(list1 is list2)

# is check for addresses for both the list, as address wll be different so it will give result as False.



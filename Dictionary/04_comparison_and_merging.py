dict1  = {'id': 101, 'name' : 'akshay', 'post' : "Software Engineer"}

sal = {'salary' : 30000}

# 1) ==: Equality check
print(dict1 == sal)

# 2) !=Inequality check.
print(dict1 != sal)

# 3) | Merge dictionaries.
print(dict1 | sal)

# 4) Update in-place:
# print(dict1 |= sal) #not working
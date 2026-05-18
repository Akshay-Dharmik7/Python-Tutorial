list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [1, 2, 4, 6, 3]
list3 = ['a', 'b', '', 'd', 'e']
list4 = [1, 2, 4, 0, 3]
list5 = [1, 2, 4, 0, 3, None]
list6 = [1, 2, 4, 0, 3, False]
list7 = []

# max()
# print(max(list1))
# print(max(list2))

# min()
# print(min(list1))
# print(min(list2))

# len()
# print(len(list1))
# print(len(list2))

# all()
# print(all(list1))
# print(all(list2))
# print(all(list3))
# print(all(list4))
# print(all(list5))
# print(all(list6))

# any()
# print(any(list1))
# print(any(list2))
# print(any(list3))
# print(any(list4))
# print(any(list5))
# print(any(list6))
# print(any(list7))

# sum()
# print(sum(list1)) //char list
# print(sum(list2))

# sorted()
# print(sorted(list1))
# print(sorted(list2))
# print(sorted(list3))
# print(sorted(list4))
# # print(sorted(list5)) // none value
# print(sorted(list6))

# reversed()
# print(list(reversed(list1)))
# print(list(reversed(list2)))
# print(list(reversed(list3)))
# print(list(reversed(list4)))
# print(list(reversed(list5)))
# print(list(reversed(list6)))

# zip()
# print(list(zip(list1, list2))) #gives set of tuples.
# print(list(zip(list1, list2, '$%@&*^'))) #gives set of tuples.

# enamurate()
# print(list(enumerate(list1)))
# for index, value in enumerate(list1):
#     print(index, value)

# map()

# print(list(map(str.upper, list1)))
# print(list(map(str, list2)))
# print(list(map(int, list1))) #char cannot be converted into numeric value

# filter
listalphanum = ['1', 'a', '2', 'b', '3', 'c']
print(list(filter(str.isalpha, listalphanum)))
print(list(filter(str.isdecimal, listalphanum)))


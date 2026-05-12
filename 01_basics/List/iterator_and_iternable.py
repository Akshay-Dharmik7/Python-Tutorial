list1 = ['a', 'b', 'c', 'd']

for i in list1:
    print(i)

# enamurate(iterable)
# this functon is used to iterate over list and also gives index of that element present in list.

for index, value in enumerate(list1):
    print(index, value)

# map(function, iterable)
# this function is used to perform certain operation on each element in list and assigned or print transformed element.
print(list(map(str.upper, list1)))

list2 = ['1', '2', '3', '4']

print(list(map(int, list2)))

for value in list(map(int, list2)):
    print(value)

# filter
# this function is used to filter out the list
# if we want to remove unwanted, falsy data from list and just gives true data, then this function is used.

list3 = ['a', '', 'b', None, 'c', False]

print(list(filter(None, list3)))

# similarly we can use bool funtion
print(list(filter(bool, list3)))

list4 = ['a', '11', 'b' , '222']

for i in filter(str.isalpha, list4):
    print(i)

for i in filter(str.isalnum, list4):
    print(i)
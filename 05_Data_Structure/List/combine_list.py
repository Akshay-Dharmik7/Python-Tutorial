# Combine simple list
numbers = [1,2, 3]
letters = ['a','b','c']

comb1 = numbers + letters
print(comb1)

# combine nested list
comb2 = [numbers , letters]
print("nested list ", comb2)

# using extend method
# If we dont want to createe new list just want to add in existing list
numbers1 = [1,2, 3]
letters1 = ['a','b','c']

numbers1 = numbers1.extend(letters)
print(numbers)

# using zip() function
numbers2 = [1,2, 3]
letters2 = ['a','b','c']

comb2 = list(zip(numbers2, letters2))
print(comb2)

# usecase of using zip() function
#  - In real time dat if we want to map the values then we can used zip() function.
#  - for example if I want to checkk which ID associated with which name then we can use zip function

# Cons
#  - zip function will goes only the less value of list.
numbers3 = [1,2, 3]
letters3 = ['a','b','c', 'd']

comb3 = list(zip(numbers3, letters3))
print(comb3)

# in above example we cna see letter3[3] = 'd' not mapped it is skipped.

# pros
# - we can also map string character with list

numbers4 = [1,2, 3]
letters4 = ['a','b','c', 'd']

comb4 = list(zip(numbers4, letters4, 'Hi'))
print(comb4)
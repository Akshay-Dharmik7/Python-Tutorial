setdata1 = {1, 2, 6, 'a', 5, 'c', 6}
print(setdata1)
setdata2 = {1, 2, 'a', 7, 4, 'c', 5, 8, 'b'}
print(setdata2)

# 1) union() or |:
print('union: ', setdata1 | setdata2) #all elements from both sets.
# or
print('union: ', setdata1.union(setdata2))

# 2) intersection() or &:
print('intersection:', setdata1 & setdata2) #common element in both the sets.
# or
print( 'intersection:',setdata1.intersection(setdata2))

# 3) difference() or -:
print('difference: ', setdata1 - setdata2) #element present in setdata1 but not in setdata2.
# or
print('difference: ', setdata1.difference(setdata2))

# 4) symmetric_difference() or  ^: 
print('symmetric_difference: ', setdata1 ^ setdata2) #element should be present either in one of the set, but not in both.
print('symmetric_difference: ', setdata1.symmetric_difference(setdata2))

# 5) issubset() or <= :
print('issubset: ', setdata1 <= setdata2) #all elements of setdata1 should be present in setdata2
print('issubset: ', setdata1.issubset(setdata2))

# 6) issuperset() or >= :
print('issuperset: ', setdata1 <= setdata2) #all elements of setdata2 should be present in setdata1
print('issuperset: ', setdata1.issuperset(setdata2))

# 7) isdisjoint() or :
print(setdata1.isdisjoint(setdata2)) #no common elements


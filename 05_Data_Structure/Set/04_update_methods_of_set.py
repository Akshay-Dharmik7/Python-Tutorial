setdata1 = {1, 2, 6, 'a', 5, 'c', 6}
setdata2 = {'a', 'b', 'c', 'd'}

# 1) .update(x):
setdata1.update(setdata2)
print(setdata1)

# 2) .intersection_update(x):
setdata1.intersection_update(setdata2)
print(setdata1)

# 3) .difference_update(x):
setdata1.difference_update(setdata2)
print(setdata1)

# 4) .symmetric_difference_update(x):
setdata1.symmetric_difference_update(setdata2)
print(setdata1)


setdata1 = {1, 2, 6, 'a', 5, 'c', 6}
setdata2 = {1, 2, 6, 5, 6}
setdata3 = {'a', 'b', 'c'}

# 1) len():
print(len(setdata1))

# 2) sum :
# print(sum(setdata1)) #error  due to multiple datatypes in set.
print(sum(setdata2)) 
# print(sum(setdata3))  #error not works for characters

# 3) min() 
print(min(setdata2))

# 4) max() 
print(max(setdata2))

# 5) sorted():
print(sorted(setdata2))

# 6) any():
print(any(setdata1))

# 7) all():
print(all(setdata1))

# 8) enumerate():
for i, v in enumerate(setdata1):
    print(f'index of element {v}  is {i}')

# 9) zip():
print(set(zip(setdata1, setdata2)))

# 10) set():
print(set([1, 2, 3, 44, 5, 6]))
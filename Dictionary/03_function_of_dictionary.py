dict1  = {'id': 101, 'name' : 'akshay', 'post' : "Software Engineer"}

dict2 = {1: 'a', 2: 'b', 3: 'c'}

# 1) len():
print(len(dict1))

# 2) sorted(d):
print(sorted(dict1))

# 3) sorted(d.values):
print(sorted(dict2.values()))

# 4) sorted(d.items())
print(sorted(dict2.items()))

# 5) enumerate(d):
for v, k in enumerate(dict1):
    print(f'value for key {k} is {v}')

# 6) zip():
print(dict(zip(dict1.keys(), dict2.values())))

# 7) dict(iterable):
print(dict([('a', 1), ('b', 2)]))

# 8) all():
print(all(dict1))

# 9) any():
print(any(dict1))


result = lambda x : x*2
print(result(2))

# lambda with map function

list1 = ['a', 'b','c']

print(list(map(lambda x : x.upper(), list1)))

prices = ['$12.50', '$13.40', '$15.70']

print(list(map(lambda p : float(p.replace('$', '')), prices)))

# lambda with filter

pricess = [100, 40, 50, 200]

print(list(filter(lambda p : p >= 50, pricess)))

students = [
    ['Maria', 85],
    ['Kumar', 90],
    ['Max', 60]
]

print(list(filter(lambda s :s[1] > 70, students)))

print(list(filter(lambda s : s[0].startswith('M'), students)))



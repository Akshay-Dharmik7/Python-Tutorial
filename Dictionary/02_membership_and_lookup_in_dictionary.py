dict  = {'id': 101, 'name' : 'akshay', 'post' : "Software Engineer"}

# 1) in:
print('id' in dict)

# 2) not in:
print('id' not in dict)

# 3) d[key]:
print(dict['id'])

# 4) d[value]:
dict['id'] = 102
print(dict)

# 5) det d[key]:
del dict['id']
print(dict)


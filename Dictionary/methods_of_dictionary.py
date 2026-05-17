dict  = {'id': 101, 'name' : 'akshay', 'post' : "Software Engineer"}

sal = {'salary' : 30000}

# 1) get():
print(dict.get('id'))
print(dict.get('id1', 'none'))

# 2) keys():
print(dict.keys())

# 3) values():
print(dict.values())

# 4) items():
print(dict.items())

# 5) pop():
print(dict.pop('id', 'none'))
print(dict.pop('id1', 'none'))

# 6) popitem():
print(dict.popitem())

# 7) clear():
print(dict.clear())

# 8) update():
print(dict.update(sal))
print(dict)

# 9) setdefault():
print(dict.setdefault('salary', 'none'))
print(dict.setdefault('id1', 'none'))

# 10) copy():
dict2 = dict.copy()
print(dict2)


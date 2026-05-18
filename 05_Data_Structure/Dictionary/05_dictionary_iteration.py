dict1  = {'id': 101, 'name' : 'akshay', 'post' : "Software Engineer"}

for key in dict1:
    print(key)

for value in dict1.values():
    print(value)

for key, value in dict1.items():
    print(f'key: {key}, value: {value}')
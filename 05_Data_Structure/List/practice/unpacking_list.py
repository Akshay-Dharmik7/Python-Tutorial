list1 = ['akshay', 25, 'software developer', 'jaipur', 25000]

# name, age, post, location, salary = list1
# print(name)
# print(age)
# print(post)
# print(location)
# print(salary)

# name, *details, salary = list1
# print(name)
# print(details)
# print(salary)

# name, _,_, _, salary = list1
# print(name)
# print(salary)

name, *_, salary = list1
print(name)
print(salary)
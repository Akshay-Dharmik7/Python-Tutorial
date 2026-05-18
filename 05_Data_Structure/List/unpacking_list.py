list = ['akshay', 25, 'software develper', 'pune']

name, age, role, location = list

print(name)
print(age)
print(role)
print(location)

# Note: In order to unpack the list we need to declare variable order to the list of variable, so that correct value will get assigned to correct variable.


# REST COOLECTOR
#  Astrick *

name, *details, location = list
print(name)
print(details)
print(location)

name, *details = list
print(name)
print(details)

*details, location = list
print(details)
print(location)

# Note: In unpacking, its only allow one * to used, if we try to use another then it will shows error.

# Unpacking Rules
# 1. numbers of variables must be matching the number of values if we are not using *.
# 2. Astricks collect leftover, and its fine if there are none.
list2 = ["akshay"]
name, *details = list2
print(name)
print(details)

# 3. We can unpack any sequence (list, tuple, string, etc)
string = 'hi'
letone, lettwo = string
print(letone)
print(lettwo)

# Unpacking using (_)
# we can use _ if we want specific details and skips others.
name1 , _ , role1 , _ = list
print(name1)
print(role1)

# using * and _ combine
# when we have n numbers of values in list and want to skip those and use only few values then this method is useful.

list3 = ["akshay", 25, "software developer", "pune", "india"]

name, *_, country = list3
print(name)
print(country)

*_, country = list3
print(country)

# 8. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def user_data(**kwargs):
    return kwargs

print(user_data(Name = "Akshay", Age = 25, Designation = "Software Engineer" ))

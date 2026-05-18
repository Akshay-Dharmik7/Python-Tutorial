# 8. Age Validator (Raising Exceptions)
# Task: Write a function register_voter(age) that takes an integer.    
# Keyword to use: raise.  
# Goal: If the age is less than 18, manually raise a ValueError with a custom message: "Must be 18 or older to register."

def register_voter(age):
    if age < 18:
        raise ValueError('Must be 18 or older to register.')

try:
    age = int(input('Enter the age: '))
    register_voter(age)

except ValueError as e:
    print(e)
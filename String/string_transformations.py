# replace()
phone_number = "+1234 567 890"
print(phone_number.replace(" ", "/"))

price = "$1234.99"
print(price.replace("$" , ""))

phone_number = "+123/ 4567/890"
print(phone_number.replace("/", "").replace(" ", ""))
print("-" * 100)
# ----------------------------------------------------------------------------------------------------------

# cocat using operator

first_name = "Akshay"
last_name = "Dharmik"

full_name = first_name +" " +last_name
print(full_name)
print("-" * 100)
# ----------------------------------------------------------------------------------------------------------
# f_string
# purpose of using this advance string is for more readability and easy to understand if we are concatining multiple data types.

name = "Akshay"
age = 25
job_status = True

print("My name is " + name +", my  age is "+ str(age) +" and job status is "+ str(job_status)+".")
# in aaboe string we can see there are multiple concat operation and to concat we have to convert data type other than string into string using str() function.
# to make this more easier we use f-string.
print(f"My name is {name} , my age is {age} and job status is {job_status}.")
print("-" * 100)
# we can easily read the string  using formated string.
# to use formatted string (f-string) we need to delacre f at begining of the string.

# We can also use "," for concating different data types but it is only work within print statement.
# if we are assigning value to another string then it is giving as seperate string inclding ",".
print("My name is", name , "," , "my age is", age, "and job status is", job_status)
text = "My name is", name , "," , "my age is", age, "and job status is", job_status
print(text)
# it act as list
# ---------------------------------------------------------------------------------------------------------

#split()
names = "akshay,raghav,raman,sushant,karan"

print(names.split(","))
print("-" * 100)
# ----------------------------------------------------------------------------------------------------------

# string repitation
print("ha"* 4)
print("-" * 100)
# ----------------------------------------------------------------------------------------------------------

# indexing and slicing
# Indexing

string = "hello"

# extract first character
print(string[0])
print(string[-5])

# extract firallst character
print(string[0])
print(string[1])
print(string[2])
print(string[3])
print(string[4])

#exctract last character
print(string[4]) 
print(string[-1]) 


# Slicing
date = "2026-15-04"

# extract year
print(date[0:4])
print(date[:4])

# exctract month - open ended slicing
print(date[-2:])

# exctract date
print(date[5:7])
print(date[-5:-3])

# open ended slicing
print(date[8:])

# step slicing
str = "hello"
print(str[0:5:2])

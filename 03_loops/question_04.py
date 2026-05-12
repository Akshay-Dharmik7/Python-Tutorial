# 4. Reverse a String
# Problem: Reverse a string using a loop.

str_name = input("Enter string ")
reversed_str = ""
for str in str_name:
    reversed_str = str + reversed_str

print("reversed string is", reversed_str)
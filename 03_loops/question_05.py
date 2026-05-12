# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

str_name = input("Enter string ") #str_name ="teeter"

first_non_repeated_char = ""

for str in str_name:
    if str_name.count(str) == 1:
        first_non_repeated_char = str
        break

print("First non repeated character is", first_non_repeated_char)
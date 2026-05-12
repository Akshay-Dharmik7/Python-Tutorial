# Searching in string
# 1. value present at start- string startwith
number = "+91-7654323456"
print(number.startswith("+91"))
# ----------------------------------------------------

# 2. value present at end- string endswith
print(number.endswith("6"))
# ----------------------------------------------------

# 3. value present anywhere in string
# 3.1 gives output as TRUE/FALSE
print("7" in number)
# ----------------------------------------------------

# 3.2 gives  output as starting index.
print(number.find("7"))

# if value is present ofr find() function then it will return index of that character.
# else it will return -1 (character not present in string)
print(number.find("78"))
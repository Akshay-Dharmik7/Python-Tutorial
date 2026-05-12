# Convert a messy phone number into a clear number format with only digits.

phone_number = "+49 (176) 123-4567"
print("Before Replace : " + phone_number)
phone_number = phone_number.replace("+", "").replace("(", "").replace(")" , "").replace(" ", "").replace("-", "")
print("After replace : " + "00" +phone_number)


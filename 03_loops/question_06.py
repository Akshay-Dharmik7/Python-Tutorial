# 6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

number = int(input("Enter the number "))
fact_num = 1
while number > 0:
    fact_num = fact_num * number
    number -= 1

print("Factorial of number is", fact_num)


# 8. Prime Number Checker
# Problem: Check if a number is prime.

number = int(input("Enter the number "))
count = 0

if number > 1:
    for num in range(1, int(number**0.5+1)):
        if number % num == 0:
            count += 1
else:
    print("Quite diffuclt to say number is prime of not")

if count == 1:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")

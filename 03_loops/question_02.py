# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

number = int(input("Enter the number "))

sum_of_even = 0

for num in range(1, number+1):
    if  num % 2 == 0:
        sum_of_even += 1

print("Sum of even numbers to", number, "is", sum_of_even)
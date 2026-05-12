# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.


while True:
    number = int(input("Enter the number "))

    if number <1 or number > 10:
        print("You entered invalid number")
        break
    print("Number is ", number)

# Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input("Enter the age"))
day = input("Enter the day")

# shorthand if-else statement
price = (12 if age >= 18 else 8) 

if day.lower() == "wednesday":
    price -= 2

print("Ticket price for you is $",price)



# 10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet = input("Enter the pet name ")
age = int(input("Enter "+ pet + "age "))

if pet == "Dog":
    if age < 2:
        food = "Puppy Food"
    else:
        food = "not fixed"
elif pet == "Cat":
    if age > 5:
        food = "Senior Cat Food"
    else:
        food = "not fixed"

print("For", pet, "food is", food)
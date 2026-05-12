# 1. Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

age = input("Enter the age: ")
int_age = int(age)

if int_age < 13:
    print("Child")
elif int_age >= 13 and int_age <=19:
    print("Teenager")
elif int_age >= 20 and int_age <= 59:
    print("Adult")
else:
    print("Senior")

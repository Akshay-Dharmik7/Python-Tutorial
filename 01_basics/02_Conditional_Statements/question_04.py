# 4. Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = input ("Enter fruit name ")

fruit_colour = input("Enter fruit colour")

if fruit == "Banana":
    if fruit_colour == "Green":
        print("Unripe")
    elif fruit_colour == "Yellow":
        print("Ripe")
    elif fruit_colour == "Brown":
        print("Overripe")
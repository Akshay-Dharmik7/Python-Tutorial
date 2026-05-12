# 7. Coffee Customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_size = input("Type of ordered coffee ")
extra_shot = input("need Extra Shot of expresso Yes/No ")

if extra_shot == "Yes":
    coffee = order_size + " Coffee with an Extra Shot of expresso"
else:
    coffee = order_size + " Coffee"

print(coffee)
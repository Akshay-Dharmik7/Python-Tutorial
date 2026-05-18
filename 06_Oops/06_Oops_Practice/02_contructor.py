# __init__ constructor (method) and self parameter
# ----------------------------------------------------

# Class
class Car:
    
    # defualt contrcutor
    def __init__(self):
        print("This is default constructor")

    # parameterized contrcutor   
    def __init__(self, car_brand, car_name):
        self.carbramd = car_brand
        self.car_name = car_name
        print("Parameterized constructor")
        print(f"{car_brand}, {car_name}")

# Creating object
tata_car = Car("Tata", "Nexon")



# Abstraction
# ----------------------------------------------------

# Class
class Car:
    
    # parameterized contrcutor   
    def __init__(self, car_brand, car_name):
        self.carbramd = car_brand
        self.car_name = car_name
        print(f"{car_brand}, {car_name}")

    # Example if abstraction how engined started hided just display action.
    def start_engine(self):
        print("Engine started")

# Creating object
tata_car = Car("Tata", "Nexon")
tata_car.start_engine()



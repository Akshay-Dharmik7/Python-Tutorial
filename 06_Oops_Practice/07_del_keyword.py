# del keyword
# ----------------------------------------------------
#used to delete object, method, variables

# Class
class Car:
    
    # parameterized contrcutor   
    def __init__(self, car_brand, car_name):
        self.carbramd = car_brand
        self.car_name = car_name
        print(f"{car_brand}, {car_name}")

    def start_engine(self):
        print("Engine started")

# Creating object
tata_car = Car("Tata", "Nexon")
tata_car.start_engine()

# delete tata_car object
# del tata_car
# print(tata_car)

# delete start_engine() method - we cannot delete method directly it shows error.
del tata_car.start_engine
tata_car.start_engine()


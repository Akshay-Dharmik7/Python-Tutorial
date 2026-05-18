# STATIC METHOD

# Class
class Car:

    # Contrcutor - entry point to initialize instance variables   
    def __init__(self, car_brand, car_name):

        # Instance variable
        self.carbramd = car_brand
        self.car_name = car_name
        print(f"{car_brand}, {car_name}")

    @staticmethod #static method
    def transport_type1():
        print("Private Vehicle using static method")

    # instance method
    def transport_type2(self):
        print("Private Vehicle using instance method")

# Creating object
tata_car = Car("Tata", "Nexon")

# instance method can't access using class name
# Car.transport_type2()
tata_car.transport_type2()

# static method can be access using class and object name
Car.transport_type1()
tata_car.transport_type1()


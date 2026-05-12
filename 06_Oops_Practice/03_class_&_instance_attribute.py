# Class
class Car:
    # class attribute/variable
    transport_type = "Private Vehicle"

    # parameterized contrcutor   
    def __init__(self, car_brand, car_name):

        # Instance variable
        self.carbramd = car_brand
        self.car_name = car_name
        print(f"{car_brand}, {car_name}")

        # Class variable :- access using class name
        print(Car.transport_type)  

# Creating object
tata_car = Car("Tata", "Nexon")


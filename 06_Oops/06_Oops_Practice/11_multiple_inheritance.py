# Single Inheritance
#                  CAR
#                   |
#         -------------------
#        |                   |
#   ELECTRIC_CAR          CNG_CAR
        

class Car:
    def __init__(self, brand1, model1):
        self.brand1 = brand1
        self.model1 = model1

    def full_name(self):
        return f"{self.brand1} {self.model1}"
    
    def fuel_type(self):
        return "Diesel Car"
    
class Bike:
    def __init__(self, brand2, model2):
        self.brand2 = brand2
        self.model2 = model2
    
    def full_name(self):
        return f"{self.brand2} {self.model2}"
    
    def fuel_type(self):
        return "Petrol Bike"
    
class Vehicle(Car, Bike):
    def __init__(self, brand1, model1, brand2, model2):
        super().__init__(brand1, model1)
        super().__init__(brand2, model2)

        print(f"{brand1}, {model1}")
        print(f"{brand2}, {model2}")


vehicle =  Vehicle("Tata", "Nexon", "Honda", "Activa") 

# below will also work same
Vehicle("Tata", "Nexon", "Honda", "Activa") 
# print(vehicle)   



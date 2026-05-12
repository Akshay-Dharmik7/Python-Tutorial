# Single Inheritance
#                  CAR
#                   |
#         -------------------
#        |                   |
#   ELECTRIC_CAR          CNG_CAR
        

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return self.__brand + "!"
    
    def fuel_type(self):
        return "Petrol Car"
    
class Electric_Car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
        print(f"{brand}, {model}, {battery_size}")

class Cng_Car(Car):
    def __init__(self, brand, model, fuel_capacity):
        super().__init__(brand, model)
        self.fuel_capacity = fuel_capacity

        print(f"{brand}, {model}, {fuel_capacity}")

       
my_tesla = Electric_Car("Telsa", "Model S", "85kWh")
my_tata = Cng_Car("Tata", "Punch", "70 ltr")


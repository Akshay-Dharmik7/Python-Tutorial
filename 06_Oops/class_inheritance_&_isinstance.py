# 9. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand + "!"
    
    def fuel_type(self):
        return "Petrol Car"
    
    @property
    def prop_deco_model(self):
        return self.__model

    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("Telsa", "Model S", "85kWh")
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))

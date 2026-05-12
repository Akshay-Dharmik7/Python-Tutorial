# 8. Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.

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
my_safari = Car("Tata", "Safari")
my_safari.model = "Sierra"

# print(my_safari.full_name())
print(my_safari.model)
print(my_safari.prop_deco_model)

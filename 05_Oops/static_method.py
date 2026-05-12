# 7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.

class Car:
    total_cars = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_cars += 1

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return self.__brand + "!"
    
    def fuel_type(self):
        return "Petrol Car"
    
    # access using class name only.
    # def general_description():
    #     return "Cars are medium of trasport"

    # Access using class and object as well.
    @staticmethod
    def general_description():
        return "Cars are medium of trasport"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("Telsa", "Model S", "85kWh")
my_safari = Car("Tata", "Safari")
Car("Maruti Suzuki", "Swift")

print(my_safari.general_description())
print(Car.general_description())
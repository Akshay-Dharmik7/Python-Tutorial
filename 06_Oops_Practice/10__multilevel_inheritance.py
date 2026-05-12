# Single Inheritance
#       CAR
#        |
#        |
#   ELECTRIC_CAR
#        |
#        |
# ELECTRIC_CAR_FEATURES         

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
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"

class Electric_Car_Features(ElectricCar):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model, battery_size)
        # self.brand = brand
        # self.model = model
        # self.battery_size = battery_size
        # print(f"{self.brand}, {self.model}, {self.battery_size}")

        print(f"{brand}, {model}, {battery_size}")
        
my_tesla = Electric_Car_Features("Telsa", "Model S", "85kWh")
my_safari = Car("Tata", "Safari")

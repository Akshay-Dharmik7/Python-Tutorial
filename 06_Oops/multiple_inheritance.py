# 10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Battery:
    def battery_info(self):
        return "This is Battery"

class Engine:
    def engine_info(self):
        return "This is Engine"
    
class ElectricCar(Battery, Engine):
    pass

my_tesla = ElectricCar()

print(my_tesla.battery_info())
print(my_tesla.engine_info())
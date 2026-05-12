# PRIVATE METHOD

class Car:
    
    # private variable/attribute
    __private_var = "this is private variable"

    # parameterized contrcutor   
    def __init__(self, car_brand, car_name):
        self.carbramd = car_brand
        self.car_name = car_name
        print(f"{car_brand}, {car_name}")

    # to access private attribute/variable we need to create getter/setter methods using @property decorator
    # this will allows to access private attribute outside a class.

    # for private methods, we cannot access it directly outside a class, we can create a new getter/setter method and we can call private method inside a getter/setter method.
    # this will allow to access private method outside a class.

    @property
    def get_var(self):
        print(self.__private_var)
        # access inside
        self.__start_engine()

    def get_var1(self):
        # access private method inside getter method
        self.__start_engine()

    def __start_engine(self):
        print("Engine started")



# Creating object
tata_car = Car("Tata", "Nexon")

# we cannot access private attribute or metho outside a class. it shows error
# tata_car.start_engine()
tata_car.get_var
tata_car.get_var1()

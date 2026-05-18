# base class
class Person:
    # def __init__(self, name, id):
    #     self.name = name
    #     self.id = id
    
    def get_details(self, name, id ):
        return f"Name: {name}, ID: {id}"
    
class Employee():
    
    # def __init__(self, name, id, position):
    #     super().__init__(name, id)

        # self.position = position
    
    def get_details(self, name, id, position):
        return f"Name: {name}, ID: {id}, Position: {position}"

person = Person()
print(person.get_details("Akshay", 1001))

employee = Employee()
print(employee.get_details("Rahul", 1002, "Engineer"))
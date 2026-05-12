class Person:

    # def __init__(self, name, id):
    #     self.name = name
    #     self.id = id
    
    # we need to used @classmethod decorator along with cls-as a first parameter of method 

    @classmethod
    def get_details(cls, name, id):
        return f"Name: {name}, ID: {id}"


# person = Person("Akshay", "1001")
print(Person.get_details("Akshay", 1001))
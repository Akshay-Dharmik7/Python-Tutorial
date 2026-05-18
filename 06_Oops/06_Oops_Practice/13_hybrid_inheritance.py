# base class
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"
    
class Employee(Person):
    def __init__(self, name, id, position):
        super().__init__(name, id)

        self.position = position
    
    def get_position(self):
        return f"Position: {self.position}"
    
class Athelete:
    def __init__(self, sport):
        self.sport = sport

    def get_sport(self):
        return f"Sport: {self.sport}"
    
class Student(Employee, Athelete):
    def __init__(self, name, id, position, grade, sport):
        Employee.__init__(self, name, id, position)
        Athelete.__init__(self, sport)
        self.grade = grade

    def get_grade(self):
        return f"Grade: {self.grade}"


student = Student("Akshay", "1001", "Software Engineer", "A+", "Cricket")
print(student.get_details())
print(student.get_position())
print(student.get_sport())
print(student.get_grade())
        
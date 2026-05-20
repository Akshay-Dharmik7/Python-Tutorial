import json

def load_student_data():
    try:
        with open("student.txt", "r") as student_file:
            data = json.load(student_file)
            # print(data)
            return data
    except:
        return {}

def save_student_data(students):
    with open("student.txt", "w") as student_file:
        json.dump(students, student_file)

def view_student(students):
    print("\n")
    print("-" * 70)
    for  student, marks in students.items():
        print(f"1. Student Name: {student}, Marks: {marks}")
    print("\n")
    print("-" * 70)

def add_student(students):
    name = input("enter the Student Name: ")
    marks = int(input("enter the Student Marks: "))

    students[name] = marks
    save_student_data(students)
    print(f"{name} Successfully Added!!")

def update_student(students):
    name = input("Enter the student name: ")
    try:
        if name != '':
            choice1 = input("Do you want to update student name: ")
            if choice1.upper()  == 'Y':
                marks = students[name] 
                students.pop(name)
                new_name = input("Enter the new name: ")
                students[new_name] = marks

            choice2 = input("Do you want to update student marks: ")
            if choice2.upper()  == 'Y':
                new_marks = input("Enter the new marks: ")
                for stuname, marks in students.items():
                    if choice1.upper() == 'Y':
                        if stuname == new_name:
                            students[stuname] = new_marks
                    else:
                        if stuname == name:
                            students[stuname] = new_marks

            save_student_data(students)
    except:
        print(f"{name} is not present in Database")
        print("Student data updated!!")
    

def delete_student(students):
    choice = input("Do you want to delete student: ")
    try:
        if choice.upper() == "Y":
            name = input("Enter name of student: ")
            students.pop(name)
            save_student_data(students)
            print("Student deleted successfully!!")
    except:
        print("Invalid input!!")

def show_result(students):
    try:
        name = input("enter the student name: ")

        print(students[name])
        if int(students[name]) > 40:
            print("Student have marks above 40.. PASS")
        else:
            print("Student have marks below 40.. FAIL")
    except:
        print("Invalid Input!!")

def main():
    while True:
        students = load_student_data()
        # print("student data", student)

        print("\n -------- STUDENT MANAGER APP --------")
        print('1. View Student')
        print('2. Add Student')
        print('3. Update Student')
        print('4. Delete Student')
        print('5. Show Result')
        print('6. Exit App')

        choice = input("Enter the choice: ")

        match choice:
            case '1':
                view_student(students)
            case '2':
                add_student(students)
            case '3':
                update_student(students)
            case '4':
                delete_student(students)
            case '5':
                show_result(students)
            case '6':
                print("Exiting App")
                break
            case _:
                print('Invalid Input')

if __name__ == '__main__':
    main()
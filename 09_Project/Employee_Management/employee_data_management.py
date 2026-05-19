import json

def load_employees():
    try:
        with open('employee_data.txt', 'r') as employee_data:
            data = json.load(employee_data)
            return data
    except FileNotFoundError:
        return []

def save_employee_data(employees):
    with open('employee_data.txt', 'w') as employee_data:
        json.dump(employees, employee_data)

def list_all_employees(employees):
    print('\n')
    print("*" * 70)
    for index, data in enumerate(employees, start=1):
        print(f"{index}. 'name: {data['name']}, 'role: ' {data['role']}, 'location:' {data['location']}")

    print('\n')
    print("*" * 70)

def add_employee(employees):
    name = input('Enter employee name: ')
    role = input('Enter employee role: ')
    location = input('Enter employee location: ')
    employees.append({'name' : name, 'role' : role, 'location' : location })
    save_employee_data(employees)
    print('Employeee Data added Successfully!!!')

def update_employee(employees):
    list_all_employees(employees)
    index = int(input('Enter the number of employee to update: '))

    if 1<= index <= len(employees):
        name = input('Enter employee name to update: ')
        role = input('Enter employee role to update: ')
        location = input('Enter employee location to update: ')
        employees[index-1] = {'name' : name, 'role' : role, 'location' : location}
        save_employee_data(employees)
        print('Employeee Data updated Successfully!!')
    else:
        print('Invalid Index selected')
    
def delete_employees(employees):
    list_all_employees(employees)
    index = int(input('Enter the number of employee to update: '))

    if 1<= index <= len(employees):
        del employees[index - 1]
        save_employee_data(employees)
        print('Employeee Data deleted Successfully!!')
    else:
        print('Invalid Index selected')

def main():
    employees = load_employees()
    while True:
        print('!!  Employee Management System  !!')
        print('1. List all Employee')
        print('2. Add new Employee')
        print('3. Update Employee')
        print('4. Delete Employee')
        print('5. Exit App')

        choice = input('Enter the choice to continue: ')
        match choice:
            case '1':
                list_all_employees(employees)
            case '2':
                add_employee(employees)
            case '3':
                update_employee(employees)
            case '4':
                delete_employees(employees)
            case '5':
                break
            case _:
                print('Invalid option')

    
if __name__ == '__main__':
    main()
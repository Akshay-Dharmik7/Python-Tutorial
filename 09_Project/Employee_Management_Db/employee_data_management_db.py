import sqlite3

conn = sqlite3.connect('employee_data.db')

cursor = conn.execute('''
    CREATE TABLE IF NOT EXISTS employee (
                      id INTEGER PRIMARY KEY,
                      name TEXT NOT NULL,
                      role TEXT NOT NULL,
                      location TEXT NOT NULL
    )
''')

def list_employees():
    cursor.execute("SELECT * FROM employee")

    for row in cursor.fetchall():
        print(row)

def add_employee(new_name, new_role, new_location):
    cursor.execute('INSERT INTO employee (name, role, location) VALUES (?, ?, ?)', (new_name, new_role, new_location))
    conn.commit()

def update_employee(employee_id, new_name, new_role, new_location):
    cursor.execute('UPDATE employee SET name = ?, role = ?, location = ? WHERE id = ?', (new_name, new_role, new_location, employee_id))
    conn.commit()

def delete_employee(employee_id):
    cursor.execute('DELETE FROM employee WHERE id = ?', (employee_id, ))
    conn.commit()

def main():
    while True:
        print('!!  Employee Management System  !!')
        print('1. List all Employee')
        print('2. Add new Employee')
        print('3. Update Employee')
        print('4. Delete Employee')
        print('5. Exit App')
    
        choice = input('Enter the choice to continue: ')

        if choice == '1':
            list_employees()
        elif choice == '2':
            name = input('Enter employee name: ')
            role = input('Enter employee role: ')
            location = input('Enter employee location: ')

            add_employee(name, role, location)
        elif choice == '3':
            list_employees()
            employee_id = int(input('Enter employee ID to update: '))
            name = input('Enter employee name: ')
            role = input('Enter employee role: ')
            location = input('Enter employee location: ')
            update_employee(employee_id, name, role, location)
        elif choice == '4':
            list_employees()
            employee_id = int(input('Enter employee ID to delete: '))
            delete_employee(employee_id)
        elif choice == '5':
            break
        else:
            print('Invalid Selection!!')

if __name__ == '__main__':
    main()
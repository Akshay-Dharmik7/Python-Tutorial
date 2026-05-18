# 6. Database Connection Simulator (Resource Cleanup)
# Task: Write a function that "opens a database connection" (print a message), attempts to perform a risky data operation, and then "closes the connection".  
# Keyword to use: finally.  
# Goal: Ensure that the "database connection closed" message prints no matter what—even if the risky operation throws an error.

def database_operation():
    try:
        file = open('08_Exception_Handling/08_file.txt', 'r')
        filedata = file.read()

    except FileNotFoundError as e:
        print(f'{e} error occured!!')

    finally:
        print('database connection closed')

database_operation()
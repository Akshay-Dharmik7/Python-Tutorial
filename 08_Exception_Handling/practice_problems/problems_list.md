# 🔹 Beginner Level: The Fundamentals
##  1. The Classic Zero Division Shield
Task: Write a program that asks the user for two numbers and divides the first by the second.  
Exception to handle: ZeroDivisionError and ValueError (in case they type words instead of numbers).  
Goal: Prevent the program from crashing if a user enters 0 or "hello".

## 2. File Reader Safeguard
Task: Prompt the user for a filename, attempt to open it, and print its contents.  
Exception to handle: FileNotFoundError.  
Goal: If the file doesn't exist, catch the error gracefully and print a helpful message instead of a stack trace.

## 3. List Index Validator
Task: Create a fixed list of 5 elements. Ask the user to input an index number to retrieve an item.  
Exception to handle: IndexError and ValueError.  
Goal: Handle cases where the user asks for index 10 or types a non-integer.

## 4. Safe Type Converter
Task: Write a function safe_int_convert(lst) that takes a list of mixed data types (strings, floats, booleans) and returns a new list containing only the successfully converted integers.  
Exception to handle: TypeError and ValueError.

# 🔸 Intermediate Level: Control Flow & Multiple Blocks
## 5. The Clean Exit (Input Loop)
Task: Create a program that continuously asks the user for numbers to add to a total. The loop should only end when the user types "exit".  
Keywords to use: try, except, and else.  
Goal: Use the else block to add the number to the total only if no exception occurred during conversion.

## 6. Database Connection Simulator (Resource Cleanup)
Task: Write a function that "opens a database connection" (print a message), attempts to perform a risky data operation, and then "closes the connection".  
Keyword to use: finally.  
Goal: Ensure that the "database connection closed" message prints no matter what—even if the risky operation throws an error.

## 7. Dictionary Key Fetcher with Default
Task: Write a program that looks up a user-provided key in a configuration dictionary.  
Exception to handle: KeyError.  
Goal: If the key doesn't exist, catch the error, assign a default value, and notify the user.

## 8. Age Validator (Raising Exceptions)
Task: Write a function register_voter(age) that takes an integer.    
Keyword to use: raise.  
Goal: If the age is less than 18, manually raise a ValueError with a custom message: "Must be 18 or older to register."

# 🚀 Advanced Level: Custom Errors & Enterprise Logic
## 9. Custom Bank Withdrawal System
Task: Create a user-defined exception class called InsufficientFundsError. Write a BankAccount class with a withdraw method.  
Goal: Raise your custom InsufficientFundsError if a withdrawal amount exceeds the current balance. Catch it in your main code block.

# 10. The Password Length Validator
Task: Write a loop that keeps asking a user to create a password.  
Goal: If the password is shorter than 6 characters, raise a custom message. If it's long enough, use the else block to break out of the loop and say "Password secured!"
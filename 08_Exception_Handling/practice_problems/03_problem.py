# 3. List Index Validator
# Task: Create a fixed list of 5 elements. Ask the user to input an index number to retrieve an item.  
# Exception to handle: IndexError and ValueError.  
# Goal: Handle cases where the user asks for index 10 or types a non-integer.

list1 = [2, 5, 3, 8, 7]

try:
    user_input_index = int(input("Enter the index: "))

    print(list1[user_input_index])

except IndexError as idx_error:
    print(f'{idx_error} error occured!!')

except ValueError as val_error:
    print(f'{val_error} error occured!!')
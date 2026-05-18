# 5. The Clean Exit (Input Loop)
# Task: Create a program that continuously asks the user for numbers to add to a total. The loop should only end when the user types "exit".  
# Keywords to use: try, except, and else.  
# Goal: Use the else block to add the number to the total only if no exception occurred during conversion.

total = 0

while True:

    try:
        num = input("Enter the number: ")

        if num == 'exit':
            break
        
        converted_num = int(num)

    except (TypeError, ValueError) as e:
        print(f'{e} error occured!!')
    
    else:
        total += converted_num
    

print('total is', total)
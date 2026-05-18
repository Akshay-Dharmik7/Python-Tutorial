#  1. The Classic Zero Division Shield
# Task: Write a program that asks the user for two numbers and divides the first by the second.  
# Exception to handle: ZeroDivisionError and ValueError (in case they type words instead of numbers).  
# Goal: Prevent the program from crashing if a user enters 0 or "hello".

try:
    num1 = int(input('Enter Numerator: '))
    num2 = int(input('Enter Denominator: '))

    res = num1/num2
    print('result is: ', res)

except (ZeroDivisionError, ValueError) as e:
    print(f'{e} error occured!!')

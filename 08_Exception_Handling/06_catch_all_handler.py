try:
    num1 = int(input('Enter Numerator: '))
    num2 = int(input('Enter Denominator: '))

    res = num1/num2

except ArithmeticError as ar:
    print(f'{ar} error occured!!')

except:
    print('Something went wrong!!')
def divide(num1, num2):
    res = num1/num2

    # raise ArithmeticError('cannot dived by zero')
    raise ArithmeticError

    print('result is', res)

try:
    num1 = int(input('Enter Numerator: '))
    num2 = int(input('Enter Denominator: '))

    divide(num1, num2)

except ArithmeticError as e:
    print(f'{e} error occured!!')


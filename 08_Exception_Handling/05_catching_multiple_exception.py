try:
    num1 = int(input('Enter Numerator: '))
    num2 = int(input('Enter Denominator: '))

    res = num1/num2

except (ZeroDivisionError, ValueError) as e:
    print(f'{e} error occured!!')

else:
    print('executed normally!!')

finally:
    print('always runs!!')
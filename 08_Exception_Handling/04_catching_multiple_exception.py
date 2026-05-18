try:
    num1 = int(input('Enter Numerator: '))
    num2 = int(input('Enter Denominator: '))

    res = num1/num2
    
except ZeroDivisionError as Ar:
    print(f'{Ar} error occured!!')

except  ValueError as vl:
    print(f'{vl} error occured!!')

else:
    print(f'Result is {res}')

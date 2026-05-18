# 4. Safe Type Converter
# Task: Write a function safe_int_convert(lst) that takes a list of mixed data types (strings, floats, booleans) and returns a new list containing only the successfully converted integers.  
# Exception to handle: TypeError and ValueError.

def safe_int_convert(lst):

    lst2 = []

    for val in lst:
        try:
            lst2.append(int(val))
        
        except (TypeError, ValueError) as err:
            print(err)
    
    return lst2;

lst3 = safe_int_convert([1.22, '3', 'akshay', True, '4', False, '3.44', '7'])

print(lst3)
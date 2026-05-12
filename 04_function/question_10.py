# 10. Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number.


def find_fact(num):
    
    if num == 0:
        return 1
    else:
        return num * find_fact(num-1)
    
print(find_fact(5))

# Genarate number  between 1 to 100 and test it is even or not.

import random

x = random.randint(1,100)
print(x)

if (x % 2) == 0:
    print("Even Number")
else:
    print("Odd Number")
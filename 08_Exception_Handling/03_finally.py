n = 10

try:
    res = n /0

except Exception as e:
    print(e)

else:
    print('executed successfully!!')

finally:
    print('regards to exception it will always execute!!')


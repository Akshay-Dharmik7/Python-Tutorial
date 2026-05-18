# 7. Dictionary Key Fetcher with Default
# Task: Write a program that looks up a user-provided key in a configuration dictionary.  
# Exception to handle: KeyError.  
# Goal: If the key doesn't exist, catch the error, assign a default value, and notify the user.

dict_data = {'id' : 101, "name" : 'akshay', 'role' : 'software engineer', 'sal' : 30000}

try:
    userkey = input('Enter key name: ')

    print(dict_data[userkey])
    
except KeyError as e:
    print(f'{e} error occured!!')
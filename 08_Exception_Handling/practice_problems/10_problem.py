# 10. The Password Length Validator
# Task: Write a loop that keeps asking a user to create a password.  
# Goal: If the password is shorter than 6 characters, raise a custom message. If it's long enough, use the else block to break out of the loop and say "Password secured!"

class IncorrectPasswordError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"{self.message}"

while True:
    try: 
        password = input("Create a password: ")

        if len(password) < 6 :
            raise IncorrectPasswordError('Invalid password, check for password validations.')
    
    except IncorrectPasswordError as e:
        print(e)
    
    else:
        print('Password Secured!!')
        break
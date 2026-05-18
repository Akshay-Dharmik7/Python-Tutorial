# 9. Custom Bank Withdrawal System
# Task: Create a user-defined exception class called InsufficientFundsError. Write a BankAccount class with a withdraw method.  
# Goal: Raise your custom InsufficientFundsError if a withdrawal amount exceeds the current balance. Catch it in your main code block.

class InsufficientFundsError(Exception):
    def __init__(self, message, error_code):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code: {self.error_code})"
    
class BankAccount:
    # def __init(self, withdraw_ammount, total_ammount):
    #     self.withdraw_ammount = withdraw_ammount
    #     self.total_ammount = total_ammount
    
    def withdraw(self, withdraw_ammount, total_ammount):
        if withdraw_ammount > total_ammount:
            raise InsufficientFundsError('Insufficient Fund to withdraw!!', 202)

try:
    total_ammount = 40000
    withdraw_ammount = int(input('Enter withdraw ammount: '))

    bankaccount = BankAccount()
    bankaccount.withdraw(withdraw_ammount, total_ammount)

except InsufficientFundsError as e:
    print(e)
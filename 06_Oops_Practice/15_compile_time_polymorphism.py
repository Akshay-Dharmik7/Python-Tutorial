class Calculator:


    def addition(self, arg1, arg2, *args ):
        result = arg1 + arg2

        for i in args:
            result += i

        return f"Addition: {result}"


calculator = Calculator()
print(calculator.addition(2, 3, 4, 5))
print(calculator.addition(2, 3, 4, 5, 10, 23))
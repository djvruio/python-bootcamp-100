from art import logo

def addition(a, b):
    """Add two number a + b."""
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error. No Zero division."
    return a / b 

def calculator(a, b, operator):
    operators = ['+','-', '*', '/']
    if operator not in operators:
        return "Error. That operator doesn't exists."
    elif operator == '+':
        return addition(a, b)
    elif operator == '-':
        return subtraction(a, b)
    elif operator == '*':
        return multiplication(a, b)
    else:
        return division(a, b)


print(logo)
first_number = float(input("What's the first number?: "))
operation_choose = input("+\n-\n*\n/\nPick an operation: ")
next_number = float(input("What's the next number?: "))


result = calculator(first_number, next_number, operation_choose)
print(f"{first_number} {operation_choose} {next_number} = {result}")
from art import logo
import os

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

def fraction(a, b):
    if b == 0:
        return "Error. No Zero division."
    return f"{a}/{b}" 

operations = {
        '+': addition,
        '-': subtraction, 
        '*': multiplication, 
        '/': division,
        'fraction': fraction, 
}



def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        user_response = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if user_response == 'y':
            num1 = answer
        else:
            should_continue = False
            os.system('cls')
            calculator()

calculator()
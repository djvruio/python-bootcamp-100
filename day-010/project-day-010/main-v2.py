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

operations = {
        '+': addition,
        '-': subtraction, 
        '*': multiplication, 
        '/': division,
}

print(logo)
first_number = float(input("What's the first number?: "))
second_number = float(input("What's the next number?: "))
for symbol in operations:
    print(symbol)
operation_picked = input("Pick an operation from the line above: ")
calculation_function = operations[operation_picked]
first_answer = calculation_function(first_number, second_number)

print(f"{first_number} {operation_picked} {second_number} = {first_answer}")

operation_picked = input("Pick another operation: ")
third_number = float(input("What's the next number?: "))
calculation_function = operations[operation_picked]
second_answer = calculation_function(first_answer, third_number)

print(f"{first_answer} {operation_picked} {third_number} = {second_answer}")
from art import logo
import os

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide

}


def calculator():
    print(logo)

    num1 = int(input("What's is the first number? "))

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's is the sconde number? "))
        calculating_function = operations[operation_symbol]
        answer = calculating_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")



        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            os.system('clear')
            calculator()


calculator()
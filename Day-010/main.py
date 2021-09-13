from art import logo
import os


def clear():
    return os.system('cls')


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


math = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    continue_calc = True
    num1 = float(input("What's the first number?: "))
    while continue_calc:

        for key in math:
            print(key)

        math_symbol = input("Pick an operation: ")
        num2 = float(input("What's the second number?: "))
        func = math[math_symbol]
        answer = func(num1, num2)
        print(f"{num1} {math_symbol} {num2} = {answer}")
        asking_user_to_continue_calculating = input(
            f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation: ")
        
        if asking_user_to_continue_calculating == "y":
            num1 = answer
        else:
            continue_calc = False
            clear()
            calculator()


calculator()

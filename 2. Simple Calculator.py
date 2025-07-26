# Simple Calculator 🧮
# Create a basic command-line calculator that can perform addition, subtraction, multiplication, and division.
# •	Description: The program asks the user for two numbers and an operator (+, -, *, /).
#       It then performs the calculation and prints the result.
# •	Concepts Covered: Functions, if/elif/else statements, user input, and basic arithmetic operators.
# •	Next Step: Improve it by adding more operations like exponents (**) or modulus (%).
#       You can also wrap the main logic in a
#       loop so the user can perform multiple calculations without restarting the script.

def calculator():
    num1=int(input("Enter a First Number: "))
    num2=int(input("Enter a Second Number: "))
    op=input("Enter Addition(+), Subtration(-), Multiplication(/), Division(/): ")
    if op == "+":
        print(f"The addition of {num1} and {num2} is {num1+num2}")
    elif op == "-":
        print(f"The subtration of {num1} and {num2} is {num1-num2}")
    elif op == "*":
        print(f"The multiplication of {num1} and {num2} is {num1*num2}")
    elif op == "/":
        print(f"The division of {num1} and {num2} is {num1/num2}")
    else:
        print("Invalid Input")

print(calculator())

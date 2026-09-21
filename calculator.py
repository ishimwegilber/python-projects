"""
Professional Calculator Application

Author: Ishimwe Gilbert
Project: Python Calculator
Description:
A simple command-line calculator demonstrating
functions, user input, loops, and error handling.
"""


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract two numbers."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide two numbers with error handling."""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def display_menu():
    print("\n========== PYTHON CALCULATOR ==========")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("=======================================")


def calculator():
    while True:
        display_menu()

        choice = input("Choose an operation (1-5): ")

        if choice == "5":
            print("Thank you for using Python Calculator!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please select between 1 and 5.")
            continue

        try:
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(number1, number2)

            elif choice == "2":
                result = subtract(number1, number2)

            elif choice == "3":
                result = multiply(number1, number2)

            elif choice == "4":
                result = divide(number1, number2)

            print("Result:", result)

        except ValueError:
            print("Error: Please enter valid numbers.")


# Start application
calculator()

# ============================================================
# SAM AI Technologies - Python Programming Internship
# Task 1: Calculator
# Intern: Mudassar Abbas
# Date: June 2026
# ============================================================

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the division of two numbers. Handles division by zero."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def modulus(a, b):
    """Return the remainder when a is divided by b."""
    if b == 0:
        return "Error: Modulus by zero is not allowed."
    return a % b

def power(a, b):
    """Return a raised to the power of b."""
    return a ** b

def display_menu():
    """Display the calculator menu."""
    print("\n" + "=" * 45)
    print("       SAM AI Technologies Calculator")
    print("=" * 45)
    print("  Select an Operation:")
    print("  1. Addition       (+)")
    print("  2. Subtraction    (-)")
    print("  3. Multiplication (*)")
    print("  4. Division       (/)")
    print("  5. Modulus        (%)")
    print("  6. Power          (^)")
    print("  7. Exit")
    print("=" * 45)

def get_number(prompt):
    """Prompt the user for a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ⚠  Invalid input! Please enter a numeric value.")

def calculator():
    """Main calculator function with loop for continuous operations."""
    print("\n  Welcome to the SAM AI Technologies Calculator!")
    print("  Intern: Mudassar Abbas | Python Programming Internship")

    operations = {
        "1": (add,      "Addition",       "+"),
        "2": (subtract, "Subtraction",    "-"),
        "3": (multiply, "Multiplication", "*"),
        "4": (divide,   "Division",       "/"),
        "5": (modulus,  "Modulus",        "%"),
        "6": (power,    "Power",          "^"),
    }

    while True:
        display_menu()
        choice = input("  Enter your choice (1-7): ").strip()

        if choice == "7":
            print("\n  Thank you for using SAM AI Calculator!")
            print("  Goodbye! 👋\n")
            break

        if choice not in operations:
            print("  ⚠  Invalid choice. Please select between 1 and 7.")
            continue

        func, op_name, symbol = operations[choice]

        print(f"\n  --- {op_name} ---")
        num1 = get_number("  Enter first number  : ")
        num2 = get_number("  Enter second number : ")

        result = func(num1, num2)

        if isinstance(result, str):
            print(f"\n  ❌ {result}")
        else:
            # Display as int if result is whole number
            display_result = int(result) if isinstance(result, float) and result.is_integer() else result
            print(f"\n  ✅ Result: {num1} {symbol} {num2} = {display_result}")

        again = input("\n  Perform another calculation? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\n  Thank you for using SAM AI Calculator!")
            print("  Goodbye! 👋\n")
            break

if __name__ == "__main__":
    calculator()

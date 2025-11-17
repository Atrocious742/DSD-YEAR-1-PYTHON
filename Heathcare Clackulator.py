# Supports: Addition, Subtraction, Multiplication, Division, Exponentiation

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    # Handle division by zero
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def exponentiate(x, y):
    return x ** y

# Display menu and run calculator indefinitely
while True:
    print("\n--- Simple Calculator ---")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Modulus (%)")
    print("6. Exit")

    choice = input("Enter choice (1-6): ")

    if choice == '6':
        print("Thank you for using the calculator. Goodbye!")
        break

    if choice in ['1', '2', '3', '4', '5']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")
        elif choice == '5':
            result = exponentiate(num1, num2)
            print(f"Result: {num1} % {num2} = {result}")
    else:
        print("Invalid choice. Please select a valid option (1-6).")
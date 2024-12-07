def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculator():
    print("Simple Calculator")

    # Get user input for numbers and operation
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")

    # Perform the selected operation
    if choice == '1':
        print(f"The result of {num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"The result of {num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result of {num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"The result of {num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    calculator()

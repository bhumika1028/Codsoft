def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference of x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the quotient of x and y. Handle division by zero."""
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    print("Simple Calculator")
    
    try:
        # Prompt the user to enter two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Prompt the user to choose an operation
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    # Perform the calculation based on the user’s choice
    if choice == '1':
        result = add(num1, num2)
        operation = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        operation = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        operation = '*'
    elif choice == '4':
        result = divide(num1, num2)
        operation = '/'
    else:
        print("Invalid choice. Please select a valid operation.")
        return
    
    # Display the result of the calculation
    print(f"\nResult: {num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()

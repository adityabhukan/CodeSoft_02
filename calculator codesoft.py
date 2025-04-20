def simple_calculator():
    print("Simple Calculator")
    print("-----------------")
    print("Operations available:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    
    while True:
        try:
            # Get user input
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ").strip()
            
            if operation.lower() == 'exit':
                print("Exiting calculator...")
                break
                
            # Perform calculation based on operation
            if operation == '+':
                result = num1 + num2
                print(f"\nResult: {num1} + {num2} = {result}")
            elif operation == '-':
                result = num1 - num2
                print(f"\nResult: {num1} - {num2} = {result}")
            elif operation == '*':
                result = num1 * num2
                print(f"\nResult: {num1} * {num2} = {result}")
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed!")
                else:
                    result = num1 / num2
                    print(f"\nResult: {num1} / {num2} = {result}")
            else:
                print("Invalid operation! Please use +, -, *, or /")
                
        except ValueError:
            print("Invalid input! Please enter numeric values.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Run the calculator
if __name__ == "__main__":
    simple_calculator()

def calculator():
    try:
        num1 = float(input("Enter first Number:"))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second Number:"))

        if op =='+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ValueError("Cannot divide by zero.")
            result = num1 / num2
        else:
            print("Invalid operator. Please use +, -, *, or /.")

        print(f"The result is: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values for numbers and a valid operator.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
while True:
    calculator()
    again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if again != 'yes':
        break

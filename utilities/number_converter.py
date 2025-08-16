def binary_to_decimal():
    binary = input("Enter a binary number: ")
    try:
        decimal = int(binary, 2)
        print(f"The decimal equivalent of binary {binary} is: {decimal}")
    except ValueError:
        print("Invalid binary number. Please enter a valid binary number consisting of 0s and 1s.")

def decimal_to_binary():
    try:
        decimal = int(input("Enter a decimal number:"))
        print(f"The binary equivalent of decimal {decimal} is: {bin(decimal)[2:]}")
    except ValueError:
        print("Invalid input. Please enter a valid decimal number.")

def decimal_to_hexadecimal():
    try:
        decimal = int(input("Enter a decimal number:"))
        print(f"The hexadecimal equivalent of decimal {decimal} is: {hex(decimal)[2:]}")
    except ValueError:
        print("Invalid input. Please enter a valid decimal number.")

def hexadecimal_to_decimal():
    hexadecimal = input("Enter a hexadecimal number: ")
    try:
        decimal = int(hexadecimal, 16) 
        print(f"The decimal equivalent of hexadecimal {hexadecimal} is: {decimal}")
    except ValueError:
        print("Invalid hexadecimal number. Please enter a valid hexadecimal number consisting of digits and letters A-F.")

while True:
    print("Choose a conversion:")
    print("1. Binary to Decimal")
    print("2. Decimal to Binary")
    print("3. Decimal to Hexadecimal")
    print("4. Hexadecimal to Decimal")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        binary_to_decimal()
    elif choice == '2':
        decimal_to_binary()
    elif choice == '3':
        decimal_to_hexadecimal()
    elif choice == '4':
        hexadecimal_to_decimal()
    elif choice == '5':
        print("Exiting the converter.")
        break
    else:
        print("Invalid choice. Please select a valid option (1-5).")
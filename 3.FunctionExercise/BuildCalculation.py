def calculator():
    print("Simple Calculator")
    print("Choose operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    choice = input("Enter choice (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice.")
        return  # Exit the function early

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    if choice == '1':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")

    elif choice == '2':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")

    elif choice == '3':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")

    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")

calculator()



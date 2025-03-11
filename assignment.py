#1.calculator menu driven with match
def calculator():
    while True:
        print("\nMenu-Driven Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = int(input("Enter your choice (1-5): "))

        if choice == 5:
            print("Exiting")
            break

        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        match choice:
            case 1:
                print(f"Result: {a} + {b} = {a + b}")
            case 2:
                print(f"Result: {a} - {b} = {a - b}")
            case 3:
                print(f"Result: {a} * {b} = {a * b}")
            case 4:
                print(f"Result: {a} / {b} = {a / b if b != 0 else 'Undefined'}")
            case _:
                print("Invalid choice! Please enter a number between 1 and 5.")

calculator()

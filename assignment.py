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

#2.N dimentional array  and perform addition subtration and multiplication
arr1 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
arr2 = np.array([[[9, 10], [11, 12]], [[13, 14], [15, 16]]])

print("Array 1:\n", arr1)
print("Array 2:\n", arr2)

# Addition
addition_result = arr1 + arr2
print("\nAddition:\n", addition_result)

# Subtraction
subtraction_result = arr1 - arr2
print("\nSubtraction:\n", subtraction_result)

#  Multiplication(Element-wise)
multiplication_result = np.multiply(arr1, arr2)
print("\nElement-wise Multiplication:\n", multiplication_result)

#  Multiplication(Matrix)
dot_product = np.matmul(arr1, arr2)
print("\nMatrix Multiplication:\n", dot_product)



def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"


print("Select the operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Quit")

while True:
    operation = input("Enter your choice (1/2/3/4/5): ")

    if operation in ('1', '2', '3', '4'):
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
        except ValueError:
            print("Please enter a valid number")
            continue

        if operation == '1':
            print("Addition of a and b is:", addition(a, b))
        elif operation == '2':
            print("Subtraction of a and b is:", subtraction(a, b))
        elif operation == '3':
            print("Multiplication of a and b is:", multiplication(a, b))
        elif operation == '4':
            result = division(a, b)
            print("Division of a and b is:", result)
    elif operation == '5':
        print("Operations over")
        break
    else:
        print("Invalid choice. Please enter a valid option.")

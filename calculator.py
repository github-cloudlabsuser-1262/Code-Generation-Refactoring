def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def main():
    print("Basic Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == '7':
        return

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result: ", add(num1, num2))
    elif choice == '2':
        print("Result: ", subtract(num1, num2))
    elif choice == '3':
        print("Result: ", multiply(num1, num2))
    elif choice == '4':
        print("Result: ", divide(num1, num2))
    elif choice == '5':
        print("Result: ", power(num1, num2))
    elif choice == '6':
        print("Result: ", modulus(num1, num2))
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()

    
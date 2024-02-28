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

# Dictionary mapping operation symbols to functions
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            operation_symbol = input("Enter operation symbol (+, -, *, /): ")

            if operation_symbol in operations:
                result = operations[operation_symbol](num1, num2)
                print("Result:", result)
            else:
                print("Invalid operation symbol!")
            
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    calculator()

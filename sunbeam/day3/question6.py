def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Division by zero not allowed"
    return a / b

def calculate(operand1, operand2, function):
    return function(operand1, operand2)

# User input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("Result:", calculate(a, b, addition))
elif choice == 2:
    print("Result:", calculate(a, b, subtraction))
elif choice == 3:
    print("Result:", calculate(a, b, multiplication))
elif choice == 4:
    print("Result:", calculate(a, b, division))
else:
    print("Invalid choice")




num1 = float(input("enter a number"))

opertion = input("enter the opertion you want to perform + - * / % :")
num2 = float(input("enter a numaber"))
if opertion == '+':
     print("addition:",num1 + num2)
elif opertion == '-':
    print("subtraction:",num1 - num2)
elif opertion == '*':
    print("multipication:",num1 * num2)
elif opertion == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print("division:",num1 / num2)      
elif opertion == '%':
    print("modulus:",num1 % num2)   
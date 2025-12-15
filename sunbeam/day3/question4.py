def addition(a,b):
    sum = a + b
    return sum

def substraction(a,b):
    sub = a - b
    return sub

def multiplication(a,b):
    mul = a* b
    return mul

def division(a,b):
    if b == 0 :
     print("Divisor zero not allowed")
    else:
      div = a / b
      return div
 
print("menu for calculator")

print("1.Addition")
print("2.Substraction")
print("3.Multipliaction")
print("4.Division")


n1 = int(input("Enter your first number: \n"))
n2 = int(input("Enter your second  number: \n"))

choice = int(input("Enter your choice: \n"))

match choice:
    case 1:
      print("the addition of 2 number is ",addition(n1,n2))
    case 2:
       print("the Substraction of 2 number is ",substraction(n1,n2))
    case 3:
       print("the Multiplication of 2 number is ", multiplication(n1,n2))
    case 4:
        print("the Division  of 2 number is ",division(n1,n2))
    case _:
         print("Invalid Choice")

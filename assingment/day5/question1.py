import math
import numbers
def calculate_area_of_cirlce():
    number = float(input("Enter the radius of the circle:"))
    print("area of cirlce is:",calculate_area_of_cirlce.pi*number ** 2)
calculate_area_of_cirlce.pi = math.pi

calculate_area_of_cirlce()
def calculate_square_of_number():
    number1 = float(input("enter a numbber to find its squre:"))
    print("squre of number is:", number1**2)
calculate_square_of_number()




# Ask the user for a number
number2 = int(input("Enter a number to find its factorial: "))

# Calculate and print the factorial
print("The factorial of", number2, "is", math.factorial(number2))

import os
print("Current directory:", os.getcwd())

if not os.path.exists("cidac"):
    os.mkdir("cidac")
    print("Directory created")
else:
    print("Directory already exists")


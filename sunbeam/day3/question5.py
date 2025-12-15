def greet(name, message="Good Morning"):
    print(message, name)
print("---- Default Parameter Demo ----")
greet("Sushant")                
greet("Sushant", "Good Evening") 
def student_info(name, age, course):
    print("\nStudent Details")
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)
print("\n---- Keyword Argument Demo ----")
student_info(age=21, course="Python", name="jayant")
def add(a, b):
    return a + b
def multiply(a, b):
    return a * b
def operate(func, x, y):
    result = func(x, y)
    return result
print("\n---- Function as Argument Demo ----")
print("Addition:", operate(add, 10, 20))
print("Multiplication:", operate(multiply, 10, 20))
def power(num, exponent=2):
    return num ** exponent
def calculate(func, value):
    return func(value)
print("\n---- Combined Example ----")
print("Square:", calculate(power, 5))
print("Cube:", calculate(lambda x: x ** 3, 4))
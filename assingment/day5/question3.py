import geomery  # assuming you have geometry.py with functions defined

print("1. Area of Circle")
print("2. Area of Rectangle")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    radius = float(input("Enter the radius: "))
    print("Area of circle is:", geomery.area_of_circle(radius))

elif choice == 2:
    length = float(input("Enter the length of rectangle: "))
    breadth = float(input("Enter the breadth of rectangle: "))
    print("Area of rectangle is:", geomery.area_of_rectangle(length, breadth))

else:
    print("Invalid choice!")






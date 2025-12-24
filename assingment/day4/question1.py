# Conversion functions
def km_to_m(km):
    return km * 1000

def m_to_cm(m):
    return m * 100

def cm_to_mm(cm):
    return cm * 10

def feet_to_inches(ft):
    return ft * 12

def inches_to_cm(inch):
    return inch * 2.54

# Generic converter function
def distance_converter(distance, conversion_type, conversion_func):
    result = conversion_func(distance)
    print(f"{conversion_type}: {result}")

# Take input from user
value = float(input("Enter a distance value: "))

print("\nConverted Values:")

# Call all conversions
distance_converter(value, "Kilometers to Meters (km → m)", km_to_m)
distance_converter(value, "Meters to Centimeters (m → cm)", m_to_cm)
distance_converter(value, "Centimeters to Millimeters (cm → mm)", cm_to_mm)
distance_converter(value, "Feet to Inches (ft → in)", feet_to_inches)
distance_converter(value, "Inches to Centimeters (in → cm)", inches_to_cm)
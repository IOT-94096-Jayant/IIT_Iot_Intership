converters = [
    lambda t: t * 1000,                 
    lambda kg: kg * 1000,               
    lambda g: g * 1000,                 
    lambda mg: mg / 453592.37            
]
tons = float(input("Enter weight in tons: "))
kg = converters[0](tons)
g = converters[1](kg)
mg = converters[2](g)
lbs = converters[3](mg)
print("Kilograms:", kg)
print("Grams:", g)
print("Milligrams:", mg)
print("Pounds:", lbs)
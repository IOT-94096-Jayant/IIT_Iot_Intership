# Given tuple of tuples
data = ((10, 10, 10, 12),
        (30, 45, 56, 45),
        (81, 80, 39, 32),
        (1, 2, 3, 4))

# List to store averages
averages = []

# Calculate average of each column
for i in range(len(data[0])):
    total = 0
    for row in data:
        total += row[i]
    avg = total / len(data)
    averages.append(avg)

print(averages)
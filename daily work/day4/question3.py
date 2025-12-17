def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False   # important!

# Test the function
list1 = [1, 2, 3, 4]
list2 = [3, 47, 8]

print(overlapping(list1, list2))  # Output: True

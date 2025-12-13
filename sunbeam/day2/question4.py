import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Example
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")
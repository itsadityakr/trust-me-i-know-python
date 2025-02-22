import math  # Importing the math module for mathematical operations

x = 9  # Integer value

# Math Constants
print(math.pi)  # Prints the value of Pi (≈ 3.141592653589793)
print(math.e)  # Prints the value of Euler's number (≈ 2.718281828459045)

# Math Functions
print(math.sqrt(x))  # Square root of 9 → Output: 3.0
print(math.ceil(3.2))  # Ceiling function (rounds up) → Output: 4
print(math.floor(3.8))  # Floor function (rounds down) → Output: 3

# Additional Math Operations
x = 3.1423  # Floating-point number
y = 2  # Integer
z = -100  # Negative integer

# Rounding Function
result = round(x)  # Rounds to the nearest integer (3.1423 → 3) i.e. if x>=0.5 => 1 else x<0.5 => 0
print(result)  # Output: 3

# Absolute Value Function
result = abs(z)  # Converts negative numbers to positive
print(result)  # Output: 100

# Power Function
result = pow(z, y)  # Computes z^y (-100^2) → (-100 * -100)
print(result)  # Output: 10000

# Maximum Function
result = max(x, y)  # Returns the maximum of x and y
print(result)  # Output: 3.1423

# Minimum Function
result = min(x, y, z)  # Returns the smallest value
print(result)  # Output: -100
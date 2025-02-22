# Variables in Python
# A variable is a name that refers to a value stored in memory.

# 1. String Variable: Stores a sequence of characters
name = "Alice"
city = 'New York'

print(f"Name: {name}")
print(f"City: {city}")

# 2. Integer Variable: Stores whole numbers
age = 25
year = 2024

print(f"Age: {age}")
print(f"Year: {year}")

# 3. Float Variable: Stores decimal numbers
price = 99.99
temperature = 36.5

print(f"Price: {price}")
print(f"Temperature: {temperature}°C")

# 4. Boolean Variable: Stores True or False values
is_raining = False
is_sunny = True

print(f"Is it raining? {is_raining}")
print(f"Is it sunny? {is_sunny}")

# 5. List Variable: Stores multiple values in a single variable
fruits = ["Apple", "Banana", "Cherry"]
print(f"Fruits: {fruits}")
print(f"First Fruit: {fruits[0]}")  # Accessing first element

# 6. Tuple Variable: Similar to a list but immutable (cannot be changed)
coordinates = (10.5, 20.8)
print(f"Coordinates: {coordinates}")

# 7. Dictionary Variable: Stores key-value pairs
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(f"Person Info: {person}")
print(f"Person's Name: {person['name']}")

# 8. NoneType Variable: Represents the absence of a value
no_value = None
print(f"No Value: {no_value}")

# Variable Reassignment
x = 10
print(f"Original x: {x}")
x = 20  # Changing the value of x
print(f"Updated x: {x}")

# Dynamic Typing in Python
y = "Hello"  # y is a string
print(f"y before: {y} ({type(y)})")
y = 42  # y is now an integer
print(f"y after: {y} ({type(y)})")

# Multiple Assignments
a, b, c = 1, 2.5, "Python"
print(f"a: {a}, b: {b}, c: {c}")

# Swapping Variables
x, y = y, x
print(f"After swapping: x = {x}, y = {y}")

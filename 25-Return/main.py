"""
The `return` statement in Python is used to exit a function and send a value back to the caller. It allows functions to produce outputs that can be used elsewhere in the program.
"""

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b  # Basic return statement


def calculate(a, b):
    """Returns sum, difference, and product as a tuple."""
    return a + b, a - b, a * b  # Returning multiple values as a tuple


def greet(name):
    """Prints a greeting but returns None."""
    print(f"Hello, {name}!")  # No return statement, so returns None


def check_positive(number):
    """Uses early return to check if a number is positive."""
    if number > 0:
        return "Positive"  # Returns early if condition is met
    return "Not Positive"  # Default return statement


def create_person(name, age):
    """Returns a dictionary representing a person."""
    return {"name": name, "age": age}  # Returning a complex data structure


def create_multiplier(factor):
    """Returns a function that multiplies by a given factor."""
    def multiplier(number):
        return number * factor  # Inner function uses the factor
    return multiplier  # Returning a function


def add_return(a, b):
    """Returns the sum of two numbers."""
    return a + b  # Returns a value


def add_print(a, b):
    """Prints the sum of two numbers but does not return anything."""
    print(a + b)  # Prints the value but does not return it

# Testing the functions
print("1. Basic Return:")
result = add(3, 5)  # Calling function, expected output: 8
print("Sum:", result)  # Output: Sum: 8

print("\n2. Returning Multiple Values:")
sum_result, difference, product = calculate(10, 5)  # Expected output: (15, 5, 50)
print("Sum:", sum_result, "Difference:", difference, "Product:", product)  # Output: Sum: 15 Difference: 5 Product: 50

print("\n3. Returning None:")
result = greet("Alice")  # Expected output: "Hello, Alice!"
print("Return value of greet():", result)  # Output: Return value of greet(): None

print("\n4. Early Return:")
print("check_positive(10):", check_positive(10))  # Expected output: Positive
print("check_positive(-5):", check_positive(-5))  # Expected output: Not Positive

print("\n5. Returning Complex Data Structures:")
person = create_person("Alice", 30)  # Expected output: {'name': 'Alice', 'age': 30}
print("Person details:", person)  # Output: Person details: {'name': 'Alice', 'age': 30}

print("\n6. Returning Functions:")
double = create_multiplier(2)  # Function that doubles a number
triple = create_multiplier(3)  # Function that triples a number
print("Double of 5:", double(5))  # Expected output: 10
print("Triple of 5:", triple(5))  # Expected output: 15

print("\n7. Return vs Print:")
result = add_return(3, 5)  # Expected output: 8
print("Result from add_return:", result)  # Output: Result from add_return: 8
add_print(3, 5)  # Expected output: 8 (printed but not returned)

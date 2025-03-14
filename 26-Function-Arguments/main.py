"""
Python Function Arguments Example
This script demonstrates different types of function arguments in Python:
1. Positional Arguments
2. Default Arguments
3. Keyword Arguments
4. Arbitrary Arguments (*args and **kwargs)
5. Combining All Types of Arguments
"""

def add(a, b):
    """This function adds two numbers."""
    return a + b  # Return the sum of a and b

# Positional Arguments Example
result = add(3, 5)  # 3 is assigned to 'a', 5 is assigned to 'b'
print("Sum:", result)  # Expected Output: Sum: 8


def greet(name="Guest"):
    """This function greets the user or a guest if no name is provided."""
    print(f"Hello, {name}!")  # Use the parameter with a default value

# Default Arguments Example
greet()  # Expected Output: Hello, Guest!
greet("Alice")  # Expected Output: Hello, Alice!


def describe_pet(pet_name, animal_type):
    """This function describes a pet."""
    print(f"I have a {animal_type} named {pet_name}.")  # Use the parameters

# Keyword Arguments Example
describe_pet(pet_name="Max", animal_type="dog")  # Expected Output: I have a dog named Max.
describe_pet(animal_type="cat", pet_name="Whiskers")  # Expected Output: I have a cat named Whiskers.


def sum_all(*args):
    """This function sums all the arguments passed to it."""
    total = sum(args)  # args is a tuple of all positional arguments
    return total

# Arbitrary Positional Arguments (*args) Example
result = sum_all(1, 2, 3, 4, 5)  # Pass any number of arguments
print("Sum:", result)  # Expected Output: Sum: 15


def describe_person(**kwargs):
    """This function describes a person using keyword arguments."""
    for key, value in kwargs.items():  # kwargs is a dictionary of keyword arguments
        print(f"{key}: {value}")

# Arbitrary Keyword Arguments (**kwargs) Example
describe_person(name="Alice", age=30, occupation="Engineer")
# Expected Output:
# name: Alice
# age: 30
# occupation: Engineer


def create_profile(name, age=30, *args, **kwargs):
    """This function creates a profile with optional details."""
    print(f"Name: {name}, Age: {age}")  # Print required and default arguments
    if args:  # Print additional positional arguments
        print("Additional positional arguments:", args)
    if kwargs:  # Print additional keyword arguments
        print("Additional keyword arguments:")
        for key, value in kwargs.items():
            print(f"{key}: {value}")

# Combining All Types of Arguments Example
create_profile("Alice", 25, "Engineer", city="New York", country="USA")
# Expected Output:
# Name: Alice, Age: 25
# Additional positional arguments: ('Engineer',)
# Additional keyword arguments:
# city: New York
# country: USA

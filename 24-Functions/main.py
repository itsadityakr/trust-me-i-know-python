# Functions in Python
# This script demonstrates various types of functions, their parameters, and return values.

# Function to print a simple greeting
def greet():
    """
    Prints a simple greeting message.
    Example output: "Hello, World!"
    """
    print("Hello, World!")  # Example output: Hello, World!

# Function to greet a person by name
def greet_name(name):
    """
    Greets a person using the provided name.
    Example output: "Hello, Alice!"
    """
    print(f"Hello, {name}!")  # Example output: Hello, Alice!

# Function to greet a person using their full name
def greet_full_name(first_name, last_name):
    """
    Greets a person using their full name.
    Example output: "Hello, John Doe!"
    """
    print(f"Hello, {first_name} {last_name}!")  # Example output: Hello, John Doe!

# Function with a default argument
def greet_default(name="Guest"):
    """
    Greets a person or uses 'Guest' if no name is provided.
    Example output: "Hello, Guest!"
    """
    print(f"Hello, {name}!")  # Example output: Hello, Guest!

# Function that returns a value
def add(a, b):
    """
    Adds two numbers and returns the result.
    Example output: 8
    """
    return a + b  # Example output: 8

# Function using keyword arguments
def describe_pet(pet_name, animal_type="dog"):
    """
    Describes a pet with a default type of 'dog'.
    Example output: "I have a dog named Max."
    """
    print(f"I have a {animal_type} named {pet_name}.")  # Example output: I have a dog named Max.

# Function with variable-length arguments using *args
def sum_all(*args):
    """
    Sums all arguments provided.
    Example output: 15
    """
    return sum(args)  # Example output: 15

# Function with variable-length keyword arguments using **kwargs
def describe_person(**kwargs):
    """
    Prints details about a person using keyword arguments.
    Example output:
    name: Alice
    age: 30
    occupation: Engineer
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Lambda function for quick addition
add_lambda = lambda a, b: a + b  # Example output: 8

# Main execution block
if __name__ == "__main__":
    greet()  # Example output: Hello, World!
    greet_name("Alice")  # Example output: Hello, Alice!
    greet_full_name("John", "Doe")  # Example output: Hello, John Doe!
    greet_default()  # Example output: Hello, Guest!
    greet_default("Bob")  # Example output: Hello, Bob!
    print("The sum is:", add(3, 5))  # Example output: The sum is: 8
    describe_pet(pet_name="Max")  # Example output: I have a dog named Max.
    describe_pet(animal_type="cat", pet_name="Whiskers")  # Example output: I have a cat named Whiskers.
    print("The sum of all numbers is:", sum_all(1, 2, 3, 4, 5))  # Example output: 15
    describe_person(name="Alice", age=30, occupation="Engineer")
    print("Lambda sum:", add_lambda(3, 5))  # Example output: Lambda sum: 8

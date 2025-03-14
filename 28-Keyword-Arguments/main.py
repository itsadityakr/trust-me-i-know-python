# Keyword Arguments in Python

# 1. Basic Keyword Arguments
def describe_pet(pet_name, animal_type):
    """This function describes a pet."""
    print(f"I have a {animal_type} named {pet_name}.")

# Call the function using keyword arguments
describe_pet(pet_name="Max", animal_type="dog")  # I have a dog named Max.
describe_pet(animal_type="cat", pet_name="Whiskers")  # I have a cat named Whiskers.


# 2. Mixing Positional and Keyword Arguments
def create_user(username, is_admin=False):
    """This function creates a user with an optional admin status."""
    print(f"User '{username}' created. Admin: {is_admin}")

# Call the function with a positional argument and a keyword argument
create_user("Alice", is_admin=True)  # User 'Alice' created. Admin: True


# 3. Default Arguments with Keyword Arguments
def create_profile(name, age=30, occupation="Engineer"):
    """This function creates a profile with optional age and occupation."""
    print(f"Name: {name}, Age: {age}, Occupation: {occupation}")

# Call the function using keyword arguments
create_profile("Alice")  # Name: Alice, Age: 30, Occupation: Engineer
create_profile("Bob", age=25)  # Name: Bob, Age: 25, Occupation: Engineer
create_profile("Charlie", occupation="Doctor")  # Name: Charlie, Age: 30, Occupation: Doctor


# 4. Arbitrary Keyword Arguments (**kwargs)
def describe_person(**kwargs):
    """This function describes a person using keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call the function with multiple keyword arguments
describe_person(name="Alice", age=30, occupation="Engineer")
# name: Alice
# age: 30
# occupation: Engineer


# 5. Combining Positional, Keyword, and Arbitrary Arguments
def create_profile(name, age=30, **kwargs):
    """This function creates a profile with optional details."""
    print(f"Name: {name}, Age: {age}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call the function with a mix of arguments
create_profile("Alice", occupation="Engineer", city="New York")
# Name: Alice, Age: 30
# occupation: Engineer
# city: New York

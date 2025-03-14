"""
Python Default Arguments Example
This script demonstrates the usage of default arguments in Python functions.
"""

def greet(name="Guest"):
    """This function greets the user or a guest if no name is provided."""
    print(f"Hello, {name}!")

greet()  # Expected Output: Hello, Guest!
greet("Alice")  # Expected Output: Hello, Alice!


def describe_pet(pet_name, animal_type="dog"):
    """This function describes a pet."""
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("Max")  # Expected Output: I have a dog named Max.
describe_pet("Whiskers", "cat")  # Expected Output: I have a cat named Whiskers.


def create_user(username, is_admin=False):
    """This function creates a user with an optional admin status."""
    print(f"User '{username}' created. Admin: {is_admin}")

create_user("Alice")  # Expected Output: User 'Alice' created. Admin: False
create_user("Bob", True)  # Expected Output: User 'Bob' created. Admin: True


def add_item(item, items=[]):
    """This function adds an item to a list."""
    items.append(item)
    return items

print(add_item("Apple"))  # Expected Output: ['Apple']
print(add_item("Banana"))  # Expected Output: ['Apple', 'Banana'] (Issue: shared mutable list)


def add_item_fixed(item, items=None):
    """This function adds an item to a list, avoiding mutable default issues."""
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item_fixed("Apple"))  # Expected Output: ['Apple']
print(add_item_fixed("Banana"))  # Expected Output: ['Banana']


def create_profile(name, age=30, occupation="Engineer"):
    """This function creates a profile with optional age and occupation."""
    print(f"Name: {name}, Age: {age}, Occupation: {occupation}")

create_profile("Alice")  # Expected Output: Name: Alice, Age: 30, Occupation: Engineer
create_profile("Bob", age=25)  # Expected Output: Name: Bob, Age: 25, Occupation: Engineer
create_profile("Charlie", occupation="Doctor")  # Expected Output: Name: Charlie, Age: 30, Occupation: Doctor

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

---

# Keyword Arguments in Python

Keyword arguments allow you to pass arguments to a function by specifying the parameter names. This makes the function calls more readable and flexible, as you can pass arguments in any order and skip optional parameters.

---

## 1. Basic Keyword Arguments

When calling a function, you can specify the parameter name along with its value. This is called a **keyword argument**.

### Example:
```python
# Define a function with multiple parameters
def describe_pet(pet_name, animal_type):
    """This function describes a pet."""
    print(f"I have a {animal_type} named {pet_name}.")  # Use the parameters

# Call the function using keyword arguments
describe_pet(pet_name="Max", animal_type="dog")  # Specify parameter names
describe_pet(animal_type="cat", pet_name="Whiskers")  # Order doesn't matter
```

Output:
```
I have a dog named Max.
I have a cat named Whiskers.
```

---

## 2. Mixing Positional and Keyword Arguments

You can mix positional arguments (passed in order) and keyword arguments. However, **positional arguments must come before keyword arguments**.

### Example:
```python
# Define a function with multiple parameters
def create_user(username, is_admin=False):
    """This function creates a user with an optional admin status."""
    print(f"User '{username}' created. Admin: {is_admin}")  # Use the parameters

# Call the function with a positional argument and a keyword argument
create_user("Alice", is_admin=True)  # 'Alice' is positional, 'is_admin' is keyword
```

Output:
```
User 'Alice' created. Admin: True
```

---

## 3. Default Arguments with Keyword Arguments

Keyword arguments are especially useful when working with functions that have default arguments. You can override only the parameters you want.

### Example:
```python
# Define a function with default arguments
def create_profile(name, age=30, occupation="Engineer"):
    """This function creates a profile with optional age and occupation."""
    print(f"Name: {name}, Age: {age}, Occupation: {occupation}")  # Use the parameters

# Call the function using keyword arguments
create_profile("Alice")  # Uses default values for age and occupation
create_profile("Bob", age=25)  # Overrides only the age
create_profile("Charlie", occupation="Doctor")  # Overrides only the occupation
```

Output:
```
Name: Alice, Age: 30, Occupation: Engineer
Name: Bob, Age: 25, Occupation: Engineer
Name: Charlie, Age: 30, Occupation: Doctor
```

---

## 4. Arbitrary Keyword Arguments (`**kwargs`)

If you want a function to accept an arbitrary number of keyword arguments, use `**kwargs`. This collects all keyword arguments into a dictionary.

### Example:
```python
# Define a function that accepts arbitrary keyword arguments
def describe_person(**kwargs):
    """This function describes a person using keyword arguments."""
    for key, value in kwargs.items():  # kwargs is a dictionary of keyword arguments
        print(f"{key}: {value}")

# Call the function with multiple keyword arguments
describe_person(name="Alice", age=30, occupation="Engineer")
```

Output:
```
name: Alice
age: 30
occupation: Engineer
```

---

## 5. Combining Positional, Keyword, and Arbitrary Arguments

You can combine positional arguments, keyword arguments, and arbitrary keyword arguments in a single function.

### Example:
```python
# Define a function with positional, keyword, and arbitrary keyword arguments
def create_profile(name, age=30, **kwargs):
    """This function creates a profile with optional details."""
    print(f"Name: {name}, Age: {age}")  # Print required and default arguments
    for key, value in kwargs.items():  # Print additional keyword arguments
        print(f"{key}: {value}")

# Call the function with a mix of arguments
create_profile("Alice", occupation="Engineer", city="New York")  # 'age' uses default value
```

Output:
```
Name: Alice, Age: 30
occupation: Engineer
city: New York
```

---

## 6. When to Use Keyword Arguments

- **Improve readability**: Keyword arguments make it clear what each argument represents.
- **Skip optional parameters**: You can omit arguments for parameters with default values.
- **Flexibility**: You can pass arguments in any order.

---

## Summary of Key Points

- **Keyword arguments** are passed to a function using the parameter name.
- You can mix **positional** and **keyword arguments**, but positional arguments must come first.
- Use `**kwargs` to accept an arbitrary number of keyword arguments.
- Keyword arguments are especially useful for functions with **default arguments**.
- They improve readability and flexibility in function calls.

---

![Static Badge](https://img.shields.io/badge/Aditya%20Kumar-black?style=for-the-badge&logo=atlasos&logoColor=%23ffffff)
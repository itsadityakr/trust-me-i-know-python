![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

---

# Default Arguments in Python

Default arguments allow you to define functions with parameters that have default values. If the caller does not provide a value for that parameter, the default value is used. This makes functions more flexible and reduces the need for repetitive code.

---

## 1. Basic Default Argument

You can specify a default value for a parameter by assigning it in the function definition.

### Example:
```python
# Define a function with a default argument
def greet(name="Guest"):  # "Guest" is the default value for the 'name' parameter
    """This function greets the user or a guest if no name is provided."""
    print(f"Hello, {name}!")  # Use the parameter with a default value

# Call the function without providing an argument
greet()  # Uses the default value "Guest"

# Call the function with an argument
greet("Alice")  # Overrides the default value
```

Output:
```
Hello, Guest!
Hello, Alice!
```

---

## 2. Multiple Default Arguments

You can define multiple parameters with default values. However, all parameters with default values must come **after** parameters without default values.

### Example:
```python
# Define a function with multiple default arguments
def describe_pet(pet_name, animal_type="dog"):  # 'animal_type' has a default value
    """This function describes a pet."""
    print(f"I have a {animal_type} named {pet_name}.")  # Use the parameters

# Call the function with only the required argument
describe_pet("Max")  # Uses the default value for 'animal_type'

# Call the function with both arguments
describe_pet("Whiskers", "cat")  # Overrides the default value for 'animal_type'
```

Output:
```
I have a dog named Max.
I have a cat named Whiskers.
```

---

## 3. Mixing Default and Non-Default Arguments

When defining a function, parameters without default values must come before parameters with default values. This is a rule in Python to avoid ambiguity.

### Example:
```python
# Define a function with a mix of default and non-default arguments
def create_user(username, is_admin=False):  # 'is_admin' has a default value
    """This function creates a user with an optional admin status."""
    print(f"User '{username}' created. Admin: {is_admin}")  # Use the parameters

# Call the function with only the required argument
create_user("Alice")  # Uses the default value for 'is_admin'

# Call the function with both arguments
create_user("Bob", True)  # Overrides the default value for 'is_admin'
```

Output:
```
User 'Alice' created. Admin: False
User 'Bob' created. Admin: True
```

---

## 4. Default Arguments with Mutable Objects

Be cautious when using mutable objects (like lists or dictionaries) as default arguments. They are created **once** when the function is defined, not each time the function is called. This can lead to unexpected behavior.

### Example:
```python
# Define a function with a mutable default argument
def add_item(item, items=[]):  # 'items' is a list with a default value
    """This function adds an item to a list."""
    items.append(item)  # Modify the default list
    return items

# Call the function multiple times
print(add_item("Apple"))  # Expected: ['Apple']
print(add_item("Banana"))  # Expected: ['Banana'], but actual: ['Apple', 'Banana']
```

Output:
```
['Apple']
['Apple', 'Banana']
```

### Fixing the Issue
To avoid this, use `None` as the default value and initialize the mutable object inside the function.

```python
# Define a function with a fixed mutable default argument
def add_item_fixed(item, items=None):  # Use None as the default value
    """This function adds an item to a list, avoiding mutable default issues."""
    if items is None:  # Initialize the list if it's None
        items = []
    items.append(item)  # Modify the list
    return items

# Call the function multiple times
print(add_item_fixed("Apple"))  # Expected: ['Apple']
print(add_item_fixed("Banana"))  # Expected: ['Banana']
```

Output:
```
['Apple']
['Banana']
```

---

## 5. Keyword Arguments with Default Values

You can use keyword arguments to override default values selectively.

### Example:
```python
# Define a function with multiple default arguments
def create_profile(name, age=30, occupation="Engineer"):  # Default values for age and occupation
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

## Summary of Key Points

- **Default arguments** allow you to specify default values for function parameters.
- Parameters with default values must come **after** parameters without default values.
- Be cautious when using **mutable objects** (like lists or dictionaries) as default arguments, as they are created only once.
- Use `None` as the default value for mutable objects and initialize them inside the function to avoid issues.
- **Keyword arguments** can be used to override default values selectively.

---

![Static Badge](https://img.shields.io/badge/Aditya%20Kumar-black?style=for-the-badge&logo=atlasos&logoColor=%23ffffff)
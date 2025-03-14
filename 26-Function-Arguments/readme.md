![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

---

# Function Arguments in Python

Python functions can accept different types of arguments, including **positional**, **default**, **keyword**, and **arbitrary arguments**. Each type serves a specific purpose and makes functions more flexible and powerful.

---

## 1. Positional Arguments

Positional arguments are the most basic type of arguments. They are passed to a function in the order they are defined.

### Example:
```python
# Define a function with positional arguments
def add(a, b):
    """This function adds two numbers."""
    return a + b  # Return the sum of a and b

# Call the function with positional arguments
result = add(3, 5)  # 3 is assigned to 'a', 5 is assigned to 'b'
print("Sum:", result)
```

Output:
```
Sum: 8
```

---

## 2. Default Arguments

Default arguments allow you to specify default values for parameters. If the caller does not provide a value, the default is used.

### Example:
```python
# Define a function with a default argument
def greet(name="Guest"):
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

## 3. Keyword Arguments

Keyword arguments allow you to pass arguments to a function by specifying the parameter names. This makes the function call more readable and flexible.

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

## 4. Arbitrary Arguments (`*args` and `**kwargs`)

Arbitrary arguments allow a function to accept an arbitrary number of positional or keyword arguments.

### a. Arbitrary Positional Arguments (`*args`)

Use `*args` to accept any number of positional arguments. They are collected into a tuple.

#### Example:
```python
# Define a function that accepts any number of positional arguments
def sum_all(*args):
    """This function sums all the arguments passed to it."""
    total = 0
    for num in args:  # args is a tuple of all positional arguments
        total += num
    return total

# Call the function with multiple arguments
result = sum_all(1, 2, 3, 4, 5)  # Pass any number of arguments
print("Sum:", result)
```

Output:
```
Sum: 15
```

### b. Arbitrary Keyword Arguments (`**kwargs`)

Use `**kwargs` to accept any number of keyword arguments. They are collected into a dictionary.

#### Example:
```python
# Define a function that accepts any number of keyword arguments
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

## 5. Combining All Types of Arguments

You can combine positional, default, keyword, and arbitrary arguments in a single function. However, the order of parameters must follow this rule:

1. Positional arguments
2. `*args` (arbitrary positional arguments)
3. Keyword arguments
4. `**kwargs` (arbitrary keyword arguments)

### Example:
```python
# Define a function with all types of arguments
def create_profile(name, age=30, *args, **kwargs):
    """This function creates a profile with optional details."""
    print(f"Name: {name}, Age: {age}")  # Print required and default arguments
    if args:  # Print additional positional arguments
        print("Additional positional arguments:", args)
    if kwargs:  # Print additional keyword arguments
        print("Additional keyword arguments:")
        for key, value in kwargs.items():
            print(f"{key}: {value}")

# Call the function with a mix of arguments
create_profile("Alice", 25, "Engineer", city="New York", country="USA")
```

Output:
```
Name: Alice, Age: 25
Additional positional arguments: ('Engineer',)
Additional keyword arguments:
city: New York
country: USA
```

---

## Summary of Key Points

- **Positional arguments**: Passed in order and assigned to parameters based on their position.
- **Default arguments**: Provide default values for parameters if no argument is passed.
- **Keyword arguments**: Passed using parameter names, making function calls more readable.
- **Arbitrary arguments**:
  - `*args`: Accepts any number of positional arguments as a tuple.
  - `**kwargs`: Accepts any number of keyword arguments as a dictionary.
- **Order of parameters**: Positional → `*args` → Keyword → `**kwargs`.

---

![Static Badge](https://img.shields.io/badge/Aditya%20Kumar-black?style=for-the-badge&logo=atlasos&logoColor=%23ffffff)
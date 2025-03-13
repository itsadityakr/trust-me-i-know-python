
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

---

# Functions in Python

Functions are reusable blocks of code that perform a specific task. They help organize code, avoid repetition, and make programs easier to read and maintain.

---

## 1. Defining a Function

To define a function, use the `def` keyword followed by the function name, parentheses `()`, and a colon `:`. The code inside the function is indented.

```python
# Define a simple function
def greet():
    """This function prints a greeting message."""  # Docstring: describes the function's purpose
    print("Hello, World!")  # Code inside the function
```

---

## 2. Calling a Function

To execute a function, you need to call it by using its name followed by parentheses `()`.

```python
# Call the greet function
greet()  # This will execute the code inside the function
```

Output:
```
Hello, World!
```

---

## 3. Functions with Parameters

Functions can accept inputs called **parameters**. These are specified inside the parentheses when defining the function.

```python
# Define a function with a parameter
def greet_name(name):  # 'name' is a parameter
    """This function greets the person passed as a parameter."""
    print(f"Hello, {name}!")  # Use the parameter in the function
```

Call the function with an argument:
```python
greet_name("Alice")  # "Alice" is the argument passed to the function
```

Output:
```
Hello, Alice!
```

---

## 4. Functions with Multiple Parameters

Functions can have multiple parameters. Separate them with commas.

```python
# Define a function with multiple parameters
def greet_full_name(first_name, last_name):
    """This function greets a person using their full name."""
    print(f"Hello, {first_name} {last_name}!")  # Use both parameters
```

Call the function with arguments:
```python
greet_full_name("John", "Doe")  # Pass two arguments
```

Output:
```
Hello, John Doe!
```

---

## 5. Default Arguments

You can provide default values for parameters. If the caller doesn't provide an argument, the default value is used.

```python
# Define a function with a default argument
def greet_default(name="Guest"):  # "Guest" is the default value
    """This function greets the user or a guest if no name is provided."""
    print(f"Hello, {name}!")  # Use the parameter with a default value
```

Call the function with and without arguments:
```python
greet_default()  # No argument provided, uses default
greet_default("Alice")  # Argument provided, overrides default
```

Output:
```
Hello, Guest!
Hello, Alice!
```

---

## 6. Return Values

Functions can return a value using the `return` keyword. This allows the function to produce an output that can be used elsewhere in the program.

```python
# Define a function that returns a value
def add(a, b):
    """This function adds two numbers and returns the result."""
    return a + b  # Return the sum of a and b
```

Call the function and use the return value:
```python
result = add(3, 5)  # Call the function and store the result
print("The sum is:", result)  # Print the result
```

Output:
```
The sum is: 8
```

---

## 7. Keyword Arguments

You can call a function using keyword arguments, where you specify the parameter name and its value. This makes the code more readable and allows you to pass arguments in any order.

```python
# Define a function with multiple parameters
def describe_pet(pet_name, animal_type="dog"):
    """This function describes a pet."""
    print(f"I have a {animal_type} named {pet_name}.")  # Use the parameters
```

Call the function using keyword arguments:
```python
describe_pet(pet_name="Max")  # Use default for animal_type
describe_pet(animal_type="cat", pet_name="Whiskers")  # Specify both arguments
```

Output:
```
I have a dog named Max.
I have a cat named Whiskers.
```

---

## 8. Variable-Length Arguments

You can define functions that accept a variable number of arguments using `*args` (for positional arguments) and `**kwargs` (for keyword arguments).

### Using `*args`
```python
# Define a function that accepts any number of positional arguments
def sum_all(*args):
    """This function sums all the arguments passed to it."""
    total = 0
    for num in args:  # args is a tuple of all positional arguments
        total += num
    return total
```

Call the function with multiple arguments:
```python
result = sum_all(1, 2, 3, 4, 5)  # Pass any number of arguments
print("The sum is:", result)
```

Output:
```
The sum is: 15
```

### Using `**kwargs`
```python
# Define a function that accepts any number of keyword arguments
def describe_person(**kwargs):
    """This function describes a person using keyword arguments."""
    for key, value in kwargs.items():  # kwargs is a dictionary of keyword arguments
        print(f"{key}: {value}")
```

Call the function with keyword arguments:
```python
describe_person(name="Alice", age=30, occupation="Engineer")
```

Output:
```
name: Alice
age: 30
occupation: Engineer
```

---

## 9. Lambda Functions

Lambda functions are small, anonymous functions defined using the `lambda` keyword. They are useful for short, one-time operations.

```python
# Define a lambda function to add two numbers
add = lambda a, b: a + b  # No 'def' keyword, no function name

# Call the lambda function
result = add(3, 5)
print("The sum is:", result)
```

Output:
```
The sum is: 8
```

---

## Summary of Key Concepts

- **Defining a Function**: Use `def` followed by the function name and parameters.
- **Calling a Function**: Use the function name followed by parentheses `()`.
- **Parameters and Arguments**: Parameters are inputs to a function; arguments are the values passed to the function.
- **Default Arguments**: Provide default values for parameters.
- **Return Values**: Use `return` to send a value back to the caller.
- **Keyword Arguments**: Pass arguments using parameter names for clarity.
- **Variable-Length Arguments**: Use `*args` for positional arguments and `**kwargs` for keyword arguments.
- **Lambda Functions**: Small, anonymous functions defined with `lambda`.

---

![Static Badge](https://img.shields.io/badge/Aditya%20Kumar-black?style=for-the-badge&logo=atlasos&logoColor=%23ffffff)
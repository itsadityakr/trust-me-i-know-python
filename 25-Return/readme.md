
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

---
# ```return``` in Python

The `return` statement in Python is used to **exit a function and send a value back to the caller**. It is a crucial part of functions, as it allows them to produce outputs that can be used elsewhere in the program. Below is a detailed explanation of the `return` statement, with examples and in-depth comments.

---

## 1. Basic `return` Statement

The `return` statement exits the function and optionally returns a value. If no value is specified, the function returns `None`.

### Example:
```python
# Define a function that returns a value
def add(a, b):
    """This function adds two numbers and returns the result."""
    return a + b  # Return the sum of a and b

# Call the function and store the result
result = add(3, 5)  # The function returns 8
print("The sum is:", result)  # Print the result
```

Output:
```
The sum is: 8
```

---

## 2. Returning Multiple Values

A function can return multiple values by separating them with commas. These values are returned as a **tuple**.

### Example:
```python
# Define a function that returns multiple values
def calculate(a, b):
    """This function returns the sum, difference, and product of two numbers."""
    sum_result = a + b
    difference = a - b
    product = a * b
    return sum_result, difference, product  # Return multiple values as a tuple

# Call the function and unpack the returned values
sum_result, difference, product = calculate(10, 5)  # Unpack the tuple
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
```

Output:
```
Sum: 15
Difference: 5
Product: 50
```

---

## 3. Returning `None`

If a function does not have a `return` statement or has a `return` statement without a value, it returns `None`.

### Example:
```python
# Define a function without a return statement
def greet(name):
    """This function prints a greeting but does not return a value."""
    print(f"Hello, {name}!")

# Call the function and check its return value
result = greet("Alice")  # The function prints a message but returns None
print("Return value of greet():", result)
```

Output:
```
Hello, Alice!
Return value of greet(): None
```

---

## 4. Early Return

You can use the `return` statement to exit a function early, based on a condition.

### Example:
```python
# Define a function with an early return
def check_positive(number):
    """This function checks if a number is positive."""
    if number > 0:
        return "Positive"  # Exit early if the condition is met
    return "Not Positive"  # This line is executed only if the condition is not met

# Call the function
print(check_positive(10))  # Output: Positive
print(check_positive(-5))  # Output: Not Positive
```

Output:
```
Positive
Not Positive
```

---

## 5. Returning Complex Data Structures

Functions can return complex data structures like lists, dictionaries, or even other functions.

### Example:
```python
# Define a function that returns a dictionary
def create_person(name, age):
    """This function returns a dictionary representing a person."""
    return {
        "name": name,
        "age": age
    }

# Call the function and use the returned dictionary
person = create_person("Alice", 30)
print("Person details:", person)
```

Output:
```
Person details: {'name': 'Alice', 'age': 30}
```

---

## 6. Returning Functions

A function can also return another function. This is useful in advanced programming patterns like closures and decorators.

### Example:
```python
# Define a function that returns another function
def create_multiplier(factor):
    """This function returns a new function that multiplies by the given factor."""
    def multiplier(number):
        return number * factor
    return multiplier  # Return the inner function

# Call the outer function to get the inner function
double = create_multiplier(2)  # Returns a function that multiplies by 2
triple = create_multiplier(3)  # Returns a function that multiplies by 3

# Use the returned functions
print("Double of 5:", double(5))  # Output: 10
print("Triple of 5:", triple(5))  # Output: 15
```

Output:
```
Double of 5: 10
Triple of 5: 15
```

---

## 7. `return` vs `print`

It’s important to distinguish between `return` and `print`. The `return` statement sends a value back to the caller, while `print` simply displays a value to the console.

### Example:
```python
# Define a function that uses return
def add_return(a, b):
    """This function returns the sum of two numbers."""
    return a + b

# Define a function that uses print
def add_print(a, b):
    """This function prints the sum of two numbers."""
    print(a + b)

# Using the return function
result = add_return(3, 5)  # The function returns 8
print("Result from add_return:", result)  # Output: 8

# Using the print function
add_print(3, 5)  # The function prints 8 but returns None
```

Output:
```
Result from add_return: 8
8
```

---

## Summary of Key Points

- The `return` statement exits a function and sends a value back to the caller.
- A function can return multiple values as a tuple.
- If no `return` statement is present, the function returns `None`.
- You can use `return` to exit a function early based on a condition.
- Functions can return complex data structures like lists, dictionaries, or even other functions.
- `return` is different from `print`: `return` sends a value back to the caller, while `print` displays a value to the console.

---

![Static Badge](https://img.shields.io/badge/Aditya%20Kumar-black?style=for-the-badge&logo=atlasos&logoColor=%23ffffff)
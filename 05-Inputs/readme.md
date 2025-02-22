
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

# The `input()` Function

The `input()` function is used to take user input from the console. By default, **input is always taken as a string**, even if the user enters a number. If numerical operations are needed, the input must be **type-cast** accordingly.  

---

## Using `input()`  

```python
# Taking a string input
name = input("Enter your Name: ")
print(f"Hi {name}")
```

- The `input("Enter your Name: ")` function prompts the user to enter their name.  
- The entered value is stored as a **string** in the variable `name`.  
- The `print(f"Hi {name}")` statement outputs the user's name.  

---

## Taking an Integer Input  

```python
# Taking an integer input
age = input("Enter your age: ")
print(f"Your age is: {age}")
```

- The `input("Enter your age: ")` function prompts the user to enter their age.  
- However, `input()` stores the value as a **string**, not an integer.  
- Printing `age` works fine because strings can be printed directly.  

---

## Type Casting for Numerical Operations  

```python
# Attempting to add 1 to age (Incorrect)
# ageAdd = age + 1  # This will cause an error: TypeError: can only concatenate str (not "int") to str

# Correcting it using type casting
ageAdd = int(age) + 1  # Convert age from string to integer before adding
print(ageAdd)
```

- The line `ageAdd = age + 1` causes an **error** because `age` is a string, and Python does not allow adding an integer (`1`) to a string.  
- The correct way is to **convert `age` to an integer using `int(age)`** before performing mathematical operations.  
- The corrected version `ageAdd = int(age) + 1` successfully increments the age by `1` and prints the result.  

---

## Summary  

| Input Type | Example Input | Stored as | Type Casting Required? |
|------------|--------------|-----------|-----------------------|
| String | `"John"` | `"John"` (str) | No |
| Integer | `"25"` | `"25"` (str) | Yes (`int(age)`) |
| Float | `"7.5"` | `"7.5"` (str) | Yes (`float(value)`) |

The `input()` function always returns a **string**, so type casting is necessary for numerical calculations.

![Static Badge](https://img.shields.io/badge/Aditya%20Kumar-black?style=for-the-badge&logo=atlasos&logoColor=%23ffffff)
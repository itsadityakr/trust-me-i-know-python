
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

# Type Casting (Type Conversion)

Python allows converting one data type to another using built-in functions such as `str()`, `int()`, `float()`, and `bool()`. Type casting is useful when handling different data types dynamically.  

---

## Defining Variables of Different Data Types  

```python
name_blank = ""  # Empty string
name = "Aditya"  # Non-empty string
age = 25  # Integer
cgpa = 7.6  # Float
is_human = True  # Boolean
```

- `name_blank` is an empty string (`""`).  
- `name` is a non-empty string (`"Aditya"`).  
- `age` is an integer (`25`).  
- `cgpa` is a floating-point number (`7.6`).  
- `is_human` is a boolean (`True`).  

---

## Type Casting Demonstrations  

### 1. Converting a String to a Boolean  

```python
print(bool(name_blank))  # Output: False (empty string is considered False)
print(bool(name))  # Output: True (non-empty strings are considered True)
```

- An **empty string** (`""`) is treated as `False` when converted to a boolean.  
- A **non-empty string** (`"Aditya"`) is treated as `True`.  

---

### 2. Converting an Integer to a String  

```python
print(str(age))  # Output: '25' (Integer converted to string)
```

- The integer `25` is converted to a string `'25'`.  

---

### 3. Converting a Boolean to a String  

```python
print(str(is_human))  # Output: 'True' (Boolean converted to string)
```

- The boolean `True` is converted to the string `'True'`.  

---

### 4. Converting an Integer to a Float  

```python
print(float(age))  # Output: 25.0 (Integer converted to float)
```

- The integer `25` is converted to `25.0` (a float).  

---

### 5. Converting a Float to an Integer  

```python
print(int(cgpa))  # Output: 7 (Decimal part is truncated)
```

- The float `7.6` is converted to `7`, **truncating** the decimal part (not rounding).  

---

### 6. Converting a Boolean to an Integer  

```python
print(int(is_human))  # Output: 1 (True is equivalent to 1)
```

- `True` is converted to `1`, and `False` would be converted to `0`.  

---

### 7. Attempting to Convert an Empty String to an Integer  

```python
# print(int(name_blank))  # Uncommenting this will raise a ValueError
```

- Trying to convert an empty string (`""`) to an integer results in an **error** (`ValueError`).  
- Reason: An empty string does not represent a valid integer.  

---

## Summary  

| Conversion Type | Example | Output | Notes |
|---------------|---------|--------|-------|
| String to Boolean | `bool("")` | `False` | Empty strings are `False` |
| String to Boolean | `bool("Aditya")` | `True` | Non-empty strings are `True` |
| Integer to String | `str(25)` | `'25'` | Integer is converted to string |
| Boolean to String | `str(True)` | `'True'` | Boolean is converted to string |
| Integer to Float | `float(25)` | `25.0` | Integer is converted to float |
| Float to Integer | `int(7.6)` | `7` | Decimal part is truncated |
| Boolean to Integer | `int(True)` | `1` | `True` → `1`, `False` → `0` |
| Empty String to Integer | `int("")` | `Error` | Raises `ValueError` |

Type casting is useful when working with user inputs, mathematical calculations, and data transformations in Python.

![Static Badge](https://img.shields.io/badge/Aditya%20Kumar-black?style=for-the-badge&logo=atlasos&logoColor=%23ffffff)
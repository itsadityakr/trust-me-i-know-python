
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

# Using the Math Module  

Python's `math` module provides **mathematical constants and functions** to perform various operations like square root, rounding, absolute value, power functions, and more.  

---

## **Importing the Math Module**  
Before using mathematical functions, **import** the `math` module:  

```python
import math  # Importing the math module for mathematical operations
```

---

## **Math Constants**  

```python
print(math.pi)  # Pi (≈ 3.141592653589793)
print(math.e)   # Euler's number (≈ 2.718281828459045)
```
- `math.pi` returns the **value of Pi**.  
- `math.e` returns **Euler’s number**.  

---

## **Basic Math Functions**  

```python
x = 9  # Integer value

# Square Root
print(math.sqrt(x))  # Square root of 9 → Output: 3.0

# Ceiling Function (rounds up)
print(math.ceil(3.2))  # Output: 4

# Floor Function (rounds down)
print(math.floor(3.8))  # Output: 3
```
- `math.sqrt(x)`: Returns the **square root** of `x`.  
- `math.ceil(x)`: **Rounds up** to the nearest integer.  
- `math.floor(x)`: **Rounds down** to the nearest integer.  

---

## **Additional Math Operations**  

```python
x = 3.1423  # Floating-point number
y = 2  # Integer
z = -100  # Negative integer
```

### **Rounding Function**  
```python
result = round(x)  # Rounds to the nearest integer
print(result)  # Output: 3
```
- `round(x)`: Rounds `x` to the nearest **integer**.  

### **Absolute Value Function**  
```python
result = abs(z)  # Converts negative numbers to positive
print(result)  # Output: 100
```
- `abs(x)`: Returns the **absolute value** of `x`.  

### **Power Function**  
```python
result = pow(z, y)  # Computes z^y (-100^2)
print(result)  # Output: 10000
```
- `pow(a, b)`: Returns `a` raised to the power of `b` (`a^b`).  

### **Finding Maximum & Minimum Values**  
```python
result = max(x, y)  # Maximum of x and y
print(result)  # Output: 3.1423

result = min(x, y, z)  # Minimum value
print(result)  # Output: -100
```
- `max(a, b, c, ...)`: Returns the **largest** value.  
- `min(a, b, c, ...)`: Returns the **smallest** value.  

---

## **Summary Table**  

| Function  | Description | Example | Output |
|-----------|-------------|---------|--------|
| `math.sqrt(x)` | Square root of `x` | `math.sqrt(9)` | `3.0` |
| `math.ceil(x)` | Rounds `x` up | `math.ceil(3.2)` | `4` |
| `math.floor(x)` | Rounds `x` down | `math.floor(3.8)` | `3` |
| `round(x)` | Rounds `x` to the nearest integer | `round(3.1423)` | `3` |
| `abs(x)` | Absolute value of `x` | `abs(-100)` | `100` |
| `pow(a, b)` | Raises `a` to power `b` | `pow(2, 3)` | `8` |
| `max(a, b, c, …)` | Returns the largest value | `max(2, 5, 8)` | `8` |
| `min(a, b, c, …)` | Returns the smallest value | `min(2, 5, 8)` | `2` |

---

Using the **math module**, you can perform various **mathematical calculations efficiently** in Python!

![Static Badge](https://img.shields.io/badge/Aditya%20Kumar-black?style=for-the-badge&logo=atlasos&logoColor=%23ffffff)
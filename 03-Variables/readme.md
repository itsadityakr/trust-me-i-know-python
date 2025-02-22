
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

# Variables

A variable is a name that refers to a value stored in memory. Python allows different types of variables, including strings, numbers, booleans, lists, tuples, dictionaries, and `NoneType`.  

---

## 1. String Variables  
String variables store sequences of characters. A string can be enclosed in either single (`'`) or double (`"`) quotes.  

```python
name = "Alice"
city = 'New York'

print(f"Name: {name}")  # Output: Name: Alice
print(f"City: {city}")  # Output: City: New York
```

---

## 2. Integer Variables  
Integer variables store whole numbers.  

```python
age = 25
year = 2024

print(f"Age: {age}")  # Output: Age: 25
print(f"Year: {year}")  # Output: Year: 2024
```

---

## 3. Float Variables  
Float variables store decimal numbers.  

```python
price = 99.99
temperature = 36.5

print(f"Price: {price}")  # Output: Price: 99.99
print(f"Temperature: {temperature}°C")  # Output: Temperature: 36.5°C
```

---

## 4. Boolean Variables  
Boolean variables store `True` or `False` values.  

```python
is_raining = False
is_sunny = True

print(f"Is it raining? {is_raining}")  # Output: Is it raining? False
print(f"Is it sunny? {is_sunny}")  # Output: Is it sunny? True
```

---

## 5. List Variables  
A list stores multiple values in a single variable. Lists are mutable, meaning their values can be changed.  

```python
fruits = ["Apple", "Banana", "Cherry"]

print(f"Fruits: {fruits}")  # Output: Fruits: ['Apple', 'Banana', 'Cherry']
print(f"First Fruit: {fruits[0]}")  # Output: First Fruit: Apple
```

---

## 6. Tuple Variables  
A tuple is similar to a list but immutable, meaning its values cannot be changed.  

```python
coordinates = (10.5, 20.8)

print(f"Coordinates: {coordinates}")  # Output: Coordinates: (10.5, 20.8)
```

---

## 7. Dictionary Variables  
A dictionary stores key-value pairs. It is used to store structured data.  

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print(f"Person Info: {person}")  
# Output: Person Info: {'name': 'Alice', 'age': 25, 'city': 'New York'}

print(f"Person's Name: {person['name']}")  
# Output: Person's Name: Alice
```

---

## 8. NoneType Variables  
The `None` type represents the absence of a value.  

```python
no_value = None

print(f"No Value: {no_value}")  # Output: No Value: None
```

---

## Variable Reassignment  
Variables can be reassigned to new values.  

```python
x = 10
print(f"Original x: {x}")  # Output: Original x: 10

x = 20  # Changing the value of x
print(f"Updated x: {x}")  # Output: Updated x: 20
```

---

## Dynamic Typing in Python  
Python allows variables to change types dynamically.  

```python
y = "Hello"  # y is a string
print(f"y before: {y} ({type(y)})")  # Output: y before: Hello (<class 'str'>)

y = 42  # y is now an integer
print(f"y after: {y} ({type(y)})")  # Output: y after: 42 (<class 'int'>)
```

---

## Multiple Assignments  
Python allows assigning multiple values to multiple variables in a single line.  

```python
a, b, c = 1, 2.5, "Python"

print(f"a: {a}, b: {b}, c: {c}")  # Output: a: 1, b: 2.5, c: Python
```

---

## Swapping Variables  
Python allows swapping two variables without using a temporary variable.  

```python
x, y = 10, 20
x, y = y, x  # Swaps values

print(f"After swapping: x = {x}, y = {y}")  
# Output: After swapping: x = 20, y = 10
```

---

### Summary  
- **String** stores text. Example: `"Hello"`  
- **Integer** stores whole numbers. Example: `25`  
- **Float** stores decimal numbers. Example: `99.99`  
- **Boolean** stores `True` or `False`. Example: `is_raining = False`  
- **List** stores multiple values. Example: `["Apple", "Banana", "Cherry"]`  
- **Tuple** is like a list but immutable. Example: `(10.5, 20.8)`  
- **Dictionary** stores key-value pairs. Example: `{"name": "Alice", "age": 25}`  
- **NoneType** represents no value. Example: `None`  
- Python allows **dynamic typing**, **variable reassignment**, **multiple assignments**, and **swapping variables easily**.
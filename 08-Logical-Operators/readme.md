
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

# Logical Operators: `and`, `or`, `not`

Logical operators are used to combine multiple **conditions** in boolean expressions. These operators return either **True** or **False** based on the given conditions.

---

## **1. Logical AND (`and`)**  
- The `and` operator returns **True** only if **both** conditions are `True`.  
- If at least **one** condition is `False`, it returns `False`.  

### **Example with Boolean values:**
```python
a = True
b = False

result_and = a and b  # Since 'b' is False, the result will be False.
print("Logical AND (True and False):", result_and)  # Output: False
```

### **Example with numeric comparisons:**
```python
x = 10
y = 5

print(x > 5 and y < 10)   # True and True → Output: True
print(x > 15 and y < 10)  # False and True → Output: False
```

---

## **2. Logical OR (`or`)**  
- The `or` operator returns **True** if **at least one** condition is `True`.  
- It returns `False` **only** if **both** conditions are `False`.  

### **Example with Boolean values:**
```python
c = True
d = False

result_or = c or d  # Since 'c' is True, the result will be True.
print("Logical OR (True or False):", result_or)  # Output: True
```

### **Example with numeric comparisons:**
```python
x = 10
y = 5

print(x > 15 or y < 10)  # False or True → Output: True
print(x > 15 or y > 10)  # False or False → Output: False
```

---

## **3. Logical NOT (`not`)**  
- The `not` operator **negates** (reverses) the boolean value.  
- If the condition is `True`, `not` makes it `False`, and vice versa.  

### **Example with Boolean values:**
```python
e = True
result_not = not e  # 'not' will invert True to False.
print("Logical NOT (not True):", result_not)  # Output: False
```

### **Example with numeric comparisons:**
```python
x = 10

print(not (x > 5))  # True → False
print(not (x < 5))  # False → True
```

---

## **4. Short-Circuit Evaluation**  
Python **stops evaluating** conditions as soon as the result is known.  

### **Example of short-circuiting in `and`:**
```python
def check_and():
    print("Checking second condition...")
    return True  # This line executes only if the first condition is True.

print(False and check_and())  # Function is never called, output is False.
```

### **Example of short-circuiting in `or`:**
```python
def check_or():
    print("Checking second condition...")
    return True  # This line executes only if the first condition is False.

print(True or check_or())  # Function is never called, output is True.
```

---

## **5. Using Logical Operators in Conditional Statements**  

### **Example with `and`:**
```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("You are allowed to enter.")
else:
    print("Access denied.")
```

### **Example with `or`:**
```python
is_student = False
has_discount_code = True

if is_student or has_discount_code:
    print("You get a discount!")
else:
    print("No discount available.")
```

---

## **6. Using Logical Operators with Lists and Strings**  

### **Using `and` with lists:**  
- `and` returns the second operand if the first one is **True** (non-empty).  
- If the first operand is **False** (empty list), it returns the first operand.

```python
list1 = [1, 2, 3]
list2 = []

print(list1 and "Hello")  # Output: "Hello"
print(list2 and "Hello")  # Output: []
```

### **Using `or` with lists:**  
- `or` returns the first **True** (non-empty) operand.  
- If the first operand is **False** (empty list), it returns the second operand.

```python
print(list1 or "Default")  # Output: [1, 2, 3]
print(list2 or "Default")  # Output: "Default"
```

### **Using `not` with strings:**
```python
text = ""

print(not text)  # Empty string is False → not False → True

text = "Python"

print(not text)  # Non-empty string is True → not True → False
```

---

## **7. Using Logical Operators in List Comprehensions**  

### **Filtering even numbers using `and`:**
```python
numbers = [10, 15, 20, 25, 30]

even_numbers = [num for num in numbers if num % 2 == 0 and num > 15]
print(even_numbers)  # Output: [20, 30]
```

### **Filtering numbers using `or`:**
```python
filtered_numbers = [num for num in numbers if num < 15 or num > 25]
print(filtered_numbers)  # Output: [10, 30]
```

---

### **Truth Tables for Logical Operators in Python**  

Logical operators return **True** or **False** based on the conditions provided. Below are the truth tables for `and`, `or`, and `not` operators.

---

### **1. Truth Table for `and` (Logical AND)**  
- The `and` operator returns `True` **only if both** conditions are `True`.  
- If at least **one** condition is `False`, it returns `False`.  

| A (Condition 1) | B (Condition 2) | A `and` B |
|-----------------|----------------|-----------|
| `False`        | `False`         | `False`   |
| `False`        | `True`          | `False`   |
| `True`         | `False`         | `False`   |
| `True`         | `True`          | `True`    |

**Example in Python:**
```python
print(False and False)  # Output: False
print(False and True)   # Output: False
print(True and False)   # Output: False
print(True and True)    # Output: True
```

---

### **2. Truth Table for `or` (Logical OR)**  
- The `or` operator returns `True` **if at least one** condition is `True`.  
- It returns `False` **only if both** conditions are `False`.  

| A (Condition 1) | B (Condition 2) | A `or` B |
|-----------------|----------------|----------|
| `False`        | `False`         | `False`  |
| `False`        | `True`          | `True`   |
| `True`         | `False`         | `True`   |
| `True`         | `True`          | `True`   |

**Example in Python:**
```python
print(False or False)  # Output: False
print(False or True)   # Output: True
print(True or False)   # Output: True
print(True or True)    # Output: True
```

---

### **3. Truth Table for `not` (Logical NOT)**  
- The `not` operator **reverses** the boolean value.  
- `not True` becomes `False`, and `not False` becomes `True`.  

| A (Condition) | `not` A |
|--------------|--------|
| `False`      | `True`  |
| `True`       | `False` |

**Example in Python:**
```python
print(not False)  # Output: True
print(not True)   # Output: False
```

---

### **4. Combined Logical Operators**
Logical operators can be combined to form complex conditions.

| A     | B     | C     | `(A and B) or C` |
|-------|-------|-------|------------------|
| False | False | False | `False`          |
| False | False | True  | `True`           |
| False | True  | False | `False`          |
| False | True  | True  | `True`           |
| True  | False | False | `False`          |
| True  | False | True  | `True`           |
| True  | True  | False | `True`           |
| True  | True  | True  | `True`           |

**Example in Python:**
```python
A, B, C = False, False, False
print((A and B) or C)  # Output: False

A, B, C = False, False, True
print((A and B) or C)  # Output: True

A, B, C = True, True, False
print((A and B) or C)  # Output: True
```

---

### **Key Takeaways**
1. **`and`** returns `True` only if **both** conditions are `True`, otherwise `False`.
2. **`or`** returns `True` if **at least one** condition is `True`, otherwise `False`.
3. **`not`** reverses the boolean value (`True → False`, `False → True`).
4. **Short-circuiting**:
   - In `and`, if the first condition is `False`, Python **stops** checking further conditions.
   - In `or`, if the first condition is `True`, Python **stops** checking further conditions.

These logical operators are fundamental in **decision-making** and **conditional statements** in Python.

---

# **Summary of Logical Operators**  

| Operator | Description | Example |
|----------|------------|---------|
| `and` | Returns `True` if **both** conditions are `True`, otherwise `False` | `True and False → False` |
| `or` | Returns `True` if **at least one** condition is `True`, otherwise `False` | `True or False → True` |
| `not` | Reverses the boolean value (`True` → `False`, `False` → `True`) | `not True → False` |
| **Short-circuiting** | `and`: Stops at `False` <br> `or`: Stops at `True` | `False and func() → func() never runs` |

Logical operators are essential for controlling the flow of programs and making decisions based on conditions.

![Static Badge](https://img.shields.io/badge/Aditya%20Kumar-black?style=for-the-badge&logo=atlasos&logoColor=%23ffffff)
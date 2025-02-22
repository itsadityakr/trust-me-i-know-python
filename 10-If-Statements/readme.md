
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

# `if` Statements

Conditional statements in Python allow the program to make **decisions** based on conditions. The `if` statement executes a block of code **only if a specified condition is met**.

---

## **1. Basic if Statement**  
The `if` statement **executes code only when the condition is `True`**.  

### **Syntax:**  
```python
if condition:
    statement(s)  # Executes only if the condition is True
```

### **Example:**
```python
x = 10
if x > 5:  # Checks if x is greater than 5
    print("x is greater than 5")  # This line executes
```
**Output:**  
```
x is greater than 5
```

---

## **2. if-else Statement**  
The `else` block executes when the `if` condition is **False**.  

### **Syntax:**  
```python
if condition:
    statement(s)  # Executes if True
else:
    statement(s)  # Executes if False
```

### **Example:**
```python
y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is 5 or less")  # Executes because y = 3
```
**Output:**  
```
y is 5 or less
```

---

## **3. if-elif-else Statement**  
Used when checking **multiple conditions**.  

### **Syntax:**  
```python
if condition1:
    statement(s)
elif condition2:
    statement(s)
else:
    statement(s)  # Executes if no conditions are True
```

### **Example:**
```python
z = 0
if z > 0:
    print("z is positive")
elif z < 0:
    print("z is negative")
else:
    print("z is zero")  # Executes because z = 0
```
✅ **Output:**  
```
z is zero
```

---

## **4. Nested if Statements**  
You can place an `if` inside another `if` (Nested `if`).  

### **Example:**
```python
age = 20
if age >= 18:  # Outer if
    print("You are an adult")
    if age >= 65:  # Inner if
        print("You are also a senior citizen")
    else:
        print("You are not a senior citizen yet")
else:
    print("You are a minor")
```
**Output:**  
```
You are an adult
You are not a senior citizen yet
```

---

## **5. Logical Operators (`and`, `or`, `not`)**  
Logical operators allow combining multiple conditions.  

### **Example:**
```python
a = 7
b = 10

if a > 5 and b < 15:  # Both conditions must be True
    print("Both conditions are met")

if a > 10 or b < 15:  # At least one condition must be True
    print("At least one condition is met")

if not (a < 5):  # The 'not' operator negates the condition
    print("a is not less than 5")
```
**Output:**  
```
Both conditions are met
At least one condition is met
a is not less than 5
```

---

## **6. Comparison Operators in if Statements**  
Comparison operators are used in `if` statements to compare values.  

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>`  | Greater than |
| `<`  | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

### **Example:**
```python
num = 10

if num == 10:
    print("num is exactly 10")

if num != 5:
    print("num is not 5")

if num >= 10:
    print("num is at least 10")
```
**Output:**  
```
num is exactly 10
num is not 5
num is at least 10
```

---

## **7. Membership Operators (`in`, `not in`)**  
Used to check if a value exists in a **sequence** (like a list, tuple, or string).  

### **Example:**
```python
fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("Banana is in the list")

if "grape" not in fruits:
    print("Grape is not in the list")
```
**Output:**  
```
Banana is in the list
Grape is not in the list
```

---

## **8. Ternary (Short-hand) if Statement**  
A compact way to write an `if-else` statement in a **single line**.  

### **Syntax:**  
```python
variable = value_if_true if condition else value_if_false
```

### **Example:**
```python
n = 7
result = "Even" if n % 2 == 0 else "Odd"  # Compact if-else
print(result)
```
**Output:**  
```
Odd
```

---

## **9. Checking Truthy and Falsy Values**  
- `0`, `None`, `""` (empty string), `[]` (empty list), `{}` (empty dictionary) are **Falsy**.
- Any other value is **Truthy**.

### **Example:**
```python
m = 0  # 0 is considered False

if m:  
    print(True)
else:
    print(False)
```
**Output:**  
```
False
```

---

# **Summary Table**  

| Concept | Syntax | Example |
|---------|--------|---------|
| **Basic if** | `if condition:` | `if x > 5:` |
| **if-else** | `if condition: else:` | `if x > 5: print("Yes") else: print("No")` |
| **if-elif-else** | `if condition1: elif condition2: else:` | `if x > 0: print("Positive") elif x < 0: print("Negative") else: print("Zero")` |
| **Nested if** | `if condition: if condition:` | `if age >= 18: if age >= 65: print("Senior")` |
| **Logical Operators** | `if A and B:` | `if x > 5 and y < 10:` |
| **Comparison Operators** | `if x == y:` | `if num != 5:` |
| **Membership Operators** | `if "a" in "apple":` | `if "banana" in fruits:` |
| **Ternary if** | `variable = val1 if condition else val2` | `result = "Even" if n % 2 == 0 else "Odd"` |

---

With these **if statement** concepts, you can create **dynamic and conditional logic** in Python!

![Static Badge](https://img.shields.io/badge/Aditya%20Kumar-black?style=for-the-badge&logo=atlasos&logoColor=%23ffffff)
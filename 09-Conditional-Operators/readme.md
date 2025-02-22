
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

# Conditional Operators

Conditional operators (also called comparison operators) are used to compare values. They return a boolean result: either `True` or `False`.

## **List of Conditional Operators:**
1. **Equal to (`==`)**  
2. **Not equal to (`!=`)**  
3. **Greater than (`>`)**  
4. **Less than (`<`)**  
5. **Greater than or equal to (`>=`)**  
6. **Less than or equal to (`<=`)**  

---

## **1. Equal to (`==`)**  

The `==` operator checks if two values are equal.

```python
a = 10
b = 20

# Checking if 'a' is equal to 'b'
print(a == b)  # Output: False

# Checking if 'a' is equal to 10
print(a == 10)  # Output: True
```

---

## **2. Not Equal to (`!=`)**  

The `!=` operator checks if two values are **not** equal.

```python
x = 5
y = 5

# Since both values are equal, the result is False
print(x != y)  # Output: False

# Since 'x' is different from 10, the result is True
print(x != 10)  # Output: True
```

---

## **3. Greater Than (`>`)**  

The `>` operator checks if the left value is greater than the right value.

```python
num1 = 15
num2 = 10

# Since num1 is greater than num2, the result is True
print(num1 > num2)  # Output: True

# Since num2 is not greater than num1, the result is False
print(num2 > num1)  # Output: False
```

---

## **4. Less Than (`<`)**  

The `<` operator checks if the left value is smaller than the right value.

```python
age1 = 18
age2 = 21

# Since 18 is less than 21, the result is True
print(age1 < age2)  # Output: True

# Since 21 is not less than 18, the result is False
print(age2 < age1)  # Output: False
```

---

## **5. Greater Than or Equal To (`>=`)**  

The `>=` operator checks if the left value is greater than or equal to the right value.

```python
score1 = 90
score2 = 90

# Since both values are equal, the result is True
print(score1 >= score2)  # Output: True

# Since score1 is greater, the result is also True
print(95 >= score2)  # Output: True

# Since 85 is not greater than 90, the result is False
print(85 >= score2)  # Output: False
```

---

## **6. Less Than or Equal To (`<=`)**  

The `<=` operator checks if the left value is smaller than or equal to the right value.

```python
price1 = 100
price2 = 120

# Since 100 is less than 120, the result is True
print(price1 <= price2)  # Output: True

# Since both values are equal, the result is True
print(price1 <= 100)  # Output: True

# Since 150 is greater than 120, the result is False
print(150 <= price2)  # Output: False
```

---

## **Using Conditional Operators in If-Else Statements**  

### **Example 1: Checking Temperature**
```python
temperature = 30

if temperature > 35:
    print("It's a hot day.")
else:
    print("It's not too hot.")
```

### **Example 2: Checking Voting Eligibility**
```python
age = 17

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

---

## **Using Conditional Operators with Strings**  

```python
name1 = "Alice"
name2 = "Bob"

# Comparing if two strings are equal
print(name1 == "Alice")  # Output: True

# Checking if two names are different
print(name1 != name2)  # Output: True
```

---

## **Using Conditional Operators in List Comparisons**  

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [4, 5, 6]

# Checking if two lists are equal
print(list1 == list2)  # Output: True

# Checking if two lists are different
print(list1 != list3)  # Output: True
```

---

## **Truth Table for Conditional Operators**  

| Expression       | Condition | Output |
|-----------------|------------|--------|
| `10 == 10`     | True       | `True` |
| `10 == 20`     | False      | `False` |
| `10 != 20`     | True       | `True` |
| `10 != 10`     | False      | `False` |
| `15 > 10`      | True       | `True` |
| `10 > 15`      | False      | `False` |
| `10 < 15`      | True       | `True` |
| `15 < 10`      | False      | `False` |
| `20 >= 20`     | True       | `True` |
| `25 >= 20`     | True       | `True` |
| `10 >= 20`     | False      | `False` |
| `10 <= 20`     | True       | `True` |
| `20 <= 20`     | True       | `True` |
| `25 <= 20`     | False      | `False` |

---

## **Summary of Conditional Operators**  

| Operator | Description |
|----------|-------------|
| `==`     | Returns `True` if both values are equal |
| `!=`     | Returns `True` if values are not equal |
| `>`      | Returns `True` if the left value is greater than the right value |
| `<`      | Returns `True` if the left value is less than the right value |
| `>=`     | Returns `True` if the left value is greater than or equal to the right value |
| `<=`     | Returns `True` if the left value is less than or equal to the right value |

Conditional operators are commonly used in **if-else statements, loops, and filtering data**.

![Static Badge](https://img.shields.io/badge/Aditya%20Kumar-black?style=for-the-badge&logo=atlasos&logoColor=%23ffffff)
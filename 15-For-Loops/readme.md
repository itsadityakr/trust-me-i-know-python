
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

# For Loop

## **What is a For Loop?**  
- A `for` loop is used to iterate over sequences such as lists, tuples, strings, and dictionaries.  
- It executes a block of code for each item in the sequence.  
- The loop automatically stops when all items are processed.  

### **Syntax:**  
```python
for variable in sequence:
    # Code to execute
```

---

## **1. Basic For Loop**  

```python
print("Basic for loop:")

for i in range(5):  # Loops from 0 to 4
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4
```

---

## **2. Using For Loop with Lists**  

```python
fruits = ["apple", "banana", "cherry"]
print("Looping through a list:")

for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry
```

---

## **3. Using For Loop with Strings**  

```python
print("Looping through a string:")

word = "Python"
for letter in word:
    print(letter)

# Output:
# P
# y
# t
# h
# o
# n
```

---

## **4. Using For Loop with `range()`**  
- The `range()` function generates a sequence of numbers.  

```python
print("Using range:")

for num in range(2, 10, 2):  # Start at 2, end at 10 (excluded), step by 2
    print(num)

# Output:
# 2
# 4
# 6
# 8
```

---

## **5. Using `break` in a For Loop**  
- `break` exits the loop immediately.  

```python
print("Using break:")

for num in range(10):
    if num == 5:
        break  # Stop the loop when num is 5
    print(num)

# Output:
# 0
# 1
# 2
# 3
# 4
```

---

## **6. Using `continue` in a For Loop**  
- `continue` skips the rest of the code for the current iteration and moves to the next one.  

```python
print("Using continue:")

for num in range(5):
    if num == 2:
        continue  # Skip number 2
    print(num)

# Output:
# 0
# 1
# 3
# 4
```

---

## **7. Using `else` with For Loop**  
- The `else` block runs if the loop completes normally (without `break`).  

```python
print("Using else:")

for num in range(3):
    print(num)
else:
    print("Loop completed!")  # Runs when loop exits normally

# Output:
# 0
# 1
# 2
# Loop completed!
```

---

## **8. Nested For Loops**  
- A for loop inside another for loop.  

```python
print("Nested for loop:")

for i in range(1, 4):  # Outer loop
    for j in range(1, 3):  # Inner loop
        print(f"i={i}, j={j}")

# Output:
# i=1, j=1
# i=1, j=2
# i=2, j=1
# i=2, j=2
# i=3, j=1
# i=3, j=2
```

---

## **9. Looping Through a Dictionary**  

```python
student = {"name": "Alice", "age": 25, "grade": "A"}
print("Looping through a dictionary (keys and values):")

for key, value in student.items():
    print(f"{key}: {value}")

# Output:
# name: Alice
# age: 25
# grade: A
```

---

## **10. Looping with `enumerate()`**  
- `enumerate()` provides an index along with the item.  

```python
print("Using enumerate:")

colors = ["red", "blue", "green"]
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

# Output:
# Index 0: red
# Index 1: blue
# Index 2: green
```

---

## **11. Using List Comprehension in For Loop**  
- A concise way to create lists using for loops.  

```python
print("List comprehension:")

numbers = [x**2 for x in range(5)]  # Square numbers from 0 to 4
print(numbers)

# Output:
# [0, 1, 4, 9, 16]
```

---

## **12. Looping with `zip()`**  
- `zip()` combines multiple lists and loops through them simultaneously.  

```python
names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 88]
print("Using zip:")

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# Output:
# Alice scored 90
# Bob scored 85
# Charlie scored 88
```

---

## **13. Common Mistakes in For Loops**  

### **1. Forgetting to Iterate Over a Sequence**  
Using a for loop without a proper sequence leads to errors.  

```python
for i in 5:  # Incorrect: 5 is not an iterable
    print(i)
```

---

### **2. Modifying a List While Iterating**  
Changing a list while iterating over it can cause unexpected behavior.  

```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # This causes skipping elements
print(numbers)  # Unexpected output
```

A better way is to use list comprehension:  

```python
numbers = [num for num in numbers if num % 2 != 0]
print(numbers)  # Correct output
```

---

### **3. Using `break` Without an Exit Condition**  
Using `break` inside a loop without a condition can make the loop unpredictable.  

```python
for num in range(10):
    break  # This exits immediately, making the loop pointless
```

---

## **Summary of For Loops**  

### **Basic Concepts**  
- **Basic for loop:** Iterates over a sequence.  
- **Lists & Strings:** Iterate through elements/characters.  
- **`range()`:** Generates sequences of numbers.  
- **`break`:** Stops the loop immediately.  
- **`continue`:** Skips the current iteration and moves to the next.  
- **`else`:** Runs if the loop exits normally.  

### **Common Use Cases**  
- **Nested loops:** Loops inside loops.  
- **Dictionaries:** Iterate through key-value pairs.  
- **`enumerate()`:** Get index along with value.  
- **List comprehension:** Compact list creation.  
- **`zip()`:** Iterate over multiple sequences.  

---

## **Conclusion**  
For loops are a powerful tool for iterating over sequences and performing repetitive tasks efficiently. By understanding concepts like `break`, `continue`, `else`, and list comprehension, you can write cleaner and more efficient Python code.

![Static Badge](https://img.shields.io/badge/Aditya%20Kumar-black?style=for-the-badge&logo=atlasos&logoColor=%23ffffff)
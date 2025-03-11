![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

# **2D Collections in Python: List, Set, and Tuple**  

This document explains different types of **2D collections** in Python with detailed explanations, examples, and expected outputs.  

## **Overview of 2D Collections**  

Python supports **multi-dimensional collections** where each element in the outer collection is itself a collection. Some common types include:  

1. **List of Lists** → Mutable, Ordered  
2. **Set of Frozensets** → Immutable, Unordered, Unique rows only  
3. **Tuple of Tuples** → Immutable, Ordered  

Each type has unique properties, advantages, and use cases.  

---

## **1. List of Lists (Mutable & Ordered)**  

A **list of lists** is the most commonly used **2D collection**.  
- **Ordered** → The elements maintain their sequence.  
- **Mutable** → We can modify elements.  
- **Allows Duplicates** → Duplicate rows and values are allowed.  

### **Example: Creating a 2D List**  

```python
matrix_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

---

### **Accessing Elements in a 2D List**  

We can access individual elements using **row and column indices**.

```python
element = matrix_list[1][2]  # Access row index 1, column index 2
print("Accessed Element:", element)
```

#### **Expected Output:**  
```
Accessed Element: 6
```

---

### **Accessing a Complete Row**  

We can extract an entire row from the **2D list**.

```python
row = matrix_list[1]  # Access row index 1
print("Accessed Row:", row)
```

#### **Expected Output:**  
```
Accessed Row: [4, 5, 6]
```

---

### **Modifying an Element in a 2D List**  

Since lists are **mutable**, we can modify their elements.

```python
matrix_list[1][2] = 99  # Change 6 to 99

# Printing the modified list
print("Modified List of Lists:")
for row in matrix_list:
    print(row)
```

#### **Expected Output:**  
```
Modified List of Lists:
[1, 2, 3]
[4, 5, 99]
[7, 8, 9]
```

---

### **Iterating Through a 2D List**  

We can **loop through rows and columns** to access elements.

```python
print("Iterating through List of Lists:")
for row in matrix_list:
    for value in row:
        print(value, end=" ")
    print()  # New line after each row
```

#### **Expected Output:**  
```
1 2 3
4 5 99
7 8 9
```

---

## **2. Set of Frozensets (Immutable & Unordered, Unique Rows Only)**  

A **set of frozensets** is used to store **unique** 2D collections.  
- **Unordered** → The order of rows is **not preserved**.  
- **Immutable** → Rows (frozensets) cannot be modified.  
- **No Duplicates** → Duplicate rows are **automatically removed**.  

---

### **Example: Creating a Set of Frozensets**  

```python
matrix_set = {
    frozenset([1, 2, 3]),
    frozenset([4, 5, 6]),
    frozenset([7, 8, 9]),
    frozenset([1, 2, 3])  # Duplicate row (will be ignored)
}
```

---

### **Printing a Set of Frozensets**  

```python
print("Set of Frozensets (Unique Rows Only):")
print(matrix_set)
```

#### **Expected Output (Order May Vary):**  
```
Set of Frozensets (Unique Rows Only):
{frozenset({1, 2, 3}), frozenset({4, 5, 6}), frozenset({7, 8, 9})}
```

---

### **Checking if a Row Exists in the Set**  

```python
row_check = frozenset([1, 2, 3]) in matrix_set
print("Is [1,2,3] in matrix_set?:", row_check)
```

#### **Expected Output:**  
```
Is [1,2,3] in matrix_set?: True
```

---

## **3. Tuple of Tuples (Immutable & Ordered)**  

A **tuple of tuples** is used for **fixed, read-only** 2D collections.  
- **Ordered** → The sequence of rows is preserved.  
- **Immutable** → Cannot be modified after creation.  
- **Allows Duplicates** → Duplicate rows are allowed.  

---

### **Example: Creating a Tuple of Tuples**  

```python
matrix_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
```

---

### **Printing a Tuple of Tuples**  

```python
print("Tuple of Tuples:")
for row in matrix_tuple:
    print(row)
```

#### **Expected Output:**  
```
(1, 2, 3)
(4, 5, 6)
(7, 8, 9)
```

---

### **Accessing an Element from a Tuple of Tuples**  

```python
tuple_element = matrix_tuple[1][2]
print("Accessed Element from Tuple:", tuple_element)
```

#### **Expected Output:**  
```
Accessed Element from Tuple: 6
```

---

### **Iterating Through a Tuple of Tuples**  

```python
print("Iterating through Tuple of Tuples:")
for row in matrix_tuple:
    for value in row:
        print(value, end=" ")
    print()  # New line after each row
```

#### **Expected Output:**  
```
1 2 3
4 5 6
7 8 9
```

---

## **Comparison of 2D Collections**  

| Feature                | List of Lists            | Set of Frozensets            | Tuple of Tuples            |
|------------------------|-------------------------|------------------------------|-----------------------------|
| **Mutability**        | Mutable                 | Immutable                     | Immutable                    |
| **Order Preserved**   | Yes                     | No (unordered)                | Yes                         |
| **Duplicates Allowed**| Yes                     | No (only unique rows)         | Yes                         |
| **Modification**      | Allowed                 | Not Allowed                   | Not Allowed                 |
| **Best Use Case**     | When frequent updates are needed | When only unique data is required | When data must remain unchanged |

---

## **Final Thoughts**  

### **When to Use Which?**  
- **Use `list of lists`** if you need a flexible, ordered, and **modifiable** structure.  
- **Use `set of frozensets`** if you need **unique** rows and don’t care about order.  
- **Use `tuple of tuples`** if your data **should never change** and order is important.  

---

![Static Badge](https://img.shields.io/badge/Aditya%20Kumar-black?style=for-the-badge&logo=atlasos&logoColor=%23ffffff)
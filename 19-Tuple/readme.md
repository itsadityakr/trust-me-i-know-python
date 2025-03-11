![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

# Python Tuple

A **tuple** is an **ordered**, **immutable** collection of elements. Tuples are similar to lists, but once created, they **cannot be modified**.

## Creating a Tuple
Tuples are defined using **parentheses** `()` or the `tuple()` constructor.
```python
numsTuple = (1, 2, 3, 4, 5)
```

## Tuple Methods
### 1. `count(x)`: Returns the number of times `x` appears in the tuple
```python
count_of_2 = numsTuple.count(2)
# Output: 1
```

### 2. `index(x, [start, end])`: Returns the index of the first occurrence of `x`
```python
index_of_4 = numsTuple.index(4)
# Output: 3
```

## Tuple Operations
### 3. `len()`: Returns the number of elements in the tuple
```python
length = len(numsTuple)
# Output: 5
```

### 4. `max()`: Returns the maximum element in the tuple
```python
maximum = max(numsTuple)
# Output: 5
```

### 5. `min()`: Returns the minimum element in the tuple
```python
minimum = min(numsTuple)
# Output: 1
```

### 6. `sum()`: Returns the sum of all numeric elements in the tuple
```python
total = sum(numsTuple)
# Output: 15
```

### 7. `sorted()`: Returns a sorted list of the tuple’s elements
```python
sorted_tuple = sorted(numsTuple)
# Output: [1, 2, 3, 4, 5]
```

### 8. Tuple Concatenation: Merging Two Tuples
```python
tuple_a = (10, 20, 30)
tuple_b = (40, 50)
concatenated_tuple = tuple_a + tuple_b
# Output: (10, 20, 30, 40, 50)
```

### 9. Tuple Repetition: Repeating Elements in a Tuple
```python
repeated_tuple = tuple_a * 2
# Output: (10, 20, 30, 10, 20, 30)
```

### 10. Membership Test: Checking if an Element Exists in a Tuple
```python
is_present = 3 in numsTuple
# Output: True
```

### 11. Tuple Unpacking: Assigning Tuple Elements to Variables
```python
a, b, c, d, e = numsTuple
# a = 1, b = 2, c = 3, d = 4, e = 5
```

### 12. Nested Tuples: Tuples Inside Tuples
```python
nested_tuple = ((1, 2, 3), (4, 5, 6))
# Output: ((1, 2, 3), (4, 5, 6))
```

### 13. Converting List to Tuple Using `tuple()` Constructor
```python
list_to_tuple = tuple([100, 200, 300])
# Output: (100, 200, 300)
```

### 14. Converting String to Tuple: Characters Become Tuple Elements
```python
string_to_tuple = tuple("hello")
# Output: ('h', 'e', 'l', 'l', 'o')
```

## Summary of Tuple Properties
- **Immutable**: Cannot modify after creation
- **Ordered**: Elements maintain order
- **Supports Indexing & Slicing**
- **Can Contain Mixed Data Types**
- **More Memory Efficient than Lists**

Tuples are useful when you need an immutable collection of elements, such as coordinates, database records, or configuration settings.



![Static Badge](https://img.shields.io/badge/Aditya%20Kumar-black?style=for-the-badge&logo=atlasos&logoColor=%23ffffff)
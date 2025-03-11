![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

# Python Lists

## What is a List?
A **list** in Python is a built-in data structure that allows you to store multiple values in a single variable. Lists are **ordered**, **mutable** (changeable), and allow **duplicate values**.

### Creating a List
You can create a list using square brackets `[]`:
```python
numsList = [1, 2, 3, 4, 5]
```

## List Methods
Python provides several built-in methods to manipulate lists. Below are some of the most commonly used list methods with examples:

### 1. `append(x)`
Adds an element to the end of the list.
```python
numsList.append(6)
# Output: [1, 2, 3, 4, 5, 6]
```

### 2. `extend(iterable)`
Extends the list by appending elements from another iterable.
```python
numsList.extend([7, 8, 9])
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 3. `insert(index, x)`
Inserts an element at a specified position.
```python
numsList.insert(2, 10)  # Inserts 10 at index 2
# Output: [1, 2, 10, 3, 4, 5, 6, 7, 8, 9]
```

### 4. `remove(x)`
Removes the first occurrence of a specified value.
```python
numsList.remove(10)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 5. `pop([index])`
Removes and returns the element at a given index (or the last element by default).
```python
removed_element = numsList.pop()
# Output: 9
```

### 6. `index(x, [start, end])`
Returns the index of the first occurrence of `x`.
```python
index_of_5 = numsList.index(5)
# Output: 4
```

### 7. `count(x)`
Returns the number of times `x` appears in the list.
```python
count_of_2 = numsList.count(2)
# Output: 1
```

### 8. `sort(key=None, reverse=False)`
Sorts the list in ascending order (modifies the list in place).
```python
numsList.sort()
# Output: [1, 2, 3, 4, 5, 6, 7, 8]
```

### 9. `reverse()`
Reverses the list in place.
```python
numsList.reverse()
# Output: [8, 7, 6, 5, 4, 3, 2, 1]
```

### 10. `copy()`
Returns a shallow copy of the list.
```python
copy_list = numsList.copy()
# Output: [8, 7, 6, 5, 4, 3, 2, 1]
```

### 11. `clear()`
Removes all elements from the list.
```python
numsList.clear()
# Output: []
```

## Non-Method List Operations
Apart from methods, Python provides functions that can operate on lists.

### 12. `len()`
Returns the number of elements in the list.
```python
length = len(copy_list)
# Output: 8
```

### 13. `max()`
Returns the maximum element in the list.
```python
maximum = max(copy_list)
# Output: 8
```

### 14. `min()`
Returns the minimum element in the list.
```python
minimum = min(copy_list)
# Output: 1
```

### 15. `sum()`
Returns the sum of all elements in the list.
```python
total = sum(copy_list)
# Output: 36
```

### 16. `sorted()`
Returns a new sorted list without modifying the original list.
```python
sorted_list = sorted(copy_list)
# Output: [1, 2, 3, 4, 5, 6, 7, 8]
```

### 17. List Comprehension
A concise way to create lists.
```python
squared_numbers = [x ** 2 for x in range(1, 6)]
# Output: [1, 4, 9, 16, 25]
```

## Summary
Lists in Python are versatile and powerful. They support a variety of methods to manipulate data efficiently. Understanding and using these methods will help you work with collections of data effectively in Python.

![Static Badge](https://img.shields.io/badge/Aditya%20Kumar-black?style=for-the-badge&logo=atlasos&logoColor=%23ffffff)
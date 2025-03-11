![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
# Index Slicing in Python

Index slicing is a powerful feature in Python that allows you to extract a portion of a sequence (like a list or tuple) by specifying a range of indices. The syntax for slicing is `[start:stop:step]`, where:

- `start`: The index where the slice begins (inclusive). If omitted, it defaults to `0`.
- `stop`: The index where the slice ends (exclusive). If omitted, it defaults to the end of the sequence.
- `step`: The step size (optional). If omitted, it defaults to `1`.

---

## Slicing in Lists

Lists are mutable sequences, and slicing works the same way as in tuples.

### Example 1: Basic Slicing
```python
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements from index 2 to 5 (exclusive)
slice1 = my_list[2:5]
print(slice1)  # Output: [2, 3, 4]
```

### Example 2: Omitting `start` or `stop`
```python
# Get elements from the start to index 5 (exclusive)
slice2 = my_list[:5]
print(slice2)  # Output: [0, 1, 2, 3, 4]

# Get elements from index 5 to the end
slice3 = my_list[5:]
print(slice3)  # Output: [5, 6, 7, 8, 9]
```

### Example 3: Using `step`
```python
# Get every second element
slice4 = my_list[::2]
print(slice4)  # Output: [0, 2, 4, 6, 8]
```

### Example 4: Reversing a List
```python
# Reverse the list
slice5 = my_list[::-1]
print(slice5)  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

### Example 5: Negative Indices
```python
# Get the last three elements
slice6 = my_list[-3:]
print(slice6)  # Output: [7, 8, 9]
```

---

## Slicing in Tuples

Tuples are immutable sequences, but slicing works the same way as in lists.

### Example 1: Basic Slicing
```python
my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Get elements from index 2 to 5 (exclusive)
slice1_tuple = my_tuple[2:5]
print(slice1_tuple)  # Output: (2, 3, 4)
```

### Example 2: Omitting `start` or `stop`
```python
# Get elements from the start to index 5 (exclusive)
slice2_tuple = my_tuple[:5]
print(slice2_tuple)  # Output: (0, 1, 2, 3, 4)

# Get elements from index 5 to the end
slice3_tuple = my_tuple[5:]
print(slice3_tuple)  # Output: (5, 6, 7, 8, 9)
```

### Example 3: Using `step`
```python
# Get every second element
slice4_tuple = my_tuple[::2]
print(slice4_tuple)  # Output: (0, 2, 4, 6, 8)
```

### Example 4: Reversing a Tuple
```python
# Reverse the tuple
slice5_tuple = my_tuple[::-1]
print(slice5_tuple)  # Output: (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
```

### Example 5: Negative Indices
```python
# Get the last three elements
slice6_tuple = my_tuple[-3:]
print(slice6_tuple)  # Output: (7, 8, 9)
```

---

## Key Points to Remember
1. Slicing returns a **new list or tuple** and does not modify the original.
2. Negative indices can be used to slice from the end. For example, `my_list[-3:]` returns the last three elements.
3. If the `start` or `stop` indices are out of bounds, Python will not raise an error but will adjust them to the nearest valid index.
4. The `step` value can be used to skip elements or reverse the sequence.

---

## Summary Table

| Syntax       | Description                                      | Example                     | Output                          |
|--------------|--------------------------------------------------|-----------------------------|---------------------------------|
| `[start:stop]` | Slice from `start` to `stop` (exclusive)         | `my_list[2:5]`              | `[2, 3, 4]`                     |
| `[:stop]`     | Slice from the start to `stop` (exclusive)       | `my_list[:5]`               | `[0, 1, 2, 3, 4]`               |
| `[start:]`     | Slice from `start` to the end                   | `my_list[5:]`               | `[5, 6, 7, 8, 9]`               |
| `[::step]`     | Slice with a step size                          | `my_list[::2]`              | `[0, 2, 4, 6, 8]`               |
| `[::-1]`       | Reverse the sequence                            | `my_list[::-1]`             | `[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]`|
| `[-start:]`    | Slice from the end using negative indices       | `my_list[-3:]`              | `[7, 8, 9]`                     |

---

![Static Badge](https://img.shields.io/badge/Aditya%20Kumar-black?style=for-the-badge&logo=atlasos&logoColor=%23ffffff)
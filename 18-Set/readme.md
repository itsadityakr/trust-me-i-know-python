![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

# Python Sets

## What is a Set?
A **set** in Python is an **unordered** collection of **unique** elements. Sets are defined using curly braces `{}` or the `set()` constructor.

### Creating a Set
```python
numsSet = {1, 2, 3, 4, 5}
```

## Set Methods
Python provides various built-in methods to manipulate sets.

### 1. `add(x)`
Adds an element to the set.
```python
numsSet.add(6)
# Output: {1, 2, 3, 4, 5, 6}
```

### 2. `update(iterable)`
Adds multiple elements to the set.
```python
numsSet.update([7, 8, 9])
# Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}
```

### 3. `remove(x)`
Removes an element from the set; raises `KeyError` if not found.
```python
numsSet.remove(4)
# Output: {1, 2, 3, 5, 6, 7, 8, 9}
```

### 4. `discard(x)`
Removes an element if present; does nothing if not found.
```python
numsSet.discard(10)  # No error even if 10 is not present
# Output: {1, 2, 3, 5, 6, 7, 8, 9}
```

### 5. `pop()`
Removes and returns a random element from the set.
```python
removed_element = numsSet.pop()
# Output: (random element removed)
```

### 6. `clear()`
Removes all elements from the set.
```python
numsSet.clear()
# Output: set()
```

## Set Operations
Python sets support mathematical operations like union, intersection, and difference.

```python
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
```

### 7. `union(set)`
Returns a new set with elements from both sets.
```python
union_set = set_a.union(set_b)
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
```

### 8. `intersection(set)`
Returns a new set with elements common to both sets.
```python
intersection_set = set_a.intersection(set_b)
# Output: {4, 5}
```

### 9. `difference(set)`
Returns a new set with elements in `set_a` but not in `set_b`.
```python
difference_set = set_a.difference(set_b)
# Output: {1, 2, 3}
```

### 10. `symmetric_difference(set)`
Returns a new set with elements in either set, but not both.
```python
symmetric_diff_set = set_a.symmetric_difference(set_b)
# Output: {1, 2, 3, 6, 7, 8}
```

### 11. `issubset(set)`
Checks if `set_a` is a subset of `set_b`.
```python
is_subset = {1, 2}.issubset(set_a)
# Output: True
```

### 12. `issuperset(set)`
Checks if `set_a` is a superset of `set_b`.
```python
is_superset = set_a.issuperset({2, 3})
# Output: True
```

### 13. `isdisjoint(set)`
Checks if two sets have no elements in common.
```python
is_disjoint = set_a.isdisjoint({6, 7})
# Output: True
```

## In-Place Modifications
Some methods modify the set directly.

### 14. `intersection_update(set)`
Keeps only elements found in both sets.
```python
set_a.intersection_update(set_b)
# Output: {4, 5}
```

### 15. `difference_update(set)`
Removes elements found in another set.
```python
set_a = {1, 2, 3, 4, 5}
set_a.difference_update(set_b)
# Output: {1, 2, 3}
```

### 16. `symmetric_difference_update(set)`
Updates the set with symmetric difference.
```python
set_a = {1, 2, 3, 4, 5}
set_a.symmetric_difference_update(set_b)
# Output: {1, 2, 3, 6, 7, 8}
```

## Frozen Set (Immutable Set)
A **frozen set** is an immutable version of a set.
```python
frozen = frozenset([1, 2, 3, 4, 5])
# frozen.add(6)  # This would raise an AttributeError
```

## Summary
Sets in Python are a powerful tool for handling unique collections of data and performing mathematical operations efficiently. Understanding these methods and operations will help you work effectively with sets.

![Static Badge](https://img.shields.io/badge/Aditya%20Kumar-black?style=for-the-badge&logo=atlasos&logoColor=%23ffffff)
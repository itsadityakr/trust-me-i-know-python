![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

# Dictionary

---
## **1. Creating a Dictionary (Empty and With Values)**
A dictionary in Python is an unordered, mutable collection of key-value pairs. You can create it using curly braces `{}` or the `dict()` function.

```python
dict1 = {}  # Creates an empty dictionary
dict2 = {"name": "Alice", "age": 25, "city": "New York"}  # Dictionary with values
```
- **Keys** must be unique and immutable (strings, numbers, or tuples).
- **Values** can be of any data type.

---

## **2. Accessing Values Using Keys**
Dictionaries allow accessing values using their keys.

```python
print(dict2["name"])  # Output: Alice
```
- **If a key is missing**, Python raises a `KeyError`.

To prevent errors, use the `.get()` method:

```python
print(dict2.get("age"))  # Output: 25
print(dict2.get("country", "Not Found"))  # Output: Not Found
```
- `.get(key, default)` returns `default` if the key does not exist.

---

## **3. Adding and Updating Values**
Dictionaries are mutable, allowing you to add or update key-value pairs.

```python
dict2["country"] = "USA"  # Adding a new key-value pair
dict2["age"] = 26  # Updating an existing value
print(dict2)  # {'name': 'Alice', 'age': 26, 'city': 'New York', 'country': 'USA'}
```
- If a key already exists, the value is updated.
- If a key does not exist, a new key-value pair is added.

---

## **4. Removing Elements**
Dictionaries provide multiple ways to remove elements:

```python
# pop() removes a key and returns its value
removed_value = dict2.pop("city")
print(removed_value)  # Output: New York
print(dict2)  # {'name': 'Alice', 'age': 26, 'country': 'USA'}

# del removes a key completely
del dict2["country"]
print(dict2)  # {'name': 'Alice', 'age': 26}

# clear() removes all elements
dict2.clear()
print(dict2)  # Output: {}
```
- `pop(key)` returns the removed value.
- `del dict[key]` permanently deletes a key.
- `clear()` empties the dictionary.

---

## **5. Dictionary Methods**
Python provides built-in dictionary methods for efficient operations.

```python
dict3 = {"name": "Alice", "age": 25, "city": "New York"}

print(dict3.keys())    # dict_keys(['name', 'age', 'city'])
print(dict3.values())  # dict_values(['Alice', 25, 'New York'])
print(dict3.items())   # dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

# update() merges dictionaries
dict3.update({"age": 26, "country": "USA"})
print(dict3)  # {'name': 'Alice', 'age': 26, 'city': 'New York', 'country': 'USA'}
```
- `.keys()`, `.values()`, and `.items()` return iterable views of the dictionary.
- `.update(other_dict)` adds or updates values from another dictionary.

---

## **6. Looping Through a Dictionary**
Iterate through dictionary keys and values:

```python
for key in dict3:
    print(key, dict3[key])  # Prints each key and value

for key, value in dict3.items():
    print(f"{key}: {value}")  # Prints key-value pairs
```
- Looping directly over `dict` gives keys.
- Using `.items()` retrieves key-value pairs.

---

## **7. Dictionary Comprehension**
Create dictionaries dynamically using comprehension.

```python
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```
- `{key_expression: value_expression for item in iterable}` creates a dictionary efficiently.

---

## **8. Nested Dictionary**
Dictionaries can hold other dictionaries.

```python
students = {
    "Alice": {"age": 20, "grade": "A", "subjects": ["Math", "Science"]},
    "Bob": {"age": 22, "grade": "B", "subjects": ["English", "History"]}
}
print(students["Alice"]["grade"])  # Output: A
print(students["Bob"]["subjects"])  # Output: ['English', 'History']
```
- Access nested data using multiple keys.

---

## **9. Dictionary Length**
Find the number of key-value pairs.

```python
print(len(dict3))  # Output: 4
```
- `len(dictionary)` returns the count of keys.

---

## **10. Sorting Dictionary Keys**
Retrieve sorted keys.

```python
print(sorted(dict3))  # ['age', 'city', 'country', 'name']
```
- `sorted(dictionary)` returns a sorted list of keys.

---

## **11. Checking if a Key Exists**
Verify the presence of a key.

```python
if "name" in dict3:
    print("Key 'name' exists in the dictionary")
```
- The `in` operator checks for key existence.

---

## **12. Copying a Dictionary**
Make a copy without affecting the original.

```python
copy_dict = dict3.copy()
print(copy_dict)  # {'name': 'Alice', 'age': 26, 'city': 'New York', 'country': 'USA'}
```
- `copy()` creates a shallow copy (nested structures still reference original data).

---

## **13. Merging Dictionaries**
Combine multiple dictionaries.

```python
dict_a = {"x": 1, "y": 2}
dict_b = {"y": 3, "z": 4}
merged_dict = {**dict_a, **dict_b}
print(merged_dict)  # {'x': 1, 'y': 3, 'z': 4}
```
- The `**` operator (Python 3.5+) merges dictionaries.
- If keys overlap, later values overwrite earlier ones.

---

## **14. Default Values with `setdefault()`**
Ensure a key exists with a default value.

```python
def_dict = {"fruit": "Apple"}
def_dict.setdefault("color", "Red")
print(def_dict)  # {'fruit': 'Apple', 'color': 'Red'}
```
- `setdefault(key, default)` adds a key if missing and returns its value.

---



![Static Badge](https://img.shields.io/badge/Aditya%20Kumar-black?style=for-the-badge&logo=atlasos&logoColor=%23ffffff)
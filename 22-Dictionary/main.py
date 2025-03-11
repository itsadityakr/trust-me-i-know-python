# Python Dictionary Explained (In-Depth)

# 1. Creating a dictionary (empty and with values)
dict1 = {}  # Empty dictionary
dict2 = {"name": "Alice", "age": 25, "city": "New York"}  # Dictionary with values

# 2. Accessing values using keys
# Accessing a value using its key
print(dict2["name"])  # Output: Alice

# Using get() method to avoid KeyError
print(dict2.get("age"))  # Output: 25
print(dict2.get("country", "Not Found"))  # Output: Not Found (default value if key is missing)

# 3. Adding and updating values
# Adding a new key-value pair
dict2["country"] = "USA"

# Updating an existing key-value pair
dict2["age"] = 26
print(dict2)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'country': 'USA'}

# 4. Removing elements
# pop() removes a key and returns its value
removed_value = dict2.pop("city")
print(removed_value)  # Output: New York

# del removes a key completely
del dict2["country"]
print(dict2)  # Output: {'name': 'Alice', 'age': 26}

# clear() removes all elements from the dictionary
dict2.clear()
print(dict2)  # Output: {}

# 5. Dictionary methods
dict3 = {"name": "Alice", "age": 25, "city": "New York"}

# keys() returns all dictionary keys
print(dict3.keys())  # Output: dict_keys(['name', 'age', 'city'])

# values() returns all values
print(dict3.values())  # Output: dict_values(['Alice', 25, 'New York'])

# items() returns all key-value pairs as tuples
print(dict3.items())  # Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

# update() merges two dictionaries
dict3.update({"age": 26, "country": "USA"})
print(dict3)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'country': 'USA'}

# 6. Looping through a dictionary
# Looping through keys
for key in dict3:
    print(key, dict3[key])  # Prints each key and corresponding value

# Looping through key-value pairs
for key, value in dict3.items():
    print(f"{key}: {value}")

# 7. Dictionary comprehension
# Creating a dictionary where keys are numbers and values are their squares
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 8. Nested dictionary
students = {
    "Alice": {"age": 20, "grade": "A", "subjects": ["Math", "Science"]},
    "Bob": {"age": 22, "grade": "B", "subjects": ["English", "History"]}
}
print(students["Alice"]["grade"])  # Output: A
print(students["Bob"]["subjects"])  # Output: ['English', 'History']

# 9. Dictionary length
print(len(dict3))  # Output: 4 (number of key-value pairs)

# 10. Sorting dictionary keys
print(sorted(dict3))  # Output: ['age', 'city', 'country', 'name'] (sorted list of keys)

# 11. Checking if a key exists
if "name" in dict3:
    print("Key 'name' exists in the dictionary")  # Output: Key 'name' exists in the dictionary

# 12. Copying a dictionary
# Using copy() to create a duplicate
copy_dict = dict3.copy()
print(copy_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'country': 'USA'}

# 13. Merging dictionaries
# Using the ** operator (Python 3.5+)
dict_a = {"x": 1, "y": 2}
dict_b = {"y": 3, "z": 4}
merged_dict = {**dict_a, **dict_b}  # If keys overlap, the last dictionary's value is used
print(merged_dict)  # Output: {'x': 1, 'y': 3, 'z': 4}

# 14. Default values with setdefault()
def_dict = {"fruit": "Apple"}
def_dict.setdefault("color", "Red")
print(def_dict)  # Output: {'fruit': 'Apple', 'color': 'Red'}

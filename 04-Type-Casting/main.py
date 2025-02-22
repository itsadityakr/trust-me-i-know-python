# Type Casting (Type Conversion) in Python
# Python allows converting one data type to another using built-in functions: str(), int(), float(), bool()

# Defining variables of different data types
name_blank = ""  # Empty string
name = "Aditya"  # Non-empty string
age = 25  # Integer
cgpa = 7.6  # Float
is_human = True  # Boolean

# Type Casting Demonstrations

# Converting an empty string to a boolean
print(bool(name_blank))  # False (empty string is considered False)

# Converting a non-empty string to a boolean
print(bool(name))  # True (non-empty strings are considered True)

# Converting an integer to a string
print(str(age))  # Output: '25' (Integer converted to string)

# Converting a boolean to a string
print(str(is_human))  # Output: 'True' (Boolean converted to string)

# Converting an integer to a float
print(float(age))  # Output: 25.0 (Integer converted to float)

# Converting a float to an integer (removes decimal part, does not round)
print(int(cgpa))  # Output: 7 (Decimal part is truncated)

# Converting a boolean to an integer (True -> 1, False -> 0)
print(int(is_human))  # Output: 1 (True is equivalent to 1)

# Attempting to convert an empty string to an integer results in an error:
# print(int(name_blank))  # Uncommenting this will raise a ValueError
# Reason: An empty string cannot be converted to an integer.


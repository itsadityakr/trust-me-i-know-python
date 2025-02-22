# Python String Methods - Complete Guide for Absolute Beginners

# In Python, a string is a sequence of characters enclosed in:
# - Single quotes: 'hello'
# - Double quotes: "hello"
# - Triple quotes (for multi-line strings): '''hello''' or """hello"""

# Strings in Python are **immutable** (cannot be changed after creation),
# but various string methods allow us to manipulate and process them effectively.

# Let's explore all the string methods in Python with examples.


# 1. upper()
# Converts all lowercase letters in a string to uppercase.

text = "hello world"
print(text.upper())  # Output: "HELLO WORLD"


# 2. lower()
# Converts all uppercase letters in a string to lowercase.

text = "Hello WORLD"
print(text.lower())  # Output: "hello world"


# 3. title()
# Capitalizes the first letter of each word in the string.

text = "python is fun"
print(text.title())  # Output: "Python Is Fun"


# 4. capitalize()
# Capitalizes only the first letter of the string and makes the rest lowercase.

text = "hello WORLD"
print(text.capitalize())  # Output: "Hello world"


# 5. swapcase()
# Swaps uppercase letters to lowercase and vice versa.

text = "Hello WoRLD"
print(text.swapcase())  # Output: "hELLO wOrld"


# 6. strip()
# Removes leading and trailing whitespaces from the string.

text = "   Hello World   "
print(text.strip())  # Output: "Hello World"


# 7. lstrip()
# Removes leading (left-side) whitespaces only.

text = "   Hello World"
print(text.lstrip())  # Output: "Hello World"


# 8. rstrip()
# Removes trailing (right-side) whitespaces only.

text = "Hello World   "
print(text.rstrip())  # Output: "Hello World"


# 9. replace(old, new)
# Replaces all occurrences of 'old' with 'new' in the string.

text = "Hello Python"
print(text.replace("Python", "World"))  # Output: "Hello World"


# 10. split(separator)
# Splits the string into a list of words based on the given separator.
# If no separator is provided, it defaults to spaces.

text = "Python is fun"
print(text.split())  # Output: ['Python', 'is', 'fun']


# 11. join(iterable)
# Joins elements of an iterable (like a list) into a single string using the given string as a separator.

words = ["Python", "is", "awesome"]
print(" ".join(words))  # Output: "Python is awesome"


# 12. find(substring, start, end)
# Returns the index of the first occurrence of the substring.
# Returns -1 if not found.

text = "Hello Python"
print(text.find("Python"))  # Output: 6
print(text.find("Java"))  # Output: -1


# 13. index(substring, start, end)
# Same as find(), but raises an error if the substring is not found.

text = "Hello Python"
print(text.index("Python"))  # Output: 6

# print(text.index("Java"))  # Raises ValueError if substring is not found


# 14. count(substring)
# Returns the number of times a substring appears in the string.

text = "Python is great. Python is fun!"
print(text.count("Python"))  # Output: 2


# 15. startswith(prefix, start, end)
# Checks if the string starts with the given prefix.

text = "Hello Python"
print(text.startswith("Hello"))  # Output: True
print(text.startswith("Python"))  # Output: False


# 16. endswith(suffix, start, end)
# Checks if the string ends with the given suffix.

text = "Hello Python"
print(text.endswith("Python"))  # Output: True
print(text.endswith("Hello"))  # Output: False


# 17. isalpha()
# Checks if the string contains only alphabetic characters (A-Z, a-z) and is non-empty.

text = "Hello"
print(text.isalpha())  # Output: True

text = "Hello123"
print(text.isalpha())  # Output: False


# 18. isdigit()
# Checks if the string contains only numeric digits (0-9).

text = "12345"
print(text.isdigit())  # Output: True

text = "123abc"
print(text.isdigit())  # Output: False


# 19. isalnum()
# Checks if the string contains only alphanumeric characters (A-Z, a-z, 0-9) and is non-empty.

text = "Hello123"
print(text.isalnum())  # Output: True

text = "Hello 123"
print(text.isalnum())  # Output: False (contains space)


# 20. isspace()
# Checks if the string contains only whitespace characters.

text = "   "
print(text.isspace())  # Output: True

text = "Hello"
print(text.isspace())  # Output: False


# 21. islower()
# Checks if all characters in the string are lowercase.

text = "hello"
print(text.islower())  # Output: True

text = "Hello"
print(text.islower())  # Output: False


# 22. isupper()
# Checks if all characters in the string are uppercase.

text = "HELLO"
print(text.isupper())  # Output: True

text = "Hello"
print(text.isupper())  # Output: False


# 23. istitle()
# Checks if each word in the string starts with an uppercase letter.

text = "Hello World"
print(text.istitle())  # Output: True

text = "hello world"
print(text.istitle())  # Output: False


# 24. zfill(width)
# Pads the string with leading zeros to make it at least the specified width.

text = "42"
print(text.zfill(5))  # Output: "00042"


# 25. format()
# Formats a string using placeholders.

name = "Alice"
age = 25
text = "My name is {} and I am {} years old.".format(name, age)
print(text)  # Output: "My name is Alice and I am 25 years old."


# 26. f-strings (formatted string literals)
# Another way to format strings in Python (introduced in Python 3.6).

name = "Alice"
age = 25
text = f"My name is {name} and I am {age} years old."
print(text)  # Output: "My name is Alice and I am 25 years old."


# 27. encode(encoding="utf-8")
# Encodes the string into bytes using the specified encoding.

text = "Hello"
encoded_text = text.encode("utf-8")
print(encoded_text)  # Output: b'Hello'


# 28. ljust(width, fillchar)
# Left aligns the string and fills the remaining space with the specified character.

text = "Hello"
print(text.ljust(10, "-"))  # Output: "Hello-----"


# 29. rjust(width, fillchar)
# Right aligns the string and fills the remaining space with the specified character.

text = "Hello"
print(text.rjust(10, "-"))  # Output: "-----Hello"


# 30. center(width, fillchar)
# Centers the string and fills the remaining space with the specified character.

text = "Hello"
print(text.center(10, "-"))  # Output: "--Hello---"


# Summary of String Methods
"""
1. Case conversion: upper(), lower(), title(), capitalize(), swapcase()
2. Trimming: strip(), lstrip(), rstrip()
3. Finding & replacing: find(), index(), replace(), count()
4. Checking start/end: startswith(), endswith()
5. String analysis: isalpha(), isdigit(), isalnum(), isspace(), islower(), isupper(), istitle()
6. Splitting & joining: split(), join()
7. Formatting: format(), f-strings, zfill(), ljust(), rjust(), center()
8. Encoding: encode()
"""


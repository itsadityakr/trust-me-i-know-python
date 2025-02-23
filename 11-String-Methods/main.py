# Python String Methods - Complete Guide

# Strings are immutable sequences of characters enclosed in quotes (' ', " ", ''' ''' or """ """).

text = "hello world"

# 1. Case conversion
print(text.upper())     # "HELLO WORLD"
print(text.lower())     # "hello world"
print(text.title())     # "Hello World"
print(text.capitalize())  # "Hello world"
print(text.swapcase())  # "HELLO WORLD"

# 2. Trimming
text = "   Hello World   "
print(text.strip())    # "Hello World"
print(text.lstrip())   # "Hello World"
print(text.rstrip())   # "Hello World"

# 3. Finding & replacing
text = "Hello Python"
print(text.replace("Python", "World"))  # "Hello World"
print(text.find("Python"))  # 6
print(text.count("l"))  # 2
print(text.startswith("Hello"))  # True
print(text.endswith("Python"))  # True

# 4. Checking content
print("Hello".isalpha())  # True
print("12345".isdigit())  # True
print("Hello123".isalnum())  # True
print("   ".isspace())  # True
print("hello".islower())  # True
print("HELLO".isupper())  # True
print("Hello World".istitle())  # True

# 5. Splitting & joining
text = "Python is fun"
print(text.split())  # ['Python', 'is', 'fun']
words = ["Python", "is", "awesome"]
print(" ".join(words))  # "Python is awesome"

# 6. Formatting
name, age = "Alice", 25
print(f"My name is {name} and I am {age} years old.")  # f-string
print("My name is {} and I am {} years old.".format(name, age))

# 7. Padding
text = "42"
print(text.zfill(5))  # "00042"
print("Hello".ljust(10, "-"))  # "Hello-----"
print("Hello".rjust(10, "-"))  # "-----Hello"
print("Hello".center(10, "-"))  # "--Hello---"

# 8. Encoding
print("Hello".encode("utf-8"))  # b'Hello'
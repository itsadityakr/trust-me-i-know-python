
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

# String Methods

## Introduction  
In Python, a string is a sequence of characters enclosed in:  
- Single quotes: `'hello'`  
- Double quotes: `"hello"`  
- Triple quotes (for multi-line strings): `'''hello'''` or `"""hello"""`  

Strings in Python are **immutable** (cannot be changed after creation), but various string methods allow us to manipulate and process them effectively.  

---

## 1. Case Conversion Methods  

- **`upper()`** – Converts all lowercase letters in a string to uppercase.  
  ```python
  "hello world".upper()  # Output: "HELLO WORLD"
  ```  

- **`lower()`** – Converts all uppercase letters in a string to lowercase.  
  ```python
  "Hello WORLD".lower()  # Output: "hello world"
  ```  

- **`title()`** – Capitalizes the first letter of each word in the string.  
  ```python
  "python is fun".title()  # Output: "Python Is Fun"
  ```  

- **`capitalize()`** – Capitalizes only the first letter of the string and makes the rest lowercase.  
  ```python
  "hello WORLD".capitalize()  # Output: "Hello world"
  ```  

- **`swapcase()`** – Swaps uppercase letters to lowercase and vice versa.  
  ```python
  "Hello WoRLD".swapcase()  # Output: "hELLO wOrld"
  ```  

---

## 2. Trimming Methods  

- **`strip()`** – Removes leading and trailing whitespaces.  
  ```python
  "   Hello World   ".strip()  # Output: "Hello World"
  ```  

- **`lstrip()`** – Removes leading (left-side) whitespaces only.  
  ```python
  "   Hello World".lstrip()  # Output: "Hello World"
  ```  

- **`rstrip()`** – Removes trailing (right-side) whitespaces only.  
  ```python
  "Hello World   ".rstrip()  # Output: "Hello World"
  ```  

---

## 3. Finding & Replacing Methods  

- **`replace(old, new)`** – Replaces all occurrences of `old` with `new`.  
  ```python
  "Hello Python".replace("Python", "World")  # Output: "Hello World"
  ```  

- **`find(substring, start, end)`** – Returns the index of the first occurrence of `substring` or `-1` if not found.  
  ```python
  "Hello Python".find("Python")  # Output: 6
  ```  

- **`index(substring, start, end)`** – Same as `find()`, but raises an error if the substring is not found.  
  ```python
  "Hello Python".index("Python")  # Output: 6
  ```  

- **`count(substring)`** – Returns the number of times a substring appears.  
  ```python
  "Python is great. Python is fun!".count("Python")  # Output: 2
  ```  

---

## 4. Checking Start/End of Strings  

- **`startswith(prefix, start, end)`** – Checks if the string starts with `prefix`.  
  ```python
  "Hello Python".startswith("Hello")  # Output: True
  ```  

- **`endswith(suffix, start, end)`** – Checks if the string ends with `suffix`.  
  ```python
  "Hello Python".endswith("Python")  # Output: True
  ```  

---

## 5. String Analysis Methods  

- **`isalpha()`** – Checks if the string contains only alphabetic characters.  
  ```python
  "Hello".isalpha()  # Output: True
  ```  

- **`isdigit()`** – Checks if the string contains only numeric digits.  
  ```python
  "12345".isdigit()  # Output: True
  ```  

- **`isalnum()`** – Checks if the string contains only alphanumeric characters.  
  ```python
  "Hello123".isalnum()  # Output: True
  ```  

- **`isspace()`** – Checks if the string contains only whitespace characters.  
  ```python
  "   ".isspace()  # Output: True
  ```  

- **`islower()`** – Checks if all characters in the string are lowercase.  
  ```python
  "hello".islower()  # Output: True
  ```  

- **`isupper()`** – Checks if all characters in the string are uppercase.  
  ```python
  "HELLO".isupper()  # Output: True
  ```  

- **`istitle()`** – Checks if each word in the string starts with an uppercase letter.  
  ```python
  "Hello World".istitle()  # Output: True
  ```  

---

## 6. Splitting & Joining Methods  

- **`split(separator)`** – Splits the string into a list based on `separator`.  
  ```python
  "Python is fun".split()  # Output: ['Python', 'is', 'fun']
  ```  

- **`join(iterable)`** – Joins elements of an iterable into a single string using the given string as a separator.  
  ```python
  " ".join(["Python", "is", "awesome"])  # Output: "Python is awesome"
  ```  

---

## 7. Formatting Methods  

- **`format()`** – Formats a string using placeholders.  
  ```python
  "My name is {} and I am {} years old.".format("Alice", 25)
  ```  

- **f-strings** (Python 3.6+) – Another way to format strings.  
  ```python
  name, age = "Alice", 25
  f"My name is {name} and I am {age} years old."
  ```  

- **`zfill(width)`** – Pads the string with leading zeros to make it at least the specified width.  
  ```python
  "42".zfill(5)  # Output: "00042"
  ```  

---

## 8. Alignment & Padding Methods  

- **`ljust(width, fillchar)`** – Left aligns the string and fills remaining space with `fillchar`.  
  ```python
  "Hello".ljust(10, "-")  # Output: "Hello-----"
  ```  

- **`rjust(width, fillchar)`** – Right aligns the string and fills remaining space with `fillchar`.  
  ```python
  "Hello".rjust(10, "-")  # Output: "-----Hello"
  ```  

- **`center(width, fillchar)`** – Centers the string and fills remaining space with `fillchar`.  
  ```python
  "Hello".center(10, "-")  # Output: "--Hello---"
  ```  

---

## 9. Encoding Methods  

- **`encode(encoding="utf-8")`** – Encodes the string into bytes using the specified encoding.  
  ```python
  "Hello".encode("utf-8")  # Output: b'Hello'
  ```  

---

## Summary of String Methods  

### 1. Case Conversion  
`upper()`, `lower()`, `title()`, `capitalize()`, `swapcase()`  

### 2. Trimming  
`strip()`, `lstrip()`, `rstrip()`  

### 3. Finding & Replacing  
`find()`, `index()`, `replace()`, `count()`  

### 4. Checking Start/End  
`startswith()`, `endswith()`  

### 5. String Analysis  
`isalpha()`, `isdigit()`, `isalnum()`, `isspace()`, `islower()`, `isupper()`, `istitle()`  

### 6. Splitting & Joining  
`split()`, `join()`  

### 7. Formatting  
`format()`, `f-strings`, `zfill()`, `ljust()`, `rjust()`, `center()`  

### 8. Encoding  
`encode()`  

By mastering these string methods, you can efficiently manipulate and process text in Python.

![Static Badge](https://img.shields.io/badge/Aditya%20Kumar-black?style=for-the-badge&logo=atlasos&logoColor=%23ffffff)
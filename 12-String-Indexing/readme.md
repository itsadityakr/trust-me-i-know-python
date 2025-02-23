![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

# String Indexing

## **What is String Indexing?**  
String indexing allows accessing individual characters within a string based on their position (index). Python supports:  

- **Positive Indexing (Left to Right)** → Starts from `0` and increases by `1`.  
- **Negative Indexing (Right to Left)** → Starts from `-1` and decreases by `1`.  

This enables flexible string manipulation, including character extraction, substring retrieval, and iteration.  

---

## **1. Understanding String Indexing**  

### **Positive Indexing (Left to Right)**  
Each character has a **positive index**, starting from `0`.  

| P  | y  | t  | h  | o  | n  |  
|----|----|----|----|----|----|  
| 0  | 1  | 2  | 3  | 4  | 5  |  

- `text[0]` → `"P"` (First character)  
- `text[3]` → `"h"` (Fourth character)  
- `text[5]` → `"n"` (Last character using positive indexing)  

### **Negative Indexing (Right to Left)**  
Negative indices allow accessing characters from the end.  

| P  | y  | t  | h  | o  | n  |  
|----|----|----|----|----|----|  
| -6 | -5 | -4 | -3 | -2 | -1 |  

- `text[-1]` → `"n"` (Last character)  
- `text[-3]` → `"h"` (Third-last character)  
- `text[-6]` → `"P"` (First character using negative indexing)  

---

## **2. Accessing Characters Using Indexing**  

### **Single Character Access**  
Characters can be accessed using square brackets `[ ]`.  

```python
text = "Python"

print(text[0])  # Output: 'P'
print(text[2])  # Output: 't'
print(text[-1]) # Output: 'n'
```

### **IndexError (Out of Range Access)**  
Trying to access an invalid index results in an `IndexError`.  

```python
print(text[10])  # IndexError: string index out of range
```

---

## **3. String Slicing (Extracting Substrings)**  

Slicing extracts a portion of a string using `[start:end:step]`.  

### **Basic Slicing**  
- **Start**: Where slicing begins (inclusive).  
- **End**: Where slicing stops (**exclusive**).  
- **Step**: Interval between characters (optional).  

```python
text = "Python"

print(text[1:4])  # Output: 'yth' (Indexes 1 to 3)
print(text[:4])   # Output: 'Pyth' (From start to index 3)
print(text[2:])   # Output: 'thon' (From index 2 to end)
```

### **Slicing with Negative Indexes**  
Negative indexes work the same way.  

```python
text = "Python"

print(text[-4:-1])  # Output: 'tho'
print(text[-6:])    # Output: 'Python' (Whole string)
```

---

## **4. Step in Slicing (Skipping Characters)**  

The **step** argument controls character skipping.  

```python
text = "Python"

print(text[::2])   # Output: 'Pto' (Every second character)
print(text[1::2])  # Output: 'yhn' (Every second character from index 1)
```

### **Reversing a String with Step**  
A step of `-1` reverses the string.  

```python
print(text[::-1])  # Output: 'nohtyP' (Reversed string)
```

Other step variations:  

```python
print(text[::-2])  # Output: 'nhy' (Every second character in reverse)
```

---

## **5. Edge Cases in String Indexing and Slicing**  

### **1. When `start > end` in Slicing**
If the **start index** is greater than the **end index**, the result is an **empty string**.  

```python
text = "Python"

print(text[4:2])   # Output: '' (empty string)
print(text[-2:-4]) # Output: '' (empty string)
```

### **2. When `step = 0`**
A `step` value of `0` is invalid and raises an error.  

```python
print(text[::0])   # ValueError: slice step cannot be zero
```

### **3. When `start` or `end` is Out of Range**
If the `start` or `end` index is beyond the string length, Python **gracefully handles it** without an error.  

```python
text = "Python"

print(text[0:100])  # Output: 'Python' (Ignores out-of-range index)
print(text[-100:3]) # Output: 'Pyt' (Start is too low but works)
```

### **4. When `step` is Negative with `start < end`**
If `step` is negative, but `start` is **less than** `end`, slicing **returns an empty string**.  

```python
text = "Python"

print(text[2:5:-1])  # Output: '' (empty string)
```

### **5. When `start` and `end` are Missing**
Python defaults to using the entire string.  

```python
text = "Python"

print(text[:])    # Output: 'Python' (Full string)
print(text[::])   # Output: 'Python' (Full string)
```

---

## **6. Looping Through a String Using Indexing**  

A `for` loop with indexing enables character-wise processing.  

```python
text = "Python"

for i in range(len(text)):  
    print(f"Character at index {i}: {text[i]}")
```

**Output:**  
```
Character at index 0: P  
Character at index 1: y  
Character at index 2: t  
Character at index 3: h  
Character at index 4: o  
Character at index 5: n  
```

---

## **7. Using Indexing in String Operations**  

### **Checking the First and Last Character**  
```python
text = "Python"

if text[0] == "P":
    print("The string starts with 'P'.")

if text[-1] == "n":
    print("The string ends with 'n'.")
```

### **Replacing Characters (Strings Are Immutable)**  
Strings in Python are **immutable**, meaning you **cannot** modify them directly using indexing.  

```python
text = "Python"

# This will raise an error:
# text[0] = "J"  # TypeError: 'str' object does not support item assignment

# Instead, create a new string:
new_text = "J" + text[1:]
print(new_text)  # Output: 'Jython'
```

---

## **8. Summary of String Indexing and Slicing**  

### **Indexing**  
- **Positive Indexing**: `0` to `len(string) - 1`  
- **Negative Indexing**: `-1` to `-len(string)`  

### **Slicing**  
- `text[start:end]` → Extracts substring from `start` to `end-1`  
- `text[start:end:step]` → Steps through the string at intervals  
- `text[::-1]` → Reverses the string  

### **Edge Cases**  
✔ `start > end` → Returns an empty string  
✔ `step = 0` → Raises an error  
✔ `start` or `end` out of range → No error, handles gracefully  
✔ Negative `step` with `start < end` → Returns an empty string  

---

### **Conclusion**  
String indexing and slicing are fundamental techniques in Python, allowing efficient text manipulation. Understanding positive and negative indexing, step values, and edge cases helps avoid common pitfalls and enhances control over string processing.

![Static Badge](https://img.shields.io/badge/Aditya%20Kumar-black?style=for-the-badge&logo=atlasos&logoColor=%23ffffff)
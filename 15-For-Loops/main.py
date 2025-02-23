# Python For Loop - Complete Guide

# 1. **Basic For Loop**
for i in range(5):  # Loops from 0 to 4
    print(i)

# Output: 0, 1, 2, 3, 4


# 2. **Looping Through a List**
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Output: apple, banana, cherry


# 3. **Looping Through a String**
word = "Python"
for letter in word:
    print(letter)

# Output: P, y, t, h, o, n


# 4. **Using `range()`**
for num in range(2, 10, 2):  # Start at 2, step by 2
    print(num)

# Output: 2, 4, 6, 8


# 5. **Using `break`**
for num in range(10):
    if num == 5:
        break
    print(num)

# Output: 0, 1, 2, 3, 4


# 6. **Using `continue`**
for num in range(5):
    if num == 2:
        continue
    print(num)

# Output: 0, 1, 3, 4


# 7. **Using `else`**
for num in range(3):
    print(num)
else:
    print("Loop completed!")

# Output: 0, 1, 2, Loop completed!


# 8. **Nested For Loops**
for i in range(1, 4):
    for j in range(1, 3):
        print(f"i={i}, j={j}")

# Output: (Pairs of i, j values)


# 9. **Looping Through a Dictionary**
student = {"name": "Alice", "age": 25, "grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}")

# Output: name: Alice, age: 25, grade: A


# 10. **Using `enumerate()`**
colors = ["red", "blue", "green"]
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

# Output: Index 0: red, Index 1: blue, Index 2: green


# 11. **List Comprehension**
numbers = [x**2 for x in range(5)]
print(numbers)

# Output: [0, 1, 4, 9, 16]


# 12. **Using `zip()`**
names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 88]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# Output: Alice scored 90, Bob scored 85, Charlie scored 88


# **Summary of For Loops**
"""
1. Basic for loop: Iterates over a sequence.  
2. Lists & Strings: Iterate through elements/characters.  
3. range(): Generates sequences of numbers.  
4. break: Stops the loop immediately.  
5. continue: Skips current iteration and moves to next.  
6. else: Runs if the loop exits normally.  
7. Nested loops: Loops inside loops.  
8. Dictionaries: Iterate through key-value pairs.  
9. enumerate(): Get index along with value.  
10. List comprehension: Compact list creation.  
11. zip(): Iterate over multiple sequences.  
"""

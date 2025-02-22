# Python For Loop - Complete Guide for Absolute Beginners

# What is a For Loop?
# - A `for` loop is used to iterate over sequences (lists, tuples, strings, dictionaries, etc.).
# - It executes a block of code for each item in the sequence.
# - The loop automatically stops when all items are processed.

# Syntax:
# for variable in sequence:
#     # Code to execute

# Example 1: Basic For Loop
print("Basic for loop:")
for i in range(5):  # Loops from 0 to 4
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4


# 1. Using For Loop with Lists
fruits = ["apple", "banana", "cherry"]
print("Looping through a list:")
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry


# 2. Using For Loop with Strings
print("Looping through a string:")
word = "Python"
for letter in word:
    print(letter)

# Output:
# P
# y
# t
# h
# o
# n


# 3. Using For Loop with `range()`
# - The `range()` function generates a sequence of numbers.

print("Using range:")
for num in range(2, 10, 2):  # Start at 2, end at 10 (excluded), step by 2
    print(num)

# Output:
# 2
# 4
# 6
# 8


# 4. Using `break` in a For Loop
# - `break` exits the loop immediately.

print("Using break:")
for num in range(10):
    if num == 5:
        break  # Stop the loop when num is 5
    print(num)

# Output:
# 0
# 1
# 2
# 3
# 4


# 5. Using `continue` in a For Loop
# - `continue` skips the rest of the current iteration and moves to the next.

print("Using continue:")
for num in range(5):
    if num == 2:
        continue  # Skip number 2
    print(num)

# Output:
# 0
# 1
# 3
# 4


# 6. Using `else` with For Loop
# - The `else` block runs if the loop completes normally (without `break`).

print("Using else:")
for num in range(3):
    print(num)
else:
    print("Loop completed!")  # Runs when loop exits normally

# Output:
# 0
# 1
# 2
# Loop completed!


# 7. Nested For Loops
# - A for loop inside another for loop.

print("Nested for loop:")
for i in range(1, 4):  # Outer loop
    for j in range(1, 3):  # Inner loop
        print(f"i={i}, j={j}")

# Output:
# i=1, j=1
# i=1, j=2
# i=2, j=1
# i=2, j=2
# i=3, j=1
# i=3, j=2


# 8. Looping Through a Dictionary
student = {"name": "Alice", "age": 25, "grade": "A"}
print("Looping through a dictionary (keys and values):")
for key, value in student.items():
    print(f"{key}: {value}")

# Output:
# name: Alice
# age: 25
# grade: A


# 9. Looping with `enumerate()`
# - `enumerate()` provides an index along with the item.

print("Using enumerate:")
colors = ["red", "blue", "green"]
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

# Output:
# Index 0: red
# Index 1: blue
# Index 2: green


# 10. Using List Comprehension in For Loop
# - A concise way to create lists using for loops.

print("List comprehension:")
numbers = [x**2 for x in range(5)]  # Square numbers from 0 to 4
print(numbers)

# Output:
# [0, 1, 4, 9, 16]


# 11. Looping with `zip()`
# - `zip()` combines multiple lists and loops through them simultaneously.

names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 88]
print("Using zip:")
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# Output:
# Alice scored 90
# Bob scored 85
# Charlie scored 88


# Summary of For Loops:
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


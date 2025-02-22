# Python Nested Loops - Complete Guide for Absolute Beginners

# What is a Nested Loop?
# - A **nested loop** is a loop inside another loop.
# - The **inner loop** executes completely for each iteration of the **outer loop**.
# - Useful for working with matrices, patterns, tables, and more.

# Syntax:
# for outer_variable in outer_sequence:
#     for inner_variable in inner_sequence:
#         # Code inside the inner loop

# Example 1: Basic Nested For Loop
print("Basic Nested Loop:")
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"i={i}, j={j}")

# Output:
# i=0, j=0
# i=0, j=1
# i=1, j=0
# i=1, j=1
# i=2, j=0
# i=2, j=1


# 1. Nested Loops for Multiplication Table
print("Multiplication Table:")
for i in range(1, 4):  # Rows (1 to 3)
    for j in range(1, 6):  # Columns (1 to 5)
        print(i * j, end="  ")  # Multiply i * j
    print()  # New line after each row

# Output:
# 1  2  3  4  5
# 2  4  6  8  10
# 3  6  9  12  15


# 2. Printing a Square Pattern using Nested Loops
size = 4
print("Square Pattern:")
for i in range(size):
    for j in range(size):
        print("*", end=" ")
    print()

# Output:
# * * * *
# * * * *
# * * * *
# * * * *


# 3. Printing a Right-Angled Triangle Pattern
print("Triangle Pattern:")
for i in range(1, 6):  # Rows
    for j in range(i):  # Columns (increases with rows)
        print("*", end=" ")
    print()

# Output:
# *
# * *
# * * *
# * * * *
# * * * * *


# 4. Nested While Loop Example
print("Nested While Loop:")
i = 1
while i <= 3:  # Outer loop
    j = 1
    while j <= 2:  # Inner loop
        print(f"i={i}, j={j}")
        j += 1
    i += 1

# Output:
# i=1, j=1
# i=1, j=2
# i=2, j=1
# i=2, j=2
# i=3, j=1
# i=3, j=2


# 5. Using `break` in Nested Loops
print("Using break in Nested Loops:")
for i in range(3):
    for j in range(3):
        if j == 2:
            break  # Stops the inner loop when j == 2
        print(f"i={i}, j={j}")

# Output:
# i=0, j=0
# i=0, j=1
# i=1, j=0
# i=1, j=1
# i=2, j=0
# i=2, j=1


# 6. Using `continue` in Nested Loops
print("Using continue in Nested Loops:")
for i in range(3):
    for j in range(3):
        if j == 1:
            continue  # Skips iteration when j == 1
        print(f"i={i}, j={j}")

# Output:
# i=0, j=0
# i=0, j=2
# i=1, j=0
# i=1, j=2
# i=2, j=0
# i=2, j=2


# 7. Nested Loop with Lists (Matrix Example)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix using Nested Loops:")
for row in matrix:  # Outer loop iterates over rows
    for num in row:  # Inner loop iterates over numbers in a row
        print(num, end=" ")
    print()  # New line after each row

# Output:
# 1 2 3
# 4 5 6
# 7 8 9


# 8. Nested Loop with Dictionary
students = {
    "Alice": [85, 90, 78],
    "Bob": [88, 76, 92]
}

print("Nested Loop with Dictionary:")
for student, scores in students.items():  # Outer loop iterates over dictionary
    print(f"{student}: ", end="")
    for score in scores:  # Inner loop iterates over list of scores
        print(score, end=" ")
    print()

# Output:
# Alice: 85 90 78
# Bob: 88 76 92


# 9. Nested Loop with `zip()`
names = ["Alice", "Bob", "Charlie"]
scores = [[90, 85, 88], [78, 92, 80], [75, 85, 89]]

print("Nested Loop with zip():")
for name, marks in zip(names, scores):
    print(f"{name}'s Scores: ", end="")
    for mark in marks:
        print(mark, end=" ")
    print()

# Output:
# Alice's Scores: 90 85 88
# Bob's Scores: 78 92 80
# Charlie's Scores: 75 85 89


# 10. Creating a Chessboard Pattern with Nested Loops
size = 8
print("Chessboard Pattern:")
for i in range(size):
    for j in range(size):
        if (i + j) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()

# Output:
# X O X O X O X O
# O X O X O X O X
# X O X O X O X O
# O X O X O X O X
# X O X O X O X O
# O X O X O X O X
# X O X O X O X O
# O X O X O X O X


# Summary of Nested Loops:
"""
1. Basic nested loop: Inner loop runs fully for each outer loop iteration.
2. Patterns: Square, triangle, chessboard.
3. While inside while: Works similarly to nested for loops.
4. `break`: Stops the inner loop when a condition is met.
5. `continue`: Skips the current iteration inside inner loop.
6. Matrix representation: Used to display 2D lists.
7. Dictionaries: Iterate through keys and values.
8. `zip()`: Iterate multiple lists in a nested structure.
"""


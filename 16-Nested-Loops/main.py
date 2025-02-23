# Python Nested Loops - Complete Guide

# 1. **Basic Nested Loop**
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# Output: (Pairs of i, j values)


# 2. **Multiplication Table**
for i in range(1, 4):
    for j in range(1, 6):
        print(i * j, end="  ")
    print()

# Output:
# 1  2  3  4  5
# 2  4  6  8 10
# 3  6  9 12 15


# 3. **Square Pattern**
size = 4
for i in range(size):
    for j in range(size):
        print("*", end=" ")
    print()

# Output: 4x4 grid of *


# 4. **Triangle Pattern**
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# Output: Right-angled triangle pattern


# 5. **Nested While Loop**
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

# Output: (Pairs of i, j values)


# 6. **Using `break`**
for i in range(3):
    for j in range(3):
        if j == 2:
            break
        print(f"i={i}, j={j}")

# Output: Skips further inner loop execution when j == 2


# 7. **Using `continue`**
for i in range(3):
    for j in range(3):
        if j == 1:
            continue
        print(f"i={i}, j={j}")

# Output: Skips j == 1 iteration


# 8. **Matrix Representation (2D List)**
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for num in row:
        print(num, end=" ")
    print()

# Output: Displays matrix in grid format


# 9. **Nested Loop with Dictionary**
students = {
    "Alice": [85, 90, 78],
    "Bob": [88, 76, 92]
}
for student, scores in students.items():
    print(f"{student}: ", end="")
    for score in scores:
        print(score, end=" ")
    print()

# Output: Student names with their scores


# 10. **Using `zip()` in Nested Loops**
names = ["Alice", "Bob", "Charlie"]
scores = [[90, 85, 88], [78, 92, 80], [75, 85, 89]]
for name, marks in zip(names, scores):
    print(f"{name}'s Scores: ", end="")
    for mark in marks:
        print(mark, end=" ")
    print()

# Output: Student names with corresponding scores


# 11. **Chessboard Pattern**
size = 8
for i in range(size):
    for j in range(size):
        print("X" if (i + j) % 2 == 0 else "O", end=" ")
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

# **Summary of Nested Loops**
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

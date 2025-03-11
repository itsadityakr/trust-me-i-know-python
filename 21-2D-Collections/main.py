# 2D Collections in Python: List, Set, and Tuple
# This script explains different types of 2D collections in Python:
# 1. List of Lists (Mutable, Ordered)
# 2. Set of Frozensets (Immutable, Unordered, Unique rows only)
# 3. Tuple of Tuples (Immutable, Ordered)
# Each section contains examples with inline expected output.

# ------------------------------------------------------------------------------
# 1. LIST OF LISTS (Mutable & Ordered)
# ------------------------------------------------------------------------------
# Lists can store multiple lists inside them, forming a 2D structure.
# They allow duplicate values, and elements can be modified.

matrix_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Printing the original list of lists
print("Original List of Lists:")
for row in matrix_list:
    print(row)
# Expected Output:
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

# Accessing an element (row index 1, column index 2)
element = matrix_list[1][2]
print("Accessed Element:", element)
# Expected Output: 6

# Accessing a row (row number)
row = matrix_list[1]
print("Accessed Row:", row)
# Expected Output: [4, 5, 6]

# Modifying an element in the list (changing 6 to 99)
matrix_list[1][2] = 99

# Printing the modified list
print("Modified List of Lists:")
for row in matrix_list:
    print(row)
# Expected Output:
# [1, 2, 3]
# [4, 5, 99]
# [7, 8, 9]

# Iterating through the list and printing each element
print("Iterating through List of Lists:")
for row in matrix_list:
    for value in row:
        print(value, end=" ")
    print()  # New line after each row
# Expected Output:
# 1 2 3
# 4 5 99
# 7 8 9

# ------------------------------------------------------------------------------
# 2. SET OF FROZENSETS (Immutable & Unordered, Unique Rows)
# ------------------------------------------------------------------------------
# Normal sets do not allow lists because they are mutable.
# Instead, we use frozensets, which are immutable and allow only unique rows.
# The set is unordered, so row order is not guaranteed.

matrix_set = {
    frozenset([1, 2, 3]),
    frozenset([4, 5, 6]),
    frozenset([7, 8, 9]),
    frozenset([1, 2, 3])  # Duplicate row (will be ignored)
}

# Printing the set of frozensets
print("Set of Frozensets (Unique Rows Only):")
print(matrix_set)
# Expected Output (order may vary):
# {frozenset({1, 2, 3}), frozenset({4, 5, 6}), frozenset({7, 8, 9})}

# Checking if a specific row exists
row_check = frozenset([1, 2, 3]) in matrix_set
print("Is [1,2,3] in matrix_set?:", row_check)
# Expected Output: True

# ------------------------------------------------------------------------------
# 3. TUPLE OF TUPLES (Immutable & Ordered)
# ------------------------------------------------------------------------------
# Tuples are immutable, so they cannot be modified after creation.
# A tuple of tuples forms a fixed 2D structure, similar to a read-only list.

matrix_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# Printing the tuple of tuples
print("Tuple of Tuples:")
for row in matrix_tuple:
    print(row)
# Expected Output:
# (1, 2, 3)
# (4, 5, 6)
# (7, 8, 9)

# Accessing an element
tuple_element = matrix_tuple[1][2]
print("Accessed Element from Tuple:", tuple_element)
# Expected Output: 6

# Iterating through the tuple and printing each element
print("Iterating through Tuple of Tuples:")
for row in matrix_tuple:
    for value in row:
        print(value, end=" ")
    print()  # New line after each row
# Expected Output:
# 1 2 3
# 4 5 6
# 7 8 9

# Index Slicing in Lists

# Define a list
numsList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Example 1: Get elements from index 2 to 5 (exclusive)
slice1 = numsList[2:5]
print("List Slice 1 (2:5):", slice1)  # Expected Output: [2, 3, 4]

# Example 2: Get elements from the start to index 5 (exclusive)
slice2 = numsList[:5]
print("List Slice 2 (:5):", slice2)  # Expected Output: [0, 1, 2, 3, 4]

# Example 3: Get elements from index 5 to the end
slice3 = numsList[5:]
print("List Slice 3 (5:):", slice3)  # Expected Output: [5, 6, 7, 8, 9]

# Example 4: Get every second element
slice4 = numsList[::2]
print("List Slice 4 (::2):", slice4)  # Expected Output: [0, 2, 4, 6, 8]

# Example 5: Reverse the list
slice5 = numsList[::-1]
print("List Slice 5 (::-1):", slice5)  # Expected Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Example 6: Get the last three elements using negative indices
slice6 = numsList[-3:]
print("List Slice 6 (-3:):", slice6)  # Expected Output: [7, 8, 9]

# Index Slicing in Tuples

# Define a tuple
numsTuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Example 1: Get elements from index 2 to 5 (exclusive)
slice1_tuple = numsTuple[2:5]
print("Tuple Slice 1 (2:5):", slice1_tuple)  # Expected Output: (2, 3, 4)

# Example 2: Get elements from the start to index 5 (exclusive)
slice2_tuple = numsTuple[:5]
print("Tuple Slice 2 (:5):", slice2_tuple)  # Expected Output: (0, 1, 2, 3, 4)

# Example 3: Get elements from index 5 to the end
slice3_tuple = numsTuple[5:]
print("Tuple Slice 3 (5:):", slice3_tuple)  # Expected Output: (5, 6, 7, 8, 9)

# Example 4: Get every second element
slice4_tuple = numsTuple[::2]
print("Tuple Slice 4 (::2):", slice4_tuple)  # Expected Output: (0, 2, 4, 6, 8)

# Example 5: Reverse the tuple
slice5_tuple = numsTuple[::-1]
print("Tuple Slice 5 (::-1):", slice5_tuple)  # Expected Output: (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

# Example 6: Get the last three elements using negative indices
slice6_tuple = numsTuple[-3:]
print("Tuple Slice 6 (-3:):", slice6_tuple)  # Expected Output: (7, 8, 9)
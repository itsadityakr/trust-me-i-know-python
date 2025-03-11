# collection = single "variable" used to store multiple values
# List = [] ordered and changeable (mutable). Duplicates Allowed

# Python List and All Its Methods with Examples

# Creating a sample list
numsList = [1, 2, 3, 4, 5]

# 1. append(x): Adds an element at the end of the list
numsList.append(6)
# Output: [1, 2, 3, 4, 5, 6]

# 2. extend(iterable): Extends the list by appending elements from an iterable
numsList.extend([7, 8, 9])
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. insert(index, x): Inserts an element at a given position
numsList.insert(2, 10)  # Inserts 10 at index 2
# Output: [1, 2, 10, 3, 4, 5, 6, 7, 8, 9]

# 4. remove(x): Removes the first occurrence of a specified value
numsList.remove(10)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 5. pop([index]): Removes and returns the element at the given index (or last element by default)
removed_element = numsList.pop()  # Removes 9
# Output: [1, 2, 3, 4, 5, 6, 7, 8]

# 6. index(x, [start, end]): Returns the index of the first occurrence of x
index_of_5 = numsList.index(5)
# Output: 4

# 7. count(x): Returns the number of times x appears in the list
count_of_2 = numsList.count(2)
# Output: 1

# 8. sort(key=None, reverse=False): Sorts the list in ascending order (modifies the list)
numsList.sort()
# Output: [1, 2, 3, 4, 5, 6, 7, 8]

# 9. reverse(): Reverses the list in place
numsList.reverse()
# Output: [8, 7, 6, 5, 4, 3, 2, 1]

# 10. copy(): Returns a shallow copy of the list
copy_list = numsList.copy()
# Output: [8, 7, 6, 5, 4, 3, 2, 1]

# 11. clear(): Removes all elements from the list
numsList.clear()
# Output: []

# Non-method list operations

# 12. len(): Returns the number of elements in the list
length = len(copy_list)
# Output: 8

# 13. max(): Returns the maximum element in the list
maximum = max(copy_list)
# Output: 8

# 14. min(): Returns the minimum element in the list
minimum = min(copy_list)
# Output: 1

# 15. sum(): Returns the sum of all elements in the list
total = sum(copy_list)
# Output: 36

# 16. sorted(): Returns a new sorted list without modifying the original
sorted_list = sorted(copy_list)
# Output: [1, 2, 3, 4, 5, 6, 7, 8]

# 17. list comprehension: A concise way to create lists
squared_numbers = [x ** 2 for x in range(1, 6)]
# Output: [1, 4, 9, 16, 25]

# Printing all results
print("Final List:", numsList)          # Output: Final List: []
print("Removed Element:", removed_element)  # Output: Removed Element: 9
print("Index of 5:", index_of_5)       # Output: Index of 5: 4
print("Count of 2:", count_of_2)       # Output: Count of 2: 1
print("Copied List:", copy_list)       # Output: Copied List: [8, 7, 6, 5, 4, 3, 2, 1]
print("Length of List:", length)       # Output: Length of List: 8
print("Maximum Value:", maximum)       # Output: Maximum Value: 8
print("Minimum Value:", minimum)       # Output: Minimum Value: 1
print("Sum of Elements:", total)       # Output: Sum of Elements: 36
print("Sorted List:", sorted_list)     # Output: Sorted List: [1, 2, 3, 4, 5, 6, 7, 8]
print("Squared Numbers:", squared_numbers)  # Output: Squared Numbers: [1, 4, 9, 16, 25]

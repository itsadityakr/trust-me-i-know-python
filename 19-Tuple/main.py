# Python Tuple and All Its Methods with Examples

# A tuple is an **ordered**, **immutable** collection of elements.
# It is defined using parentheses () or the tuple() constructor.

# Creating a sample tuple
numsTuple = (1, 2, 3, 4, 5)

# Tuples are immutable, meaning we **cannot** modify them after creation.
# However, we can access their elements and perform various operations.

# 1. count(x): Returns the number of times x appears in the tuple
count_of_2 = numsTuple.count(2)
# Output: 1

# 2. index(x, [start, end]): Returns the index of the first occurrence of x
index_of_4 = numsTuple.index(4)
# Output: 3

# Tuple operations

# 3. len(): Returns the number of elements in the tuple
length = len(numsTuple)
# Output: 5

# 4. max(): Returns the maximum element in the tuple (works only with comparable data types)
maximum = max(numsTuple)
# Output: 5

# 5. min(): Returns the minimum element in the tuple
minimum = min(numsTuple)
# Output: 1

# 6. sum(): Returns the sum of all numeric elements in the tuple
total = sum(numsTuple)
# Output: 15

# 7. sorted(): Returns a sorted list of the tuple's elements
sorted_tuple = sorted(numsTuple)
# Output: [1, 2, 3, 4, 5]

# 8. tuple concatenation: Merging two tuples
tuple_a = (10, 20, 30)
tuple_b = (40, 50)
concatenated_tuple = tuple_a + tuple_b
# Output: (10, 20, 30, 40, 50)

# 9. tuple repetition: Repeating elements in a tuple
repeated_tuple = tuple_a * 2
# Output: (10, 20, 30, 10, 20, 30)

# 10. membership test: Checking if an element exists in a tuple
is_present = 3 in numsTuple
# Output: True

# 11. tuple unpacking: Assigning tuple elements to variables
a, b, c, d, e = numsTuple
# a = 1, b = 2, c = 3, d = 4, e = 5

# 12. nested tuples: Tuples inside tuples
nested_tuple = ((1, 2, 3), (4, 5, 6))
# Output: ((1, 2, 3), (4, 5, 6))

# 13. converting list to tuple: Using tuple() constructor
list_to_tuple = tuple([100, 200, 300])
# Output: (100, 200, 300)

# 14. converting string to tuple: Characters become tuple elements
string_to_tuple = tuple("hello")
# Output: ('h', 'e', 'l', 'l', 'o')

# Printing all results
print("Tuple:", numsTuple)                   # Output: (1, 2, 3, 4, 5)
print("Count of 2:", count_of_2)            # Output: 1
print("Index of 4:", index_of_4)            # Output: 3
print("Length of Tuple:", length)           # Output: 5
print("Maximum Value:", maximum)            # Output: 5
print("Minimum Value:", minimum)            # Output: 1
print("Sum of Elements:", total)            # Output: 15
print("Sorted Tuple (as List):", sorted_tuple)  # Output: [1, 2, 3, 4, 5]
print("Concatenated Tuple:", concatenated_tuple)  # Output: (10, 20, 30, 40, 50)
print("Repeated Tuple:", repeated_tuple)    # Output: (10, 20, 30, 10, 20, 30)
print("Is 3 Present in Tuple?:", is_present) # Output: True
print("Tuple Unpacking:", a, b, c, d, e)    # Output: 1 2 3 4 5
print("Nested Tuple:", nested_tuple)        # Output: ((1, 2, 3), (4, 5, 6))
print("List to Tuple:", list_to_tuple)      # Output: (100, 200, 300)
print("String to Tuple:", string_to_tuple)  # Output: ('h', 'e', 'l', 'l', 'o')

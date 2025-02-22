# Python String Indexing - Complete Guide for Absolute Beginners

# What is String Indexing?
# - String indexing allows you to access individual characters in a string.
# - Each character in a string has an **index** (position).
# - Indexing starts from 0 (first character) and goes up to (length - 1).
# - Negative indexing allows accessing characters from the end.

# Example String:
text = "Python"

# Positive Indexing (Left to Right)
# P  y  t  h  o  n
# 0  1  2  3  4  5

# Negative Indexing (Right to Left)
# P  y  t  h  o  n
#-6 -5 -4 -3 -2 -1


# 1. Accessing Characters Using Positive Indexing
# Use square brackets [ ] with the index to get a character.

print(text[0])  # Output: 'P' (First character)
print(text[3])  # Output: 'h' (Fourth character)
print(text[5])  # Output: 'n' (Last character using positive indexing)


# 2. Accessing Characters Using Negative Indexing
# Use negative index to access characters from the end.

print(text[-1])  # Output: 'n' (Last character)
print(text[-3])  # Output: 'h' (Third-last character)
print(text[-6])  # Output: 'P' (First character using negative indexing)


# 3. Using Indexing in a Loop
# We can use indexing in a loop to iterate over each character.

for i in range(len(text)):
    print(f"Character at index {i}: {text[i]}")

# Output:
# Character at index 0: P
# Character at index 1: y
# Character at index 2: t
# Character at index 3: h
# Character at index 4: o
# Character at index 5: n


# 4. String Slicing (Using Index Ranges)
# Slicing allows extracting a portion of a string using [start:end:step].

substring = text[1:4]  # Extracts characters from index 1 to 3 (4 is excluded)
print(substring)  # Output: 'yth'

# Using negative indexes
print(text[-4:-1])  # Output: 'tho'


# 5. Omitting Start or End Index
# If start is omitted, it defaults to 0. If end is omitted, it goes till the last character.

print(text[:4])   # Output: 'Pyth' (From start to index 3)
print(text[2:])   # Output: 'thon' (From index 2 to the end)


# 6. Using Step in Slicing
# Step allows skipping characters in the string.

print(text[::2])   # Output: 'Pto' (Every second character)
print(text[::-1])  # Output: 'nohtyP' (Reversing the string)


# 7. Accessing Out-of-Range Index
# Trying to access an index beyond the length of the string causes an error.

# print(text[10])  # IndexError: string index out of range


# Summary of String Indexing:
"""
1. Positive Indexing: Starts from 0 and moves right.
2. Negative Indexing: Starts from -1 and moves left.
3. Slicing: Extracts substrings using [start:end:step].
4. Omitting Start or End: Defaults to beginning or end of the string.
5. Step in Slicing: Skips characters or reverses the string.
6. IndexError: Occurs if accessing an invalid index.
"""

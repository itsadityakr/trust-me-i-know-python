# Python String Indexing - Complete Guide

# Strings are indexed sequences of characters.
text = "Python"

# 1. **Indexing Basics**
# Positive Indexing (Left to Right)
# P  y  t  h  o  n
# 0  1  2  3  4  5

# Negative Indexing (Right to Left)
# P  y  t  h  o  n
#-6 -5 -4 -3 -2 -1

print(text[0])   # 'P' (First character)
print(text[-1])  # 'n' (Last character)

# 2. **Looping Through Characters**
for i in range(len(text)):
    print(f"Character at index {i}: {text[i]}")

# 3. **String Slicing** (Extracting Substrings)
print(text[1:4])   # 'yth' (From index 1 to 3)
print(text[-4:-1]) # 'tho' (Negative indexes)
print(text[:4])    # 'Pyth' (From start to index 3)
print(text[2:])    # 'thon' (From index 2 to end)
print(text[::2])   # 'Pto' (Every second character)
print(text[::-1])  # 'nohtyP' (Reversed string)

# 4. **IndexError Example**
# print(text[10])  # Causes IndexError: string index out of range

# **Summary**
"""
1. Positive Indexing (0 to len-1)  
2. Negative Indexing (-1 to -len)  
3. Slicing: [start:end:step]  
4. Omitting Start/End: Defaults to full range  
5. Step: Skips characters or reverses the string  
6. Out-of-Range Indexing raises an error  
"""

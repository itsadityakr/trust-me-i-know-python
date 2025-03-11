# Python Set and All Its Methods with Examples

# A set is an unordered collection of unique elements.
# It is defined using curly braces {} or the set() constructor.

# Creating a sample set
numsSet = {1, 2, 3, 4, 5}

# 1. add(x): Adds an element to the set
numsSet.add(6)
# Output: {1, 2, 3, 4, 5, 6}

# 2. update(iterable): Adds multiple elements to the set
numsSet.update([7, 8, 9])
# Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 3. remove(x): Removes an element from the set; raises KeyError if not found
numsSet.remove(4)
# Output: {1, 2, 3, 5, 6, 7, 8, 9}

# 4. discard(x): Removes an element if present; does nothing if not found
numsSet.discard(10)  # No error even if 10 is not present
# Output: {1, 2, 3, 5, 6, 7, 8, 9}

# 5. pop(): Removes and returns a random element from the set
removed_element = numsSet.pop()
# Output: (random element removed)

# 6. clear(): Removes all elements from the set
numsSet.clear()
# Output: set()

# Set Operations

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# 7. union(set): Returns a new set with elements from both sets
union_set = set_a.union(set_b)
# Output: {1, 2, 3, 4, 5, 6, 7, 8}

# 8. intersection(set): Returns a new set with elements common to both sets
intersection_set = set_a.intersection(set_b)
# Output: {4, 5}

# 9. difference(set): Returns a new set with elements in set_a but not in set_b
difference_set = set_a.difference(set_b)
# Output: {1, 2, 3}

# 10. symmetric_difference(set): Returns a new set with elements in either set, but not both
symmetric_diff_set = set_a.symmetric_difference(set_b)
# Output: {1, 2, 3, 6, 7, 8}

# 11. issubset(set): Checks if set_a is a subset of set_b
is_subset = {1, 2}.issubset(set_a)
# Output: True

# 12. issuperset(set): Checks if set_a is a superset of set_b
is_superset = set_a.issuperset({2, 3})
# Output: True

# 13. isdisjoint(set): Checks if two sets have no elements in common
is_disjoint = set_a.isdisjoint({6, 7})
# Output: True

# In-place modifications

# 14. intersection_update(set): Keeps only elements found in both sets
set_a.intersection_update(set_b)
# Output: {4, 5}

# 15. difference_update(set): Removes elements found in another set
set_a = {1, 2, 3, 4, 5}
set_a.difference_update(set_b)
# Output: {1, 2, 3}

# 16. symmetric_difference_update(set): Updates the set with symmetric difference
set_a = {1, 2, 3, 4, 5}
set_a.symmetric_difference_update(set_b)
# Output: {1, 2, 3, 6, 7, 8}

# Frozen set (Immutable set)
frozen = frozenset([1, 2, 3, 4, 5])
# frozen.add(6)  # This would raise an AttributeError since frozensets are immutable

# Printing all results
print("Final Set:", numsSet)                 # Output: Final Set: set()
print("Removed Element:", removed_element)  # Output: (random element)
print("Union:", union_set)                  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print("Intersection:", intersection_set)    # Output: {4, 5}
print("Difference:", difference_set)        # Output: {1, 2, 3}
print("Symmetric Difference:", symmetric_diff_set)  # Output: {1, 2, 3, 6, 7, 8}
print("Is Subset:", is_subset)              # Output: True
print("Is Superset:", is_superset)          # Output: True
print("Is Disjoint:", is_disjoint)          # Output: True
print("Frozen Set:", frozen)                # Output: frozenset({1, 2, 3, 4, 5})

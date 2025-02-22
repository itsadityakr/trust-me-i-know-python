# Logical operators: and, or, not

# 1. Logical AND (`and`) → True only if both conditions are True
a, b = True, False
print(a and b)  # False

x, y = 10, 5
print(x > 5 and y < 10)  # True
print(x > 15 and y < 10)  # False

# 2. Logical OR (`or`) → True if at least one condition is True
c, d = True, False
print(c or d)  # True

print(x > 15 or y < 10)  # True
print(x > 15 or y > 10)  # False

# 3. Logical NOT (`not`) → Reverses boolean value
e = True
print(not e)  # False

print(not (x > 5))  # False
print(not (x < 5))  # True

# Short-Circuit Evaluation
def check_and():
    print("Checking second condition...")
    return True

print(False and check_and())  # False (function not called)

def check_or():
    print("Checking second condition...")
    return True

print(True or check_or())  # True (function not called)

# Logical operators in conditions
age, has_id = 20, True
if age >= 18 and has_id:
    print("You are allowed to enter.")
else:
    print("Access denied.")

is_student, has_discount_code = False, True
if is_student or has_discount_code:
    print("You get a discount!")
else:
    print("No discount available.")

# Logical operators with lists and strings
list1, list2 = [1, 2, 3], []
print(list1 and "Hello")  # "Hello"
print(list2 and "Hello")  # []

print(list1 or "Default")  # [1, 2, 3]
print(list2 or "Default")  # "Default"

text = ""
print(not text)  # True
text = "Python"
print(not text)  # False

# Logical operators in list comprehensions
numbers = [10, 15, 20, 25, 30]
even_numbers = [num for num in numbers if num % 2 == 0 and num > 15]
print(even_numbers)  # [20, 30]

filtered_numbers = [num for num in numbers if num < 15 or num > 25]
print(filtered_numbers)  # [10, 30]

# Summary:
"""
1. `and` → True if both conditions are True.  
2. `or` → True if at least one condition is True.  
3. `not` → Reverses boolean value.  
4. Short-circuiting: `and` stops at False, `or` stops at True.  
5. Works with numbers, strings, lists, and functions.  
"""

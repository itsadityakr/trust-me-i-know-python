# Conditional operators compare values and return True or False.

# 1. Equal to (==)
a, b = 10, 20
print(a == b)  # False
print(a == 10)  # True

# 2. Not equal to (!=)
x, y = 5, 5
print(x != y)  # False
print(x != 10)  # True

# 3. Greater than (>)
num1, num2 = 15, 10
print(num1 > num2)  # True
print(num2 > num1)  # False

# 4. Less than (<)
age1, age2 = 18, 21
print(age1 < age2)  # True
print(age2 < age1)  # False

# 5. Greater than or equal to (>=)
score1, score2 = 90, 90
print(score1 >= score2)  # True
print(95 >= score2)  # True
print(85 >= score2)  # False

# 6. Less than or equal to (<=)
price1, price2 = 100, 120
print(price1 <= price2)  # True
print(price1 <= 100)  # True
print(150 <= price2)  # False

# Using Conditional Operators in If-Else Statements
temperature = 30
if temperature > 35:
    print("It's a hot day.")
else:
    print("It's not too hot.")

age = 17
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Conditional Operators with Strings
name1, name2 = "Alice", "Bob"
print(name1 == "Alice")  # True
print(name1 != name2)  # True

# Conditional Operators in Lists
list1, list2, list3 = [1, 2, 3], [1, 2, 3], [4, 5, 6]
print(list1 == list2)  # True
print(list1 != list3)  # True

# Summary:
"""
1. `==` → True if values are equal.
2. `!=` → True if values are different.
3. `>` → True if left is greater.
4. `<` → True if left is smaller.
5. `>=` → True if left is greater or equal.
6. `<=` → True if left is smaller or equal.
"""

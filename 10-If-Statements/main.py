# 1. Basic if statement
x = 10
if x > 5:
    print("x is greater than 5")

# 2. if-else statement
y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is 5 or less")

# 3. if-elif-else statement
z = 0
if z > 0:
    print("z is positive")
elif z < 0:
    print("z is negative")
else:
    print("z is zero")

# 4. Nested if statements
age = 20
if age >= 18:
    print("You are an adult")
    if age >= 65:
        print("You are also a senior citizen")
    else:
        print("You are not a senior citizen yet")
else:
    print("You are a minor")

# 5. Logical operators in if statements
a = 7
b = 10

if a > 5 and b < 15:
    print("Both conditions are met")

if a > 10 or b < 15:
    print("At least one condition is met")

if not (a < 5):
    print("a is not less than 5")

# 6. Comparison operators
num = 10

if num == 10:
    print("num is exactly 10")

if num != 5:
    print("num is not 5")

if num >= 10:
    print("num is at least 10")

# 7. Membership operators
fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("Banana is in the list")

if "grape" not in fruits:
    print("Grape is not in the list")

# 8. Ternary (short-hand) if statement
n = 7
result = "Even" if n % 2 == 0 else "Odd"
print(result)

m = 0
if m:
    print(True)
else:
    print(False)

# Augmented Assignment Operators in Python
# These operators combine an arithmetic operation with assignment.

# Initial value
num = 20

# These two are exactly same [num = num+10] = [num += 10]

# Addition assignment
# num = num+10
num += 10  # Augmented assignment operator
print(num) # 30

# Subtraction assignment
# num = num-15
num -= 15
print(num) # 15

# Multiplication assignment
# num = num*10
num *= 10
print(num) #150

# Division assignment
# num = num/10
num /= 10 # --------------[1]
print(num) #15.0

# Exponentiation assignment
# num = num**2
num **= 2
print(num) # 225.0 (Gets converted to float on division done above at [1])

# Modulus assignment
# num = num%10
num %= 10 # # Finds remainder when divided by 10
print(num) # 5.0 as (225 % 10 = 5)
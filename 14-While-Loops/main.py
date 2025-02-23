# Python While Loop - Complete Guide

# 1. **Basic While Loop**
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# Output:
# Count: 1
# Count: 2
# Count: 3
# Count: 4
# Count: 5


# 2. **Avoiding Infinite Loops**
# Be careful! If the condition always remains True, the loop runs forever.

# while True:
#     print("This is an infinite loop")  # Warning: Runs forever


# 3. **Using `break` to Stop a Loop**
num = 1
while num <= 10:
    if num == 5:
        break  # Exit loop when num is 5
    print(num)
    num += 1

# Output: 1, 2, 3, 4


# 4. **Using `continue` to Skip an Iteration**
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue  # Skip printing 3
    print(num)

# Output: 1, 2, 4, 5


# 5. **Using `else` with While Loop**
num = 1
while num <= 3:
    print(num)
    num += 1
else:
    print("Loop finished!")  # Runs when loop ends normally

# Output:
# 1, 2, 3
# Loop finished!


# 6. **User Input While Loop**
while True:
    user_input = input("Enter 'exit' to stop: ")
    if user_input.lower() == "exit":
        break
    print("You entered:", user_input)


# 7. **Counter-Based While Loop**
counter = 10
while counter > 0:
    print("Counter:", counter)
    counter -= 2  # Decrease by 2

# Output: 10, 8, 6, 4, 2


# 8. **Nested While Loop**
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

# Output:
# i=1, j=1
# i=1, j=2
# i=2, j=1
# i=2, j=2
# i=3, j=1
# i=3, j=2


# 9. **Number Guessing Game (Practical Example)**
import random

secret_number = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess a number (1-10): "))
    attempts += 1
    if guess == secret_number:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")


# **Summary of While Loops**
"""
1. **Basic while loop** - Runs while condition is True.  
2. **Infinite loop** - Runs forever if the condition never changes.  
3. **`break`** - Exits the loop immediately.  
4. **`continue`** - Skips the current iteration.  
5. **`else`** - Runs when the loop ends normally.  
6. **User input loop** - Useful for interactive programs.  
7. **Counter-based loop** - Common in counting programs.  
8. **Nested while loop** - A loop inside another loop.  
9. **Practical example** - Number guessing game.  
"""

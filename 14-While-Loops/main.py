# Python While Loop - Complete Guide for Absolute Beginners

# What is a While Loop?
# - A `while` loop allows repeating a block of code as long as a condition is True.
# - The condition is checked before each iteration.
# - If the condition is False initially, the loop will not run.

# Syntax:
# while condition:
#     # Code to execute repeatedly

# Example 1: Basic While Loop
count = 1  # Initialize counter
while count <= 5:  # Condition
    print("Count:", count)
    count += 1  # Increment counter

# Output:
# Count: 1
# Count: 2
# Count: 3
# Count: 4
# Count: 5


# 1. Infinite Loop (Avoid Mistakes)
# - If the condition always remains True, the loop runs forever.
# - To stop, use Ctrl + C in the terminal or `break` inside the loop.

# Example 2: Infinite Loop (Warning: Do not run)
# while True:
#     print("This is an infinite loop")  # Runs forever


# 2. Using `break` to Stop a Loop
# - `break` immediately stops the loop, even if the condition is still True.

print("Using break:")
num = 1
while num <= 10:
    if num == 5:
        break  # Exit the loop when num is 5
    print(num)
    num += 1

# Output:
# 1
# 2
# 3
# 4


# 3. Using `continue` to Skip Iteration
# - `continue` skips the rest of the code for the current iteration and goes to the next one.

print("Using continue:")
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue  # Skip printing 3
    print(num)

# Output:
# 1
# 2
# 4
# 5


# 4. Using `else` with While Loop
# - The `else` block runs if the loop exits normally (without `break`).

print("Using else:")
num = 1
while num <= 3:
    print(num)
    num += 1
else:
    print("Loop finished!")  # Runs when loop ends normally

# Output:
# 1
# 2
# 3
# Loop finished!


# 5. Using a While Loop with User Input
# - Useful for interactive programs.

print("Using while loop for user input:")
while True:
    user_input = input("Enter 'exit' to stop: ")
    if user_input.lower() == "exit":
        break  # Stop the loop
    print("You entered:", user_input)


# 6. While Loop with a Counter
# - Common use case for counting iterations.

print("Counting with while loop:")
counter = 10
while counter > 0:
    print("Counter:", counter)
    counter -= 2  # Decrease by 2 each time

# Output:
# Counter: 10
# Counter: 8
# Counter: 6
# Counter: 4
# Counter: 2


# 7. Nested While Loop
# - A while loop inside another while loop.

print("Nested while loop:")
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


# 8. Using While Loop for Number Guessing Game
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

# This program asks the user to guess a random number until they get it right.


# Summary of While Loops:
"""
1. Basic while loop: Runs while condition is True.
2. Infinite loop: Runs forever if condition never changes.
3. `break`: Exits the loop immediately.
4. `continue`: Skips the rest of the iteration and starts the next one.
5. `else`: Runs when the loop exits normally.
6. User input while loop: Repeats until user decides to stop.
7. Counter-based while loop: Common in counting programs.
8. Nested while loop: A loop inside another loop.
9. Practical example: Number guessing game.
"""


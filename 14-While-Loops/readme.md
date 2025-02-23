
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

# While Loop

## **What is a While Loop?**  
- A `while` loop allows repeating a block of code as long as a condition is `True`.  
- The condition is checked before each iteration.  
- If the condition is `False` initially, the loop will not run.  

### **Syntax:**  
```python
while condition:
    # Code to execute repeatedly
```

---

## **1. Basic While Loop**  

```python
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
```

---

## **2. Infinite Loop (Avoid Mistakes)**  
- If the condition always remains `True`, the loop runs forever.  
- To stop, use `Ctrl + C` in the terminal or `break` inside the loop.  

```python
# Warning: Do not run!
# while True:
#     print("This is an infinite loop")  # Runs forever
```

---

## **3. Using `break` to Stop a Loop**  
- `break` immediately stops the loop, even if the condition is still `True`.  

```python
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
```

---

## **4. Using `continue` to Skip Iteration**  
- `continue` skips the rest of the code for the current iteration and moves to the next one.  

```python
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
```

---

## **5. Using `else` with While Loop**  
- The `else` block runs if the loop exits normally (without `break`).  

```python
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
```

---

## **6. Using a While Loop with User Input**  
- Useful for interactive programs.  

```python
print("Using while loop for user input:")

while True:
    user_input = input("Enter 'exit' to stop: ")
    if user_input.lower() == "exit":
        break  # Stop the loop
    print("You entered:", user_input)
```

---

## **7. While Loop with a Counter**  
- Common use case for counting iterations.  

```python
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
```

---

## **8. Nested While Loop**  
- A while loop inside another while loop.  

```python
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
```

---

## **9. Using While Loop for Number Guessing Game**  
A practical example using a `while` loop to create an interactive game.  

```python
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
```

---

## **10. Edge Cases in While Loops**  

### **1. Condition Never Becomes False**  
A `while` loop must have a termination condition; otherwise, it results in an infinite loop.  

```python
x = 1
while x > 0:  # Always True, infinite loop
    print(x)
    x += 1  # This will never stop naturally
```

---

### **2. Forgetting to Increment the Counter**  
If the counter inside the loop is not updated, it results in an infinite loop.  

```python
x = 1
while x < 5:
    print(x)  # This will run indefinitely because x is never incremented
```

---

### **3. Using `break` Without an Exit Condition**  
Using `break` without an external exit condition can make the loop unpredictable.  

```python
while True:
    user_input = input("Enter something: ")
    if len(user_input) > 5:  # Arbitrary condition
        break  # Exits the loop
```

---

### **4. Using `else` with a `break` Statement**  
If `break` is used, the `else` block will not execute.  

```python
x = 1
while x < 5:
    if x == 3:
        break  # Exits before reaching else
    print(x)
    x += 1
else:
    print("Loop completed!")  # This will not run

# Output:
# 1
# 2
```

---

## **11. Summary of While Loops**  

### **Basic Concepts**  
- **Basic while loop:** Runs while the condition is `True`.  
- **Infinite loop:** Runs forever if the condition never changes.  
- **`break`:** Exits the loop immediately.  
- **`continue`:** Skips the rest of the iteration and starts the next one.  
- **`else`:** Runs when the loop exits normally.  

### **Common Use Cases**  
- **User input while loop:** Repeats until the user decides to stop.  
- **Counter-based while loop:** Useful for counting iterations.  
- **Nested while loop:** A loop inside another loop.  
- **Practical example:** Number guessing game.  

---

## **Conclusion**  

Mastering `while` loops helps in creating efficient loops that can handle user input, perform repetitive tasks, and implement logic-driven programs. Using `break`, `continue`, and `else` effectively allows for better control and optimization of loops.

![Static Badge](https://img.shields.io/badge/Aditya%20Kumar-black?style=for-the-badge&logo=atlasos&logoColor=%23ffffff)
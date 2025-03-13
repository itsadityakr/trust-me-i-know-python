
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

---

# Random Numbers in Python

Python provides the `random` module to generate random numbers and perform random operations. Below are some common use cases and examples with detailed comments.

---

## 1. Generating Random Integers

To generate random integers, use the `random.randint()` function. It takes two arguments: the lower and upper bounds (inclusive).

```python
import random  # Import the random module to use its functions

# Generate a random integer between 1 and 10 (inclusive)
random_number = random.randint(1, 10)  # randint() includes both 1 and 10
print("Random Integer:", random_number)  # Print the generated random number
```

Output (example):
```
Random Integer: 7
```

---

## 2. Generating Random Floats

To generate random floating-point numbers, use the `random.random()` function (for numbers between 0 and 1) or `random.uniform()` (for a custom range).

```python
import random  # Import the random module

# Generate a random float between 0 and 1
random_float = random.random()  # random() generates a float in [0.0, 1.0)
print("Random Float (0 to 1):", random_float)  # Print the generated float

# Generate a random float between 5.0 and 10.0
random_float_range = random.uniform(5.0, 10.0)  # uniform() generates a float in [5.0, 10.0]
print("Random Float (5.0 to 10.0):", random_float_range)  # Print the generated float
```

Output (example):
```
Random Float (0 to 1): 0.634523
Random Float (5.0 to 10.0): 7.891234
```

---

## 3. Selecting Random Elements

To select a random element from a list, use the `random.choice()` function. To select multiple unique elements, use `random.sample()`.

```python
import random  # Import the random module

# Define a list of items
my_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Select a single random element from the list
random_element = random.choice(my_list)  # choice() picks one element randomly
print("Random Element:", random_element)  # Print the selected element

# Select 3 unique random elements from the list
random_elements = random.sample(my_list, 3)  # sample() picks 3 unique elements
print("Random Elements:", random_elements)  # Print the selected elements
```

Output (example):
```
Random Element: banana
Random Elements: ['cherry', 'date', 'apple']
```

---

## 4. Shuffling a List

To shuffle a list in place, use the `random.shuffle()` function. This modifies the original list.

```python
import random  # Import the random module

# Define a list of numbers
my_list = [1, 2, 3, 4, 5]

# Shuffle the list in place
random.shuffle(my_list)  # shuffle() modifies the original list
print("Shuffled List:", my_list)  # Print the shuffled list
```

Output (example):
```
Shuffled List: [3, 1, 5, 2, 4]
```

---

## 5. Seeding Random Numbers

To ensure reproducibility, you can set a seed using `random.seed()`. This ensures that the same sequence of random numbers is generated every time the program runs.

```python
import random  # Import the random module

# Set a seed for reproducibility
random.seed(42)  # Seed ensures the same sequence of random numbers

# Generate random numbers
print("Random Number 1:", random.randint(1, 100))  # Generate and print a random number
print("Random Number 2:", random.randint(1, 100))  # Generate and print another random number

# Reset the seed to get the same sequence again
random.seed(42)  # Reset the seed to the same value
print("Random Number 1 (with seed):", random.randint(1, 100))  # Same as first random number
print("Random Number 2 (with seed):", random.randint(1, 100))  # Same as second random number
```

Output:
```
Random Number 1: 82
Random Number 2: 15
Random Number 1 (with seed): 82
Random Number 2 (with seed): 15
```

---

## Summary of Functions

- `random.randint(a, b)`: Generates a random integer between `a` and `b` (inclusive).
- `random.random()`: Generates a random float between 0 and 1 (exclusive of 1).
- `random.uniform(a, b)`: Generates a random float between `a` and `b` (inclusive of both bounds).
- `random.choice(seq)`: Selects a random element from a sequence (e.g., a list or tuple).
- `random.sample(seq, k)`: Selects `k` unique random elements from a sequence.
- `random.shuffle(seq)`: Shuffles a list in place (modifies the original list).
- `random.seed(a)`: Sets the seed for reproducibility (ensures the same sequence of random numbers).

---

![Static Badge](https://img.shields.io/badge/Aditya%20Kumar-black?style=for-the-badge&logo=atlasos&logoColor=%23ffffff)
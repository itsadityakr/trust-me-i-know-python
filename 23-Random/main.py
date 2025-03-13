import random  # Import the random module to use its functions


# Function to generate a random integer between 1 and 10 (inclusive)
def generate_random_integer():
    """
    Generates a random integer within the range of 1 to 10 (inclusive).
    Uses random.randint(a, b), where 'a' and 'b' define the range.
    Example output: 7
    """
    return random.randint(1, 10)  # Example output: 7


# Function to generate a random floating-point number between 0 and 1
def generate_random_float():
    """
    Generates a random float in the range [0.0, 1.0).
    Uses random.random(), which returns a float greater than or equal to 0.0 and less than 1.0.
    Example output: 0.634523
    """
    return random.random()  # Example output: 0.634523


# Function to generate a random float between a specific range (5.0 and 10.0)
def generate_random_float_range():
    """
    Generates a random floating-point number between 5.0 and 10.0.
    Uses random.uniform(a, b), which returns a float within the specified range.
    Example output: 7.891234
    """
    return random.uniform(5.0, 10.0)  # Example output: 7.891234


# Function to select a single random element from a given list
def select_random_element(my_list):
    """
    Selects and returns a random element from a given list.
    Uses random.choice(seq), which picks one element randomly.
    Example output: 'banana'
    """
    return random.choice(my_list)  # Example output: 'banana'


# Function to select multiple unique random elements from a given list
def select_multiple_random_elements(my_list, k=3):
    """
    Selects 'k' unique random elements from the provided list.
    Uses random.sample(seq, k), which picks 'k' unique elements randomly.
    Example output: ['cherry', 'date', 'apple']
    """
    return random.sample(my_list, k)  # Example output: ['cherry', 'date', 'apple']


# Function to shuffle a list randomly
def shuffle_list(my_list):
    """
    Shuffles the elements of a given list in place.
    Uses random.shuffle(seq), which modifies the original list order.
    Example output: [3, 1, 5, 2, 4]
    """
    random.shuffle(my_list)  # Example output: [3, 1, 5, 2, 4]
    return my_list


# Function to set a seed for reproducibility and generate two random numbers
def seed_random_numbers(seed_value=42):
    """
    Sets a seed for random number generation to ensure reproducibility.
    Generates and returns two random numbers between 1 and 100.
    Example output: (82, 15)
    """
    random.seed(seed_value)  # Setting seed for reproducibility
    return random.randint(1, 100), random.randint(1, 100)  # Example output: (82, 15)


# Main execution block
if __name__ == "__main__":
    # Generating and printing a random integer
    print("Random Integer:", generate_random_integer())  # Example output: 7

    # Generating and printing random floating-point numbers
    print("Random Float (0 to 1):", generate_random_float())  # Example output: 0.634523
    print("Random Float (5.0 to 10.0):", generate_random_float_range())  # Example output: 7.891234

    # Selecting random elements from a predefined list
    my_list = ["apple", "banana", "cherry", "date", "elderberry"]
    print("Random Element:", select_random_element(my_list))  # Example output: 'banana'
    print("Random Elements:", select_multiple_random_elements(my_list))  # Example output: ['cherry', 'date', 'apple']

    # Shuffling a predefined list of numbers and printing the result
    my_numbers = [1, 2, 3, 4, 5]
    print("Shuffled List:", shuffle_list(my_numbers))  # Example output: [3, 1, 5, 2, 4]

    # Generating and printing reproducible random numbers using a seed
    num1, num2 = seed_random_numbers()
    print("Random Number 1 (with seed):", num1)  # Example output: 82
    print("Random Number 2 (with seed):", num2)  # Example output: 15

    # Resetting seed and generating again to verify reproducibility
    num1, num2 = seed_random_numbers()
    print("Random Number 1 (with seed again):", num1)  # Example output: 82
    print("Random Number 2 (with seed again):", num2)  # Example output: 15

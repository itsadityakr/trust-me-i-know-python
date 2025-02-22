# Introduction to Python

# 1. What is Python?
# A high-level, interpreted language known for readability and ease of use.
# Created by Guido van Rossum in 1991, it supports object-oriented and dynamic typing.

# 2. How Python Runs:
#    a) Code is written in a .py file.
#    b) The interpreter converts it to bytecode (.pyc).
#    c) The Python Virtual Machine (PVM) executes the bytecode.

# Example:
print("Hello, World!")  # Prints to the console

# 3. Why Use Python?
# Popular in web development (Django, Flask), data science (NumPy, TensorFlow), automation, game dev, and cybersecurity.

# 4. Python vs C, C++, Java:

# Advantages:
#    - **Simplicity:** Readable, concise syntax.
#    - **Dynamic Typing:** No need for type declarations.
#    - **Interpreted:** No compilation required.
#    - **Extensive Libraries:** Supports many tasks (NumPy, Pandas).
#    - **Memory Management:** Automatic garbage collection.
#    - **Platform Independence:** Runs on any OS.
#    - **Less Code:** Example:

# Swapping values in Python:
a, b = 5, 10
a, b = b, a  # One-line swap

# In C++:
"""
int temp = a;
a = b;
b = temp;
"""

# Disadvantages:
#    - **Slower Execution:** Interpreted, not compiled.
#    - **High Memory Use:** Due to dynamic typing.
#    - **Not Ideal for Mobile Development:** Java dominates Android.
#    - **Limited Multithreading:** Due to the Global Interpreter Lock (GIL).

# Conclusion:
# Python is beginner-friendly and great for automation, data science, and scripting.
# C++ is faster for performance-critical applications, and Java is preferred for mobile development.

# Running Python Code:
# Save the file as "script.py" and run:
#     python script.py

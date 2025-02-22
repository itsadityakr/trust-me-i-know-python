# Python Format Specifiers - Complete Guide for Absolute Beginners

# What is a Format Specifier?
# - Format specifiers define how values should be displayed.
# - Used with `format()` and f-strings (`f""`).
# - Control width, alignment, precision, type conversion, and more.

# Basic Syntax:
# "{:specifier}".format(value)
# f"{value:specifier}"


# 1. String Formatting
# - s → String conversion (default for text)

name = "Alice"
print("Hello, {:s}!".format(name))  # Output: "Hello, Alice!"
print(f"Hello, {name:s}!")  # Output: "Hello, Alice!"


# 2. Integer Formatting
# - d → Decimal (integer)
# - b → Binary
# - o → Octal
# - x → Hexadecimal (lowercase)
# - X → Hexadecimal (uppercase)

num = 255
print("Decimal: {:d}".format(num))  # Output: "Decimal: 255"
print("Binary: {:b}".format(num))   # Output: "Binary: 11111111"
print("Octal: {:o}".format(num))    # Output: "Octal: 377"
print("Hex (lower): {:x}".format(num))  # Output: "Hex (lower): ff"
print("Hex (upper): {:X}".format(num))  # Output: "Hex (upper): FF"


# 3. Floating-Point Formatting
# - f → Fixed-point notation
# - e → Scientific notation (lowercase)
# - E → Scientific notation (uppercase)
# - g → General format (auto chooses fixed-point or scientific)

pi = 3.141592653589
print("Fixed-point: {:.2f}".format(pi))  # Output: "Fixed-point: 3.14"
print("Scientific (lower): {:.2e}".format(pi))  # Output: "Scientific: 3.14e+00"
print("Scientific (upper): {:.2E}".format(pi))  # Output: "Scientific: 3.14E+00"
print("General format: {:.4g}".format(pi))  # Output: "General: 3.142"


# 4. Width and Alignment
# - < → Left-align
# - > → Right-align
# - ^ → Center-align

text = "Python"
print("|{:<10}|".format(text))  # Left-align: "|Python    |"
print("|{:>10}|".format(text))  # Right-align: "|    Python|"
print("|{:^10}|".format(text))  # Center-align: "|  Python  |"


# 5. Padding with Zeros
# - 0 → Pads with zeros

num = 42
print("Zero-padded: {:05d}".format(num))  # Output: "00042"


# 6. Sign Formatting
# - + → Always show sign (+ or -)
# - - → Show negative sign only (default)
# - space → Add a leading space for positive numbers

pos = 42
neg = -42
print("{:+d}".format(pos))  # Output: "+42"
print("{: d}".format(pos))  # Output: " 42" (Space instead of +)
print("{: d}".format(neg))  # Output: "-42"


# 7. Thousands Separator
# - , → Adds a comma separator for thousands

large_num = 1000000
print("{:,}".format(large_num))  # Output: "1,000,000"


# 8. Percentage Formatting
# - % → Converts to percentage (multiplies by 100 and adds % sign)

value = 0.85
print("{:.0%}".format(value))  # Output: "85%"


# 9. Combining Multiple Specifiers
print("{:>10,.2f}".format(1234567.8910))
# Output: " 1,234,567.89" (Right-aligned, 2 decimal places, comma separator)


# 10. Using f-strings (Python 3.6+)
# - Works like format(), but more readable.

name = "Alice"
age = 25
print(f"My name is {name}, and I am {age} years old.")  # Output: "My name is Alice, and I am 25 years old."

pi = 3.14159
print(f"Pi rounded: {pi:.2f}")  # Output: "Pi rounded: 3.14"


# Summary of Format Specifiers:
"""
1. Strings: {:s}
2. Integers: {:d}, {:b} (binary), {:o} (octal), {:x} (hex)
3. Floats: {:.2f}, {:.2e} (scientific), {:.2g} (general)
4. Alignment: {:<10} (left), {:>10} (right), {:^10} (center)
5. Padding: {:05d} (zero padding)
6. Signs: {:+d} (show sign), {: d} (space for positive)
7. Separators: {:,} (thousands separator)
8. Percentages: {:.0%} (percentage)
9. f-strings: f"{value:.2f}"
"""


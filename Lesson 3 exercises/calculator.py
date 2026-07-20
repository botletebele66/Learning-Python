# Task Overview
# Multi-Function Calculator
# Build a Python calculator called calculator.py that takes two numbers as input and performs all four basic arithmetic operations plus two advanced operations. The calculator must handle user input safely using type casting and display results clearly using f-strings.

# Requirements
# Use float(input()) to collect two numbers from the user
# Calculate and display: addition, subtraction, multiplication, division
# Calculate and display: floor division (//) and modulus (%)
# Round all results to 2 decimal places using round()
# Handle division by zero — if the second number is 0, display a friendly error message instead of crashing
# Display all results in a formatted table using f-strings
 

# Outcome of the task
# At the end of this task, you should be competent in creating and running a Python calculator that accepts numeric user input, performs arithmetic calculations using Python’s operators, applies type conversion, uses functions such as round() and abs(), handles division by zero appropriately, and displays results clearly using f-strings.

# Before progressing to the next unit, complete the Unit 3 Quiz to check your understanding of the key numerical operations, type conversion, and calculation concepts covered, identify any areas that may need further practice, and reinforce your learning.

num1 = (float(input("Please enter your first number: ")))
num2 = (float(input("Please enter your second number: ")))

print("Addition:         ", num1 + num2)
print("Subtraction:      ", num1 - num2)
print("Multiplication:   ", num1 * num2)

# Division – check for zero
if num2 != 0:
    print("True Division:    ", num1 / num2)      # always returns a float
    print("Floor Division:   ", num1 // num2)     # integer division, rounds down
    print("Modulus (remainder):", num1 % num2)    # remainder after floor division
else:
    print("Division by zero is not allowed.")

# Calculate and display: addition, subtraction, multiplication, division.
# print(int(num1 + num2))
# print(int(num1 - num2))
# print(int(num1 * num2))
# print(int(num1 / num2))

# # Calculate and display: floor division (//) and modulus (%)
# print(int(num1 // num2))
# print(int(num1 % num2))

# Round all results to 2 decimal places using round()
# this is very wrong
# print(int(num1 + num2).round(2.00))
# print(int(num1 - num2).round(2.00))
# print(int(num1 * num2).round(2.00))
# print(int(num1 / num2).round(2.00))
# print(int(num1 // num2).round(2.00))
# print(int(num1 % num2).round(2.00))

print(round(num1 + num2, 2.00))
print(round(num1 - num2, 2.00))
print(round(num1 * num2, 2.00))
print(round(num1 / num2, 2.00))    # Normal division
print(round(num1 // num2, 2.00))   # Floor division
print(round(num1 % num2, 2.00))    # Modulus (remainder)

# Handle division by zero — if the second number is 0, display a friendly error message instead of crashing
# division by 0 
# Check for zero before any division
if num2 == 0:
    print("Cannot divide by zero. Please restart with a non‑zero second number.")

    # All operations are safe now
    print(f"Addition:          {num1 + num2}")
    print(f"Subtraction:       {num1 - num2}")
    print(f"Multiplication:    {num1 * num2}")
    print(f"Division:          {num1 / num2}")
    print(f"Floor division:    {num1 // num2}")
    print(f"Modulus (remainder): {num1 % num2}")
# Unit 3: Arithmetic Operations and Type Casting

## Welcome to Unit 3

This unit introduces you to the **core mathematical operations** that form the foundation of calculations in Python programs. You will develop a comprehensive understanding of how Python performs arithmetic, evaluates numerical expressions, and how different data types interact with each other.

By mastering these concepts, you'll be equipped to:

- Perform accurate calculations
- Process numerical data effectively
- Build programs that handle user input appropriately
- Create robust multi-function calculators

---

## Learning Objectives

By the end of this unit, you will be able to:

✅ Perform arithmetic using Python's **seven operators**: `+`, `-`, `*`, `/`, `//`, `%`, `**`

✅ Explain the difference between **integer division** (`//`) and **regular division** (`/`)

✅ Convert between data types using **type casting**: `int()`, `float()`, and `str()`

✅ Apply **built-in functions** (`round()` and `abs()`) to manipulate numeric values

✅ Build a **multi-function calculator** using arithmetic operations and type casting

---

## 1. Python's Seven Arithmetic Operators

Python uses special symbols called **operators** to perform mathematical computations on values (known as **operands**). These are the seven fundamental arithmetic operators you need to master:

### 1.1 Addition (`+`)

Adds two numeric values together.

**Syntax:** `operand1 + operand2`

**Examples:**

```python
# Basic addition
result = 10 + 5
print(result)  # Output: 15

# Addition with floats
price = 19.99
tax = 2.50
total = price + tax
print(total)  # Output: 22.49

# String concatenation (different use)
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe
```

---

### 1.2 Subtraction (`-`)

Subtracts one value from another.

**Syntax:** `operand1 - operand2`

**Examples:**

```python
# Basic subtraction
balance = 1000
withdrawal = 250
remaining = balance - withdrawal
print(remaining)  # Output: 750

# Subtraction with floats
starting_temperature = 72.5
temperature_drop = 15.3
final_temperature = starting_temperature - temperature_drop
print(final_temperature)  # Output: 57.2

# Negative results
small = 5
large = 12
difference = small - large
print(difference)  # Output: -7
```

---

### 1.3 Multiplication (`*`)

Multiplies two values together.

**Syntax:** `operand1 * operand2`

**Examples:**

```python
# Basic multiplication
width = 10
height = 20
area = width * height
print(area)  # Output: 200

# Multiplication with decimals
quantity = 5
unit_price = 12.99
total_cost = quantity * unit_price
print(total_cost)  # Output: 64.95

# String repetition (different use)
dashes = "-" * 20
print(dashes)  # Output: --------------------
```

---

### 1.4 Division (`/`)

Divides the first operand by the second operand. **In Python 3, this always returns a floating-point number**, even if the numbers divide evenly.

**Syntax:** `operand1 / operand2`

**Key Point:** Unlike some older programming languages, Python 3's division operator (`/`) never returns an integer—it always produces a result with a decimal point.

**Examples:**

```python
# Division with result containing decimals
total_miles = 200
gallons_used = 8
miles_per_gallon = total_miles / gallons_used
print(miles_per_gallon)  # Output: 25.0 (notice the decimal point)

# Division resulting in decimals
minutes = 59
seconds_per_minute = 60
decimal_minutes = minutes / seconds_per_minute
print(decimal_minutes)  # Output: 0.9833333333333333

# Even division still returns a float in Python 3
clean_division = 20 / 4
print(clean_division)  # Output: 5.0 (not 5)
print(type(clean_division))  # Output: <class 'float'>
```

---

### 1.5 Floored Division (Integer Division) (`//`)

Divides two numbers and **truncates** (chops off) the remainder to return only the integer portion of the quotient. This is also called **floored division** because it rounds down to the nearest whole number.

**Syntax:** `operand1 // operand2`

**Key Difference from `/`:**

- `/` returns a float (decimal number)
- `//` returns an integer (whole number), discarding the remainder

**Examples:**

```python
# Floored division with remainder
total_items = 23
items_per_box = 5
complete_boxes = total_items // items_per_box
print(complete_boxes)  # Output: 4 (23 ÷ 5 = 4 remainder 3)

# Comparing / and //
print(20 / 3)   # Output: 6.666666666666667
print(20 // 3)  # Output: 6

print(10 / 2)   # Output: 5.0
print(10 // 2)  # Output: 5

# Floored division with negative numbers
print(-10 // 3)  # Output: -4 (rounds down to nearest integer)
```

**Use Cases:**

- Converting minutes to hours: `hours = total_minutes // 60`
- Determining how many complete groups you can make
- Array indexing calculations

---

### 1.6 Modulus (`%`)

Returns the **remainder** left over after integer division. This operator is useful for checking divisibility and cycling through patterns.

**Syntax:** `operand1 % operand2`

**Examples:**

```python
# Finding the remainder
total_items = 23
items_per_box = 5
leftover_items = total_items % 5
print(leftover_items)  # Output: 3 (23 = 4×5 + 3)

# Checking if a number is even
number = 14
if number % 2 == 0:
    print(f"{number} is even")  # Output: 14 is even
else:
    print(f"{number} is odd")

# Checking if a number is divisible by another
year = 2024
if year % 4 == 0:
    print(f"{year} is potentially a leap year")

# Cycling through values (like a clock)
hour = 25
actual_hour = hour % 24
print(actual_hour)  # Output: 1 (25th hour becomes 1st hour)
```

**Common Use Cases:**

- Checking divisibility (`n % 2 == 0` for even numbers)
- Finding remainders
- Creating cyclic patterns
- Implementing circular buffers

---

### 1.7 Exponentiation (`**`)

Raises the first operand to the power of the second operand (exponent).

**Syntax:** `base ** exponent`

**Examples:**

```python
# Basic exponentiation
result = 5 ** 2
print(result)  # Output: 25 (5 squared)

# Cubing a number
side_length = 3
volume = side_length ** 3
print(volume)  # Output: 27

# Fractional exponents (calculating roots)
number = 16
square_root = number ** 0.5
print(square_root)  # Output: 4.0

cube_root = 27 ** (1/3)
print(cube_root)  # Output: 3.0

# Powers of 2 (common in computer science)
print(2 ** 10)  # Output: 1024

# Negative exponents (reciprocals)
print(2 ** -1)  # Output: 0.5
print(10 ** -2)  # Output: 0.01
```

**Use Cases:**

- Calculating area and volume
- Computing compound interest
- Scientific calculations
- Working with exponential growth/decay

---

## 2. Integer Division (`//`) vs. Regular Division (`/`)

### Understanding the Difference

This is a critical distinction in Python that affects many programs:

| Aspect | Division `/` | Floored Division `//` |
| --- | --- | --- |
| **Result Type** | Always returns a `float` | Returns an `int` |
| **Decimal Places** | Includes all decimal places | Removes remainder entirely |
| **Python 3 Behavior** | Always shows decimals (e.g., `5.0`) | Returns whole number only |
| **Rounding Method** | Not applicable | Rounds **down** to nearest integer |

### Detailed Comparison

```python
# Example 1: Numbers that divide evenly
print(20 / 4)   # Output: 5.0 (float with decimal point)
print(20 // 4)  # Output: 5 (integer)

# Example 2: Numbers with remainder
print(20 / 3)   # Output: 6.666666666666667
print(20 // 3)  # Output: 6

# Example 3: Negative numbers
print(-20 / 3)   # Output: -6.666666666666667
print(-20 // 3)  # Output: -7 (rounds DOWN, not toward zero)

# Example 4: Working with time conversions
total_seconds = 3725
minutes = total_seconds / 60
print(minutes)  # Output: 62.08333333333333

whole_minutes = total_seconds // 60
print(whole_minutes)  # Output: 62 (complete minutes only)
```

### When to Use Each

**Use `/` when:**

- You need precise decimal results
- Calculating ratios or percentages
- Working with measurements that require precision

**Use `//` when:**

- You need only whole numbers
- Counting complete groups or batches
- Performing time/date calculations
- Converting units where only whole values make sense

---

## 3. Type Casting (Data Type Conversion)

### Why Type Casting Matters

When your program receives input from a user via the `input()` function, **it is always treated as a string (`str`)**, regardless of what the user types. To perform mathematical operations on this data, you must **convert** (or "cast") it to an appropriate numeric type.

### The Three Main Type Conversions

### 3.1 Converting to Integer: `int()`

Converts a value to an integer (whole number). When converting from a float, it **truncates** (cuts off) the decimal part rather than rounding it.

**Syntax:** `int(value)`

**Examples:**

```python
# Converting from string
user_age = input("Enter your age: ")
print(type(user_age))  # Output: <class 'str'>

age = int(user_age)
print(type(age))  # Output: <class 'int'>

# Converting from float (truncation, not rounding)
decimal_value = 3.99
integer_value = int(decimal_value)
print(integer_value)  # Output: 3 (not 4!)

decimal_value = 3.14
integer_value = int(decimal_value)
print(integer_value)  # Output: 3

# Practical example: simple calculator
num1 = int(input("Enter first number: "))  # "15" → 15
num2 = int(input("Enter second number: "))  # "8" → 8
sum_result = num1 + num2
print(f"The sum is: {sum_result}")

# Converting boolean to integer
print(int(True))   # Output: 1
print(int(False))  # Output: 0
```

**Important Note:** The `int()` function **truncates**, it does not round:

- `int(3.99)` → `3` (not 4)
- `int(3.14)` → `3` (not 3)
- `int(-3.99)` → `-3` (not -4)

---

### 3.2 Converting to Float: `float()`

Converts integers or compatible strings into numbers with decimal points. This is essential when you need decimal precision.

**Syntax:** `float(value)`

**Examples:**

```python
# Converting from string
user_height = input("Enter your height in meters: ")
height = float(user_height)
print(type(height))  # Output: <class 'float'>

# Converting from integer
whole_number = 42
decimal_number = float(whole_number)
print(decimal_number)  # Output: 42.0

# Practical example: calculating average
grade1 = int(input("Grade 1: "))   # "85" → 85
grade2 = int(input("Grade 2: "))   # "90" → 90
grade3 = int(input("Grade 3: "))   # "88" → 88

average = (grade1 + grade2 + grade3) / 3
print(f"Average: {average}")  # Output: Average: 87.66666666666667

# Converting boolean to float
print(float(True))   # Output: 1.0
print(float(False))  # Output: 0.0
```

---

### 3.3 Converting to String: `str()`

Converts numeric values back into strings. This is essential when you need to concatenate a number with text or prepare output.

**Syntax:** `str(value)`

**Examples:**

```python
# Converting integer to string
age = 25
message = "I am " + str(age) + " years old"
print(message)  # Output: I am 25 years old

# Converting float to string
price = 19.99
label = "Price: $" + str(price)
print(label)  # Output: Price: $19.99

# Without str() conversion (this causes an error)
# message = "I am " + 25 + " years old"  # TypeError!

# Using f-strings (modern approach, doesn't require str())
product_count = 42
product_price = 12.50
print(f"You have {product_count} items at ${product_price} each")
# Output: You have 42 items at $12.50 each
```

---

### Type Casting Workflow

```python
# Step 1: Get input (always a string)
user_input = input("Enter a number: ")  # "42"

# Step 2: Cast to appropriate type
number = int(user_input)  # "42" → 42

# Step 3: Perform calculations
result = number * 2  # 84

# Step 4: Cast back to string for output
output = str(result)  # 84 → "84"
print("Result: " + output)
```

---

## 4. Manipulating Numeric Values

Python provides built-in functions to refine and manipulate your numeric data.

### 4.1 Rounding Numbers: `round()`

The `round()` function rounds a numeric value to a specified number of decimal places. This is particularly useful for displaying monetary values, percentages, and other measurements.

**Syntax:** `round(number, ndigits)`

**Parameters:**

- `number`: The value to round
- `ndigits`: Number of decimal places (optional, defaults to 0)

**Examples:**

```python
# Rounding to nearest integer
value = 3.7
rounded = round(value)
print(rounded)  # Output: 4

value = 3.4
rounded = round(value)
print(rounded)  # Output: 3

# Rounding to specific decimal places
price = 19.9856
rounded_price = round(price, 2)
print(rounded_price)  # Output: 19.99

# Calculating and rounding a pay rate
hours = 40
gross_pay = 850
hourly_rate = gross_pay / hours
rounded_rate = round(hourly_rate, 2)
print(f"Hourly rate: ${rounded_rate}")  # Output: Hourly rate: $21.25

# Rounding percentages
correct_answers = 18
total_questions = 25
percentage = (correct_answers / total_questions) * 100
rounded_percentage = round(percentage, 1)
print(f"Score: {rounded_percentage}%")  # Output: Score: 72.0%

# Rounding to nearest 10 (using negative digits)
number = 1234
rounded_tens = round(number, -1)
print(rounded_tens)  # Output: 1230

rounded_hundreds = round(number, -2)
print(rounded_hundreds)  # Output: 1200
```

**Key Points:**

- `round()` uses **banker's rounding** (rounds to nearest even number when exactly between two values)
- `round()` without a second argument rounds to the nearest integer
- Negative values for `ndigits` round to the left of the decimal point

---

### 4.2 Finding Absolute Value: `abs()`

The `abs()` function returns the **absolute value** of a number—its distance from zero, always as a positive number. This is useful when you care about magnitude but not direction.

**Syntax:** `abs(number)`

**Examples:**

```python
# Basic absolute value
temperature_change = -15
magnitude = abs(temperature_change)
print(magnitude)  # Output: 15

# Finding distance between two points
starting_position = 100
ending_position = 45
distance_traveled = abs(ending_position - starting_position)
print(distance_traveled)  # Output: 55

# Working with positive and negative numbers
print(abs(42))    # Output: 42
print(abs(-42))   # Output: 42
print(abs(3.14))  # Output: 3.14
print(abs(-3.14)) # Output: 3.14

# Checking if values are approximately equal
value1 = 10.1
value2 = 10.0
difference = abs(value1 - value2)
if difference < 0.2:
    print("Values are approximately equal")  # This prints

# Calculating deviation from average
scores = [85, 92, 78, 95, 88]
average = sum(scores) / len(scores)
print(f"Average: {average}")  # Output: Average: 87.6

for score in scores:
    deviation = abs(score - average)
    print(f"Score {score} deviates by {deviation:.1f}")
```

**Use Cases:**

- Measuring distance or magnitude
- Checking if a value is within a range
- Calculating deviations or errors
- Working with coordinates

---

## 5. Building a Multi-Function Calculator

By combining arithmetic operators with type casting, you can create a functional calculator that handles user input effectively. Here's a complete example:

### 5.1 Basic Two-Number Calculator

```python
# Simple calculator for two numbers

# Get user input and convert to float
print("=== Simple Calculator ===")
num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")

# Type casting: convert strings to floats
num1 = float(num1_str)
num2 = float(num2_str)

# Perform calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
modulus = num1 % num2
exponent = num1 ** num2

# Display results (formatted nicely)
print(f"\n{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {round(division, 2)}")
print(f"{num1} // {num2} = {int(floor_division)}")
print(f"{num1} % {num2} = {round(modulus, 2)}")
print(f"{num1} ** {num2} = {exponent}")
```

**Sample Output:**

```text
=== Simple Calculator ===
Enter the first number: 20
Enter the second number: 3

20.0 + 3.0 = 23.0
20.0 - 3.0 = 17.0
20.0 * 3.0 = 60.0
20.0 / 3.0 = 6.67
20.0 // 3.0 = 6
20.0 % 3.0 = 2.0
20.0 ** 3.0 = 8000.0
```

---

### 5.2 Advanced Calculator with Operation Selection

```python
# Advanced calculator that lets users choose the operation

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def floor_divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a // b

def modulus(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a % b

def exponent(a, b):
    return a ** b

# Main program
print("=== Multi-Function Calculator ===")
print("Operations: + (add), - (subtract), * (multiply), / (divide),")
print("           // (floor divide), % (modulus), ** (exponent)")

try:
    # Get input
    num1 = float(input("\nEnter first number: "))
    operation = input("Enter operation: ")
    num2 = float(input("Enter second number: "))
    
    # Perform calculation based on operation
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    elif operation == '//':
        result = floor_divide(num1, num2)
    elif operation == '%':
        result = modulus(num1, num2)
    elif operation == '**':
        result = exponent(num1, num2)
    else:
        result = "Error: Invalid operation"
    
    # Display result
    if isinstance(result, str):
        print(f"\n{result}")
    else:
        print(f"\n{num1} {operation} {num2} = {round(result, 2) if isinstance(result, float) else result}")

except ValueError:
    print("Error: Please enter valid numbers")
```

**Sample Output:**

```text
=== Multi-Function Calculator ===
Operations: + (add), - (subtract), * (multiply), / (divide),
           // (floor divide), % (modulus), ** (exponent)

Enter first number: 15.5
Enter operation: *
Enter second number: 3.2

15.5 * 3.2 = 49.6
```

---

### 5.3 Practical Application: Tip Calculator

```python
# Real-world example: calculating tip and total bill

print("=== Tip Calculator ===\n")

# Get input
bill_amount_str = input("Enter the bill amount: $")
tip_percent_str = input("Enter tip percentage (e.g., 15, 18, 20): ")

# Type casting
bill_amount = float(bill_amount_str)
tip_percent = float(tip_percent_str)

# Calculations
tip_amount = bill_amount * (tip_percent / 100)
total_amount = bill_amount + tip_amount

# Display results (rounded for currency)
print(f"\nBill Amount:    ${bill_amount:.2f}")
print(f"Tip ({tip_percent}%):       ${round(tip_amount, 2):.2f}")
print(f"Total Amount:   ${round(total_amount, 2):.2f}")
```

**Sample Output:**

```text
=== Tip Calculator ===

Enter the bill amount: $45.67
Enter tip percentage (e.g., 15, 18, 20): 18

Bill Amount:    $45.67
Tip (18.0%):       $8.22
Total Amount:   $53.89
```

---

## Quick Reference Cheat Sheet

### Arithmetic Operators

| Operator | Name | Example | Result |
| --- | --- | --- | --- |
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 5` | `50` |
| `/` | Division | `10 / 4` | `2.5` |
| `//` | Floor Division | `10 // 4` | `2` |
| `%` | Modulus | `10 % 3` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

### Type Conversion

```python
int(value)      # Convert to integer (truncates decimals)
float(value)    # Convert to float (adds decimals)
str(value)      # Convert to string
```

### Useful Functions

```python
round(number, decimals)  # Round to specified decimal places
abs(number)              # Get absolute value (distance from zero)
```

### Common Patterns

**Getting numeric input from user:**

```python
number = float(input("Enter a number: "))  # Always use float() or int()
```

**Formatting numeric output:**

```python
print(f"Value: ${price:.2f}")  # Shows 2 decimal places
print(f"Score: {round(score, 1)}%")  # Rounds to 1 decimal place
```

---

## Key Takeaways

1. **Python's seven operators** (`+`, `-`, `*`, `/`, `//`, `%`, `**`) form the foundation of mathematical programming

2. **Division (`/`) always returns a float** in Python 3; use floor division (`//`) for whole number results

3. **User input is always a string**; always use `int()` or `float()` to convert before doing math

4. **Type casting is essential** for robust programs that handle diverse data types

5. **Built-in functions** like `round()` and `abs()` extend your numeric manipulation capabilities

6. **Combining these concepts** allows you to build real-world applications like calculators, converters, and financial tools

---

## Practice Exercises

1. Create a program that calculates the area and perimeter of a rectangle
2. Build a BMI calculator that takes height and weight as input
3. Write a program that converts temperatures between Celsius and Fahrenheit
4. Create a time converter that converts seconds into hours, minutes, and seconds
5. Build a currency converter with user-specified exchange rates

---

*Unit 3 Complete* ✓

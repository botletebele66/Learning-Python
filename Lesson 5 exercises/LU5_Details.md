# Unit 5: Conditional Execution

Welcome to **Unit 5**! This unit focuses on how Python makes decisions using logical comparisons to control the flow of a program. By the end of this unit, you will be able to write scripts that respond dynamically to different inputs and data.

---

## Table of Contents

1. [Controlling Program Flow: `if`, `elif`, and `else`](#1-controlling-program-flow-if-elif-and-else)
2. [Using Comparison Operators](#2-using-comparison-operators)
3. [Combining Conditions with Logical Operators](#3-combining-conditions-with-logical-operators)
4. [Membership Testing with the `in` Keyword](#4-membership-testing-with-the-in-keyword)
5. [Nested Conditionals and `elif` Logic](#5-nested-conditionals-and-elif-logic)
6. [Advanced Error Handling: `try` and `except`](#6-advanced-error-handling-try-and-except)

---

## 1. Controlling Program Flow: `if`, `elif`, and `else`

Python uses conditional statements to check specific conditions and change the behavior of the program accordingly. These statements allow your program to make decisions based on data and execute different code paths.

### The `if` Statement

The `if` statement is the simplest form of conditional execution. It evaluates a boolean expression and only executes the indented code block if the condition is `True`. If the condition is `False`, the block is skipped.

**Syntax:**

```python
if condition:
    # Code block executed if condition is True
    statement1
    statement2
```

**Example:**

```python
score = 105
if score > 100:
    print("High score!")
```

**Output:**

```text
High score!
```

### The `else` Statement

The `else` statement provides an alternative execution path when you have exactly two possibilities. If the `if` condition is `False`, the `else` block executes instead.

These alternatives are called **branches** — your program chooses one path or the other.

**Syntax:**

```python
if condition:
    # Code block if condition is True
else:
    # Code block if condition is False
```

**Example:**

```python
score = 45
if score > 100:
    print("High score!")
else:
    print("Keep trying!")
```

**Output:**

```text
Keep trying!
```

### The `elif` Statement

The `elif` statement (short for "else if") allows you to chain multiple conditions together when there are more than two possibilities. Python evaluates each condition in order from top to bottom. As soon as one condition is `True`, that branch executes and all remaining conditions are skipped.

**Syntax:**

```python
if condition1:
    # Code block if condition1 is True
elif condition2:
    # Code block if condition1 is False and condition2 is True
elif condition3:
    # Code block if condition1 and condition2 are False and condition3 is True
else:
    # Code block if all conditions are False
```

**Example:**

```python
score = 75
if score > 100:
    print("Amazing!")
elif score > 50:
    print("Good job!")
else:
    print("Better luck next time.")
```

**Output:**

```text
Good job!
```

**Important Note:** You can have multiple `elif` statements, but only one `if` and one `else` per conditional block.

---

## 2. Using Comparison Operators

To create conditions for `if` statements, you use **comparison operators** to evaluate values. These expressions return a boolean value: either `True` or `False`.

### Comparison Operators Reference

| Operator | Meaning                  | Example  | Result  |
| -------- | ------------------------ | -------- | ------- |
| `==`     | Equal to                 | `5 == 5` | `True`  |
| `!=`     | Not equal to             | `5 != 3` | `True`  |
| `>`      | Greater than             | `5 > 3`  | `True`  |
| `<`      | Less than                | `5 < 3`  | `False` |
| `>=`     | Greater than or equal to | `5 >= 5` | `True`  |
| `<=`     | Less than or equal to    | `5 <= 3` | `False` |

**Important:** Do not confuse `==` (comparison) with `=` (assignment). Using `=` in an `if` statement will assign a value rather than compare it.

### Practical Examples

**Example 1: Checking Age**'

```python
age = 18
if age >= 18:
    print("You are an adult")
```

**Output:**

```text
You are an adult
```

'**Example 2: Checking String Equality**'

```python
username = "alice"
if username == "alice":
    print("Welcome, Alice!")
```

**Output:**

```text
Welcome, Alice!
```

**Example 3: Checking Inequality** '

```python
status = "inactive"
if status != "active":
    print("Account is not active")
```

**Output:**

```text
Account is not active
```

---

## 3. Combining Conditions with Logical Operators

You can create more complex decision-making logic by combining multiple boolean expressions using **logical operators**. This allows you to evaluate multiple conditions at once.

### Logical Operators

### `and` Operator

Returns `True` only if **both** individual conditions are `True`. If either condition is `False`, the result is `False`.

**Truth Table:**

| Condition A | Condition B | A `and` B |
| ----------- | ----------- | --------- |
| `True`      | `True`      | `True`    |
| `True`      | `False`     | `False`   |
| `False`     | `True`      | `False`   |
| `False`     | `False`     | `False`   |

**Example:**

```python
temperature = 25
raining = False

if temperature > 20 and not raining:
    print("Go for a walk")
```

**Output:**

```text
Go for a walk
```

### `or` Operator

Returns `True` if **at least one** of the conditions is `True`. It only returns `False` if both conditions are `False`.

**Truth Table:**

| Condition A | Condition B | A `or` B |
| ----------- | ----------- | -------- |
| `True`      | `True`      | `True`   |
| `True`      | `False`     | `True`   |
| `False`     | `True`      | `True`   |
| `False`     | `False`     | `False`  |

**Example:**

```python
day = "Saturday"
is_holiday = False

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
```

**Output:**

```text
It's the weekend!
```

### `not` Operator

Negates a boolean expression, flipping `True` to `False` and `False` to `True`.

**Truth Table:**

| Condition | `not` Condition |
| --------- | --------------- |
| `True`    | `False`         |
| `False`   | `True`          |

**Example:**

```python
is_raining = True

if not is_raining:
    print("No rain today")
else:
    print("Bring an umbrella")
```

**Output:**

```text
Bring an umbrella
```

### Complex Conditions

You can combine multiple logical operators to create sophisticated conditions:

```python
age = 25
income = 50000
credit_score = 720

if age >= 21 and income >= 30000 and credit_score >= 700:
    print("Loan approved!")
```

**Output:**

```text
Loan approved!
```

### Short-Circuit Evaluation

Python uses an optimization called **short-circuit evaluation**. It stops evaluating as soon as it knows the overall result:

- For `and`: If the first condition is `False`, the second condition is not checked (because the result is already `False`)
- For `or`: If the first condition is `True`, the second condition is not checked (because the result is already `True`)

This is useful for the **guardian pattern**, where you place a "guard" condition before a potentially dangerous operation:

```python
numerator = 10
denominator = 0

# Safe: checks denominator is not zero BEFORE dividing
if denominator != 0 and numerator / denominator > 5:
    print("Result is large")
```

Without the guard condition, the code would crash with a `ZeroDivisionError`.

---

## 4. Membership Testing with the `in` Keyword

The `in` operator checks whether a value exists within a sequence. It returns `True` if the value is found and `False` otherwise.

### Using `in` with Strings

The `in` operator checks if one string appears as a **substring** within another string.

```python
word = "banana"
if 'a' in word:
    print("The letter 'a' is in 'banana'")
```

**Output:**

```text
The letter 'a' is in 'banana'
```

**More Examples:**

```python
if 'ana' in 'banana':
    print("'ana' found in 'banana'")  # True

if 'xyz' in 'banana':
    print("'xyz' found in 'banana'")  # False (not printed)
```

### Using `in` with Lists

The `in` operator checks if a specific element exists anywhere in the list.

```python
fruits = ['banana', 'apple', 'orange', 'grape']

if 'apple' in fruits:
    print("Apple is in the fruit list")
```

**Output:**

```text
Apple is in the fruit list
```

**More Examples:**

```python
inventory = [101, 102, 103, 104]

if 103 in inventory:
    print("Product 103 is in stock")  # Printed

if 105 in inventory:
    print("Product 105 is in stock")  # Not printed
```

### Using `in` with Dictionaries

When used with a dictionary, the `in` operator checks if a **key** exists (not the value).

```python
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}

if 'name' in person:
    print("'name' key exists")  # Printed

if 'Alice' in person:
    print("'Alice' value exists")  # Not printed (checks keys, not values)
```

**Output:**

```text
'name' key exists
```

### Using `not in`

You can also use `not in` to check if something does NOT exist:

```python
colors = ['red', 'blue', 'green']

if 'yellow' not in colors:
    print("Yellow is not in the list")
```

**Output:**

```text
Yellow is not in the list
```

---

## 5. Nested Conditionals and `elif` Logic

### Nested Conditionals

You can place one conditional statement inside another to handle multi-layered decisions. The inner `if` statement only executes if the outer `if` condition is `True`.

**Example:**

```python
x = 5
y = 10

if x > 0:
    print("x is positive")
    if y > 0:
        print("y is also positive")
    else:
        print("y is negative")
else:
    print("x is negative")
```

**Output:**

```text
x is positive
y is also positive
```

### Simplifying Nested Conditionals

Nested conditionals can become difficult to read and understand. Often, it's more "Pythonic" to simplify them using logical operators.

**Nested (harder to read):**

```python
if x > 0:
    if y > 0:
        print("Both positive")
```

**Simplified (easier to read):**

```python
if x > 0 and y > 0:
    print("Both positive")
```

Both produce the same result, but the second version is clearer and more maintainable.

### `elif` vs. Separate `if` Statements

It's crucial to understand the difference between using `elif` and using multiple separate `if` statements.

#### Using `elif` (Mutually Exclusive)

Use `elif` when you have a series of mutually exclusive options where **only one branch should execute**. Python stops checking after the first `True` condition.

```python
grade = 85

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("F")
```

**Output:**

```text
B
```

Only `"B"` is printed. Python doesn't check the remaining conditions after finding the first `True`.

#### Using Separate `if` Statements (Independent)

If you use separate `if` statements instead of `elif`, Python checks **every single condition independently**, which might result in multiple blocks executing:

```python
grade = 85

if grade >= 90:
    print("A")
if grade >= 80:
    print("B")
if grade >= 70:
    print("C")
```

**Output:**

```text
B
C
```

Both `"B"` and `"C"` are printed because each `if` is evaluated independently, and both conditions are `True`.

**When to Use Each:**

- Use `elif` when only one option should be selected (grades, status levels, categories)
- Use separate `if` statements when multiple conditions can be true simultaneously (checking multiple independent flags)

### Complex Decision Trees

You can build sophisticated decision logic with multiple `elif` branches:

```python
score = 78
attendance = 0.95

if score >= 90 and attendance >= 0.95:
    print("Grade: A (Perfect attendance bonus)")
elif score >= 90:
    print("Grade: A")
elif score >= 80 and attendance >= 0.95:
    print("Grade: B (Excellent attendance)")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

**Output:**

```text
Grade: B (Excellent attendance)
```

---

## 6. Advanced Error Handling: `try` and `except`

While not strictly a conditional statement, the `try`/`except` structure is a form of conditional execution designed to handle **exceptions** (errors). It acts as an "insurance policy" on your code, allowing the program to catch an error and recover gracefully instead of crashing with a traceback.

### Basic Structure

**Syntax:**

```python
try:
    # Code that might cause an error
    dangerous_operation()
except ErrorType:
    # Code that runs if the specified error occurs
    handle_error()
```

### Common Exceptions

| Exception           | Cause                                         |
| ------------------- | --------------------------------------------- |
| `ValueError`        | Invalid value (e.g., converting "abc" to int) |
| `ZeroDivisionError` | Division by zero                              |
| `IndexError`        | List index out of range                       |
| `KeyError`          | Dictionary key doesn't exist                  |
| `TypeError`         | Wrong data type for operation                 |
| `FileNotFoundError` | File doesn't exist                            |

### Example 1: Handling User Input

```python
try:
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are an adult")
except ValueError:
    print("That's not a valid number!")
```

**If user enters "25":**

```text
Enter your age: 25
You are an adult
```

**If user enters "abc":**

```text
Enter your age: abc
That's not a valid number!
```

### Example 2: Handling Division by Zero

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

**Output:**

```text
Cannot divide by zero!
```

### Example 3: Handling List Index Errors

```python
numbers = [1, 2, 3]
try:
    print(numbers[5])
except IndexError:
    print("Index is out of range")
```

**Output:**

```text
Index is out of range
```

### Multiple Except Blocks

You can handle different types of errors with separate `except` blocks:

```python
try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = 100 / number
    print(f"Result: {result}")
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### Catching Any Exception

You can use a generic `except` clause to catch any exception:

```python
try:
    # Some code
    result = risky_operation()
except Exception:
    print("An error occurred!")
```

However, it's better practice to specify the exception type so you know what went wrong.

### The `else` and `finally` Clauses

The `else` clause runs only if no exception occurred in the `try` block:

```python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input")
else:
    print(f"You entered: {age}")
```

The `finally` clause runs regardless of whether an exception occurred. Useful for cleanup operations:

```python
try:
    file = open("data.txt")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close()  # Always executes
```

---

## Summary

In this unit, you've learned:

- How to use `if`, `elif`, and `else` for conditional execution
- Comparison operators for creating conditions
- Logical operators (`and`, `or`, `not`) for complex conditions
- The `in` operator for membership testing
- How to structure nested conditionals and choose between `elif` and separate `if` statements
- Basic error handling with `try`/`except`

These tools enable you to write intelligent programs that respond dynamically to different inputs and situations!

---

## Practice Problems

1. Write a program that asks for a number and determines if it's positive, negative, or zero.
2. Create a program that checks if a year is a leap year (divisible by 4, but not 100 unless also divisible by 400).
3. Write a program that grades students based on their score (A: 90+, B: 80+, C: 70+, F: below 70).
4. Create a program that validates a password (must be at least 8 characters and contain at least one number).
5. Write a program that handles user input safely using try/except to ensure the user enters a valid integer.

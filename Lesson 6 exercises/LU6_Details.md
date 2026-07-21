# Unit 6: Repetition in Python

Welcome to **Unit 6**! This unit introduces you to **repetition** in Python, enabling programs to perform tasks efficiently without rewriting the same code. You will explore different looping techniques for working with sequences, collections, and repeated user interactions. The unit also develops your understanding of how to control and customize loop behaviour for different situations. In addition, you will combine loops with conditional logic to solve more complex programming problems. Together, these concepts will help you write efficient, structured, and scalable Python programs.

---

## Table of Contents

1. [`for` Loops – Iterating Over Sequences](#1-for-loops--iterating-over-sequences)
2. [`while` Loops – Repeating Based on a Condition](#2-while-loops--repeating-based-on-a-condition)
3. [Controlling Loop Flow: `break` and `continue`](#3-controlling-loop-flow-break-and-continue)
4. [Combining Loops with Conditionals](#4-combining-loops-with-conditionals)
5. [Practical Applications and Examples](#5-practical-applications-and-examples)

---

## Learning Objectives

By the end of this unit, you should be able to:

- ✓ Write `for` loops to iterate over lists, dictionaries, strings, and `range()`
- ✓ Write `while` loops to repeat code until a condition becomes `False`
- ✓ Use `range()` with start, stop, and step arguments
- ✓ Use `break` to exit a loop early and `continue` to skip the current iteration
- ✓ Combine loops with conditionals to solve multi-step real-world problems

---

## 1. `for` Loops – Iterating Over Sequences

The `for` loop is used to iterate over items in a sequence (such as a list, string, dictionary, or range). It executes the indented block once for each element, making it perfect for processing collections of data.

### Basic `for` Loop Structure

**Syntax:**

```python
for variable in sequence:
    # Code block executed for each item
    statement1
    statement2
```

The `variable` takes on the value of each element in the `sequence` one at a time.

### Iterating Over a List

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
```

**Output:**

```text
I like apple
I like banana
I like cherry
```

**More Examples:**

```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(f"Number: {num}, Squared: {num ** 2}")
```

**Output:**

```text
Number: 1, Squared: 1
Number: 2, Squared: 4
Number: 3, Squared: 9
Number: 4, Squared: 16
Number: 5, Squared: 25
```

### Iterating Over a String

When you iterate over a string, each character becomes the loop variable:

```python
for char in "Python":
    print(char)
```

**Output:**

```text
P
y
t
h
o
n
```

**Counting Characters:**

```python
word = "hello"
for char in word:
    print(f"'{char}' is at index {word.index(char)}")
```

**Output:**

```text
'h' is at index 0
'e' is at index 1
'l' is at index 2
'l' is at index 2
'o' is at index 4
```

### Iterating Over a Dictionary

When iterating over a dictionary with just `for key in dict`, you get the keys. You can access values using bracket notation, or use `.items()` to get both keys and values simultaneously.

#### Method 1: Keys Only

```python
person = {"name": "Alice", "age": 30, "city": "New York"}
for key in person:
    print(f"{key}: {person[key]}")
```

**Output:**

```text
name: Alice
age: 30
city: New York
```

#### Method 2: Keys and Values Together (Recommended)

```python
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key} → {value}")
```

**Output:**

```text
name → Alice
age → 30
city → New York
```

#### Method 3: Values Only

```python
person = {"name": "Alice", "age": 30, "city": "New York"}
for value in person.values():
    print(value)
```

**Output:**

```text
Alice
30
New York
```

### Using `range()` to Generate Sequences

The `range()` function generates a sequence of numbers. It's extremely useful for loops when you need to repeat something a specific number of times.

#### `range(stop)` – Numbers from 0 to stop-1

```python
for i in range(5):
    print(i)
```

**Output:**

```text
0
1
2
3
4
```

#### `range(start, stop)` – Numbers from start to stop-1

```python
for i in range(2, 8):
    print(i)
```

**Output:**

```text
2
3
4
5
6
7
```

#### `range(start, stop, step)` – Custom Increment

The `step` parameter lets you skip numbers:

```python
for i in range(1, 10, 2):
    print(i)
```

**Output:**

```text
1
3
5
7
9
```

**Counting Down:**

```python
for i in range(10, 0, -1):
    print(i)
```

**Output:**

```text
10
9
8
7
6
5
4
3
2
1
```

**Understanding range() Parameters:**

| Expression | Output |
| ---------- | ------ |
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(2, 7)` | 2, 3, 4, 5, 6 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 |
| `range(10, 0, -1)` | 10, 9, 8, ..., 2, 1 |
| `range(0, 20, 5)` | 0, 5, 10, 15 |

### Practical Example: Creating a Multiplication Table

```python
number = 7
for i in range(1, 11):
    print(f"{number} × {i} = {number * i}")
```

**Output:**

```text
7 × 1 = 7
7 × 2 = 14
7 × 3 = 21
7 × 4 = 28
7 × 5 = 35
7 × 6 = 42
7 × 7 = 49
7 × 8 = 56
7 × 9 = 63
7 × 10 = 70
```

---

## 2. `while` Loops – Repeating Based on a Condition

The `while` loop continues to execute as long as a given condition is `True`. Unlike `for` loops, `while` loops don't iterate over a predetermined sequence. Instead, they repeat as long as a condition remains true. This is useful when you don't know in advance how many iterations you need.

### Basic `while` Loop Structure

**Syntax:**

```python
while condition:
    # Code block executed while condition is True
    statement1
    statement2
    # IMPORTANT: Update the condition inside the loop!
```

### Simple Example

```python
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1
```

**Output:**

```text
Count is 0
Count is 1
Count is 2
Count is 3
Count is 4
```

### Important: Avoiding Infinite Loops

You **must** update the condition inside the loop, or the loop will run forever (infinite loop).

**Bad Example (Infinite Loop!):**

```python
count = 0
while count < 5:
    print(f"Count is {count}")
    # count is never incremented, so this runs forever!
```

**Good Example:**

```python
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1  # Increment count each iteration
```

### Real-World Example: User Validation

```python
password = ""
while len(password) < 8:
    password = input("Enter a password (at least 8 characters): ")
    if len(password) < 8:
        print("Password too short. Try again.")

print("Password accepted!")
```

**Sample Run:**

```text
Enter a password (at least 8 characters): abc
Password too short. Try again.
Enter a password (at least 8 characters): password123
Password accepted!
```

### Real-World Example: Sum Until User Stops

```python
total = 0
while True:
    user_input = input("Enter a number (or 'done' to stop): ")
    if user_input.lower() == "done":
        break
    total += int(user_input)

print(f"Total sum: {total}")
```

**Sample Run:**

```text
Enter a number (or 'done' to stop): 10
Enter a number (or 'done' to stop): 20
Enter a number (or 'done' to stop): 15
Enter a number (or 'done' to stop): done
Total sum: 45
```

---

## 3. Controlling Loop Flow: `break` and `continue`

### `break` – Exit the Loop Immediately

The `break` statement terminates the loop entirely and execution continues with the code after the loop.

**Use Case:** Exit early when a condition is met.

```python
for num in range(10):
    if num == 5:
        break
    print(num)
```

**Output:**

```text
0
1
2
3
4
```

The loop stops as soon as `num` equals 5, even though the loop was supposed to go to 10.

### Example: Searching for a Value

```python
items = ["apple", "banana", "cherry", "date", "elderberry"]
search = "cherry"

for item in items:
    if item == search:
        print(f"Found {search}!")
        break
else:
    print(f"{search} not found.")
```

**Output:**

```text
Found cherry!
```

### `continue` – Skip to the Next Iteration

The `continue` statement skips the rest of the current iteration and jumps to the next one.

**Use Case:** Skip elements that meet certain conditions.

```python
for num in range(5):
    if num == 2:
        continue
    print(num)
```

**Output:**

```text
0
1
3
4
```

Notice that 2 is skipped.

### Example: Filtering Numbers

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers
    print(f"{num} is odd")
```

**Output:**

```text
1 is odd
3 is odd
5 is odd
7 is odd
9 is odd
```

### Comparison: `break` vs `continue`

| Statement | Effect | Continues Loop? |
| --------- | ------ | --------------- |
| `break` | Exits the loop entirely | No |
| `continue` | Skips to next iteration | Yes |
| No control statement | Executes normally | Yes |

### Nested Loop with `break`

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # Only breaks inner loop
        print(f"i={i}, j={j}")
```

**Output:**

```text
i=0, j=0
i=1, j=0
i=2, j=0
```

---

## 4. Combining Loops with Conditionals

One of the most powerful features of programming is combining loops with conditional statements. This allows you to make decisions about each element as you process them.

### Pattern: Loop + If Statement

```python
for element in sequence:
    if condition:
        # do something
    else:
        # do something else
```

### Example 1: Find Even Numbers

```python
numbers = [10, 15, 22, 37, 40]
for n in numbers:
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")
```

**Output:**

```text
10 is even
15 is odd
22 is even
37 is odd
40 is even
```

### Example 2: Grade Assignment

```python
scores = [95, 82, 78, 91, 65]
for score in scores:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    print(f"Score: {score} → Grade: {grade}")
```

**Output:**

```text
Score: 95 → Grade: A
Score: 82 → Grade: B
Score: 78 → Grade: C
Score: 91 → Grade: A
Score: 65 → Grade: F
```

### Example 3: User Validation with while and Conditionals

```python
while True:
    password = input("Enter password (or 'quit' to exit): ")
    if password.lower() == "quit":
        print("Goodbye!")
        break
    if len(password) < 8:
        print("Password too short, try again.")
        continue
    print("Password accepted!")
    break
```

**Sample Run:**

```text
Enter password (or 'quit' to exit): hi
Password too short, try again.
Enter password (or 'quit' to exit): mysecurepass123
Password accepted!
```

### Example 4: Processing a List with Conditions

```python
items = ["apple", 5, "banana", 12, "cherry", 3, "date"]
total = 0
for item in items:
    if isinstance(item, int):  # Check if item is an integer
        total += item
        print(f"Added {item}. Running total: {total}")
    else:
        print(f"Skipped '{item}' (not a number)")

print(f"Final total: {total}")
```

**Output:**

```text
Skipped 'apple' (not a number)
Added 5. Running total: 5
Skipped 'banana' (not a number)
Added 12. Running total: 17
Skipped 'cherry' (not a number)
Added 3. Running total: 20
Skipped 'date' (not a number)
Final total: 20
```

---

## 5. Practical Applications and Examples

### Project 1: Number Statistics Program

Write a Python script that continuously asks the user to enter numbers. The program should:

1. Start with an empty list
2. Use a `while` loop to repeatedly ask for a number
3. If the user enters "done" (case-insensitive), break out of the loop
4. Otherwise, convert the input to a float and append it to the list
5. After the loop ends, if there is at least one number, print:
   - The total count of numbers
   - The sum
   - The average
   - The maximum
   - The minimum
6. If no numbers were entered, print a friendly message

**Solution:**

```python
numbers = []

while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    
    if user_input.lower() == "done":
        break
    
    try:
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        print("That's not a valid number. Try again.")
        continue

if numbers:
    print(f"\nCount: {len(numbers)}")
    print(f"Sum: {sum(numbers)}")
    print(f"Average: {sum(numbers) / len(numbers)}")
    print(f"Max: {max(numbers)}")
    print(f"Min: {min(numbers)}")
else:
    print("No numbers were entered.")
```

**Example Run:**

```text
Enter a number (or 'done' to finish): 10
Enter a number (or 'done' to finish): 25.5
Enter a number (or 'done' to finish): 3
Enter a number (or 'done' to finish): done

Count: 3
Sum: 38.5
Average: 12.833333333333334
Max: 25.5
Min: 3.0
```

### Project 2: Guessing Game

Build an interactive guessing game where the computer picks a random number between 1 and 100, and the player tries to guess it.

**Requirements:**

- Use `import random` and `random.randint(1, 100)` to generate the secret number
- Use a `while` loop to repeatedly ask the user for their guess
- For each guess:
  - If the guess is too low, print "Too low!"
  - If too high, print "Too high!"
  - If correct, print "Congratulations! You got it!" and break out of the loop
- Keep track of the number of attempts and display it when the game ends
- Allow the user to type "quit" to exit early

**Solution:**

```python
import random

secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Type 'quit' at any time to give up.\n")

while True:
    try:
        user_input = input("Make a guess: ")
        
        if user_input.lower() == "quit":
            print(f"You quit! The number was {secret_number}.")
            break
        
        guess = int(user_input)
        
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue
        
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You got it!")
            print(f"The number was {secret_number}.")
            print(f"You took {attempts} attempt(s).")
            break
    
    except ValueError:
        print("That's not a valid number. Try again.")
```

**Example Run:**

```text
Welcome to the Guessing Game!
I'm thinking of a number between 1 and 100.
Type 'quit' at any time to give up.

Make a guess: 50
Too high! Try again.
Make a guess: 25
Too low! Try again.
Make a guess: 37
Too low! Try again.
Make a guess: 43
Too high! Try again.
Make a guess: 40
Congratulations! You got it!
The number was 40.
You took 4 attempt(s).
```

### Project 3: Pattern Printing

Create a program that prints different patterns using nested loops.

**Triangle Pattern:**

```python
size = 5
for i in range(1, size + 1):
    for j in range(i):
        print("*", end="")
    print()
```

**Output:**

```text
*
**
***
****
*****
```

**Multiplication Table:**

```python
print("Multiplication Table (1-10):")
print()

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4d}", end="")
    print()
```

**Output:**

```text
Multiplication Table (1-10):

   1   2   3   4   5   6   7   8   9  10
   2   4   6   8  10  12  14  16  18  20
   3   6   9  12  15  18  21  24  27  30
   4   8  12  16  20  24  28  32  36  40
   5  10  15  20  25  30  35  40  45  50
   6  12  18  24  30  36  42  48  54  60
   7  14  21  28  35  42  49  56  63  70
   8  16  24  32  40  48  56  64  72  80
   9  18  27  36  45  54  63  72  81  90
  10  20  30  40  50  60  70  80  90 100
```

### Project 4: Data Processing

Read a list of scores and categorize them.

```python
scores = [45, 78, 92, 65, 88, 55, 100, 72]

categories = {
    "Excellent (90+)": [],
    "Good (80-89)": [],
    "Satisfactory (70-79)": [],
    "Needs Improvement (60-69)": [],
    "Below 60": []
}

for score in scores:
    if score >= 90:
        categories["Excellent (90+)"].append(score)
    elif score >= 80:
        categories["Good (80-89)"].append(score)
    elif score >= 70:
        categories["Satisfactory (70-79)"].append(score)
    elif score >= 60:
        categories["Needs Improvement (60-69)"].append(score)
    else:
        categories["Below 60"].append(score)

for category, scores_list in categories.items():
    print(f"{category}: {scores_list}")
```

**Output:**

```text
Excellent (90+): [92, 100]
Good (80-89): [78, 88]
Satisfactory (70-79): [72]
Needs Improvement (60-69): [65]
Below 60: [45, 55]
```

---

## Key Differences: `for` vs `while`

| Feature | `for` Loop | `while` Loop |
| ------- | ---------- | ------------ |
| **Best for** | Iterating over sequences | Repeating while condition is true |
| **Iterations** | Known in advance | Unknown/variable |
| **Typical use** | Processing lists, dictionaries, ranges | User input, state changes |
| **Syntax** | `for item in sequence:` | `while condition:` |
| **Risk** | Low (sequence is finite) | High (infinite loops if not careful) |

**Choose `for` when:** You know what you're iterating over (a list, range, string, etc.)

**Choose `while` when:** You need to repeat until a condition changes, and you don't know how many times that will be.

---

## Common Loop Patterns

### Pattern 1: Accumulator

```python
total = 0
for num in [1, 2, 3, 4, 5]:
    total += num
print(total)  # 15
```

### Pattern 2: Counter

```python
count = 0
for letter in "hello":
    count += 1
print(count)  # 5
```

### Pattern 3: Filtering

```python
even_numbers = []
for num in range(1, 11):
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)  # [2, 4, 6, 8, 10]
```

### Pattern 4: Transforming

```python
numbers = [1, 2, 3, 4, 5]
squared = []
for num in numbers:
    squared.append(num ** 2)
print(squared)  # [1, 4, 9, 16, 25]
```

### Pattern 5: Search

```python
items = ["apple", "banana", "cherry", "date"]
search = "cherry"
found = False

for item in items:
    if item == search:
        found = True
        break

print(f"Found: {found}")
```

---

## Summary

By mastering repetition in Python, you've learned:

- ✓ How to use `for` loops to iterate over sequences (lists, strings, dictionaries, ranges)
- ✓ How to use `while` loops for condition-based repetition
- ✓ How to control loop behavior with `break` and `continue`
- ✓ How to combine loops with conditionals for complex logic
- ✓ Common patterns for data processing and manipulation
- ✓ Real-world applications in games, validation, and data analysis

Loops are fundamental to programming. Mastering them opens the door to handling large amounts of data efficiently and writing dynamic, responsive programs!

---

## Practice Problems

### Easy

1. Write a `for` loop that prints all numbers from 1 to 10.

2. Write a `for` loop that prints every other number from 1 to 20.

3. Write a `for` loop that calculates the sum of numbers from 1 to 100.

4. Write a program that prints "Hello" 5 times using a `while` loop.

5. Write a program that asks the user for their name and age in a `while` loop, and exits when they type "quit".

### Medium

1. Write a program that finds all even numbers in a list and prints them.

2. Write a program that reverses the digits of a number (e.g., 12345 → 54321).

3. Create a program that asks the user for 5 numbers and finds the largest one.

4. Write a program that prints a multiplication table for a number entered by the user.

5. Create a program that counts how many vowels are in a string.

### Hard

1. Write a program that checks if a number is prime.

2. Create a program that finds all factors of a number.

3. Write a Fibonacci sequence generator that creates numbers up to a user-specified limit.

4. Create a program that simulates a simple slot machine with loops and conditionals.

5. Build a program that calculates statistics (mean, median, mode) for a list of numbers entered by the user.

---

## Challenge Projects

### Challenge 1: Number Pyramid

Create a program that prints a pyramid of numbers:

```text
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

### Challenge 2: Password Strength Checker

Create a program that validates passwords based on:

- At least 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character

Keep asking until a strong password is entered.

### Challenge 3: Interactive Quiz

Create a simple quiz game that:

- Stores questions and answers
- Loops through questions
- Keeps score
- Provides feedback (correct/incorrect)
- Shows final score and percentage

### Challenge 4: Prime Number Generator

Write a program that generates all prime numbers up to a number specified by the user.

### Challenge 5: Hangman Game

Create a hangman game where:

- Computer picks a random word
- Player guesses letters
- Display progress and remaining guesses
- End game on win or loss

Happy coding! 🐍

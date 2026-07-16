# String Manipulation and Formatting

Welcome to Unit 2!  
This unit will introduce you to the essential techniques for working with text in Python, an important skill in application development. You will explore how strings can be transformed, searched, measured, and organised using built-in tools. The unit also develops your ability to access and manipulate specific portions of text with precision. In addition, you will learn how to create clear, dynamic output by combining text with variables and expressions. Together, these skills will enable you to process and present text effectively in your Python programs.

## Learning Objectives

By the end of this unit, you should be able to:

- Apply at least 7 string methods including `upper`, `lower`, `title`, `strip`, `replace`, `find`, and `split`
- Use `len()` to count characters in a string
- Access individual characters and substrings using indexing and slicing
- Format output strings cleanly using f-strings
- Concatenate strings using `+` and format them with f-strings

---

## Activities

### Task 1: Username and Message Formatter

Write a Python script called `string_formatter.py` that takes a user’s first name, last name, and a short bio message as input, then applies multiple string transformations to produce a formatted user profile output. This simulates how a real app backend processes user-submitted text.

### Task 2: The Secure Password Hint Tool

Users often forget their passwords. Create a script called `PasswordHelp.py` that helps them by showing a secure hint.

1. Ask the user to input their secret password.
2. Use `.strip()` to clean up any accidental spaces they might have typed at the start or end.
3. Grab the very first letter and the very last letter of the password using string indexing.
4. Print a hint using an f-string that forces the letters into uppercase so they stand out. (e.g., “Your password hint: It starts with P and ends with N”).
